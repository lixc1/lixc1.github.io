"""Validate generated routes, local assets, fragments, and publication output."""
from html.parser import HTMLParser
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
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate id: {attrs['id']}"
            self.ids.add(attrs["id"])
        if tag in ("a", "link", "img", "script"):
            value = attrs.get("href") if tag in ("a", "link") else attrs.get("src")
            if value:
                self.links.append(value)

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
assert {"about", "research", "publications", "projects", "cv", "contact"} <= home.ids
bib = (root / "publications.bib").read_text(encoding="utf-8")
assert "@article" in bib and "@phdthesis" in bib and "{{" not in bib
print(f"Checked {len(pages)} HTML pages, required sections, local links, and BibTeX.")

