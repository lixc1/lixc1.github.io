# Personal Website for Xincheng Li

A custom, responsive Jekyll site for [lixc1.github.io](https://lixc1.github.io). Content is rendered at build time; the site needs no client-side JavaScript, external fonts, theme, or runtime service. The existing MIT license is retained.

## Edit content

| File | What to edit |
| --- | --- |
| `_data/profile.yml` | Bio, role, contact links, optional portrait and PDF CV, update date |
| `_data/research.yml` | Research interests |
| `_data/ongoing_research.yml` | Current research directions |
| `_data/publications.yml` | Publications, statuses, links, summaries, and BibTeX |
| `_data/projects.yml` | Software, educational tools, and robotics implementations; public links are optional |
| `_config.yml` | Site URL, homepage title, and search description |
| `cv.html` | Appointment, education, and presentation details |
| `assets/css/site.css` | Colors, typography, responsive and print styles |

The homepage and CV share publication data. `publications.bib` is generated from the same records. Add publications in the order you want them displayed (newest first). Quote YAML values that contain colons. Prefer DOI, arXiv, and institutional repository links; label accepted papers accurately.

The homepage includes ProfilePage/Person JSON-LD from `_includes/person-schema.html`. Identity links, affiliation, portrait, and research areas come from `_data/profile.yml`; keep those fields aligned with the visible profile. ORCID and Google Scholar links also appear in Contact.

The supplied personal photo is stored at `assets/images/xincheng-li.png`. The updated three-page CV is at `assets/files/CV_Xincheng_Li.pdf`, with download links on the homepage and `/cv/`. Their paths are configured in `_data/profile.yml`. To revise and rebuild the PDF, edit `scripts/build_cv.py` and run it with Python and ReportLab installed. The `/cv/` page also provides a printable selected academic record.

## Local preview

Install Ruby 3.3 and Bundler, then run:

```sh
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000`. For validation:

```sh
bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py
```

The pull-request workflow runs these build and link checks. For a project-site preview, set `baseurl` to the path prefix; all local page and asset URLs use Jekyll's URL filters. The validation script targets the root user-site deployment (`baseurl: ""`).

## GitHub Pages

This repository retains a native Jekyll structure and is intended to publish from the root of `main`. In **Settings → Pages**, select **Deploy from a branch**, branch **main**, folder **/(root)** if that is not already configured. GitHub's Jekyll build will use the custom local layouts. The PR check workflow validates only; it does not deploy. Merge the pull request to publish through the configured Pages source. No custom domain is configured.

Repository Pages settings could not be read through the available connector; verify that setting once before merging. `/projects/` is provided to repair the original homepage's project link. The missing portrait reference and filler text have been replaced.

## Content sources

See [docs/content-sources.md](docs/content-sources.md) for the public records used to update the bio, publication statuses, CV, and software description. Current copy was checked in September 2026. The CV is a selected academic record, not an assertion of a complete employment or publication history.
