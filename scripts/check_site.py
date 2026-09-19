"""Validate generated routes, local assets, fragments, and publication output."""
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

root = Path("_site").resolve()
required = ["index.html", "cv/index.html", "projects/index.html", "404.html", "publications.bib"]
for route in required:
    assert (root / route).is_file(), f"Missing route: {route}"

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids, self.links = set(), []
        self.sections, self.metadata, self.schemas = [], {}, []
        self.title, self._in_title, self._json = '', False, None
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'section' and 'id' in attrs:
            self.sections.append(attrs['id'])
        if tag == 'title':
            self._in_title = True
        if tag == 'meta':
            self.metadata[attrs.get('name', attrs.get('property'))] = attrs.get('content')
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self._json = ''
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate id: {attrs['id']}"
            self.ids.add(attrs["id"])
        if tag in ("a", "link", "img", "script"):
            value = attrs.get("href") if tag in ("a", "link") else attrs.get("src")
            if value:
                self.links.append(value)

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._json is not None:
            self._json += data

    def handle_endtag(self, tag):
        if tag == 'title':
            self._in_title = False
        if tag == 'script' and self._json is not None:
            self.schemas.append(json.loads(self._json))
            self._json = None

pages = {p.resolve(): Page(p) for p in root.rglob("*.html")}
for path, page in pages.items():
    for link in page.links:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc:
            continue
        target = (root / unquote(parsed.path).lstrip("/")) if parsed.path.startswith("/") else (path.parent / unquote(parsed.path)) if parsed.path else path
        target = target.resolve()
        if target.is_dir():
            target /= "index.html"
        assert target.is_relative_to(root) and target.exists(), f"{path}: broken local link {link}"
        if parsed.fragment and target in pages:
            assert unquote(parsed.fragment) in pages[target].ids, f"{path}: missing fragment {link}"
home = pages[root / "index.html"]
assert home.sections == ['about', 'research', 'ongoing-research', 'publications', 'projects', 'cv', 'contact']
assert home.title == 'Xincheng Li | Control Theory, Robotics & Geometric Control'
assert home.metadata['og:title'] == home.title
assert 'University of South Florida' in home.metadata['description']
assert home.metadata['og:description'] == home.metadata['description']
assert len(home.schemas) == 1
schema = home.schemas[0]
assert schema['@type'] == 'ProfilePage'
person = schema['mainEntity']
assert person['@type'] == 'Person' and person['name'] == 'Xincheng Li'
assert person['url'] == 'https://xincheng.li/'
assert person['image'] == home.metadata['og:image']
assert person['image'].startswith('https://xincheng.li/assets/')
assert person['affiliation']['name'] == 'University of South Florida'
assert person['jobTitle'] == 'Postdoctoral Scholar' and person['knowsAbout']
assert {'https://orcid.org/0009-0004-3636-4460', 'https://scholar.google.com/citations?user=qaGHO34AAAAJ&hl=en'} <= set(person['sameAs'])
assert set(person['sameAs'][:2]) <= set(home.links)
bib = (root / "publications.bib").read_text(encoding="utf-8")
assert "@article" in bib and "@phdthesis" in bib and "{{" not in bib
print(f"Checked {len(pages)} HTML pages, section order, metadata, identity JSON-LD, local links, and BibTeX.")
