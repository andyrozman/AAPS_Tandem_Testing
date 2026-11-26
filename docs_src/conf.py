# Sphinx configuration for the AAPS Tandem Mobi driver documentation.
#
# Build locally:
#   pip install -r docs_src/requirements.txt
#   sphinx-build -W --keep-going -b html docs_src _build/html
#
# Published two ways, both from this same configuration:
#   - GitHub Pages, by .github/workflows/docs.yml
#   - Read the Docs, by .readthedocs.yaml at the repo root
#
# Pages are written in MyST Markdown (.md), the same format used by the
# official AndroidAPS documentation, so pages can be moved upstream later
# with minimal changes.

import os
from datetime import date

ON_RTD = os.environ.get("READTHEDOCS") == "True"

# -- Project information -----------------------------------------------------

project = "AAPS Tandem Mobi Driver"
author = "Andy Rozman (AAPS driver) and James Woglom (PumpX2 library)"
copyright = f"2025-{date.today():%y}, {author}"

# Driver version this documentation describes. Bump with each tagged release.
version = "0.10.1.x"
release = "v0.10.1.1 (24.11.2026 - dev 4.0.1-dev-a (24.11.2026) (Phase 5 / Beta)"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx.ext.autosectionlabel",
    # Writes .nojekyll into the output so GitHub Pages serves _static/ and
    # _images/ (Jekyll would otherwise hide folders starting with "_").
    "sphinx.ext.githubpages",
]

source_suffix = {".md": "markdown"}
root_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md"]

# Allow :ref:`page:Section title` cross-references without explicit labels.
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3

myst_enable_extensions = [
    "colon_fence",   # ::: fences for directives
    "deflist",
    "attrs_inline",  # {width=...} on inline images
    "attrs_block",
    "substitution",
    "tasklist",      # - [ ] / - [x] checklists (Todo page)
]
myst_heading_anchors = 3

myst_substitutions = {
    "controlx2_version": "1.0.0-20251224",
    "version": version,
}

# Broken links and missing images already fail the build through -W (CI and
# Read the Docs). nitpicky would also flag unresolved Python/C references,
# which these docs don't use.
nitpicky = False

# -- HTML output -------------------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_title = "AAPS Tandem Mobi Driver"
html_static_path = ["_static"]
# Copied as-is to the site root: redirect pages for URLs of the old hand-written
# site (e.g. index_phase_1.html), so existing links keep working.
html_extra_path = ["_extra"]
html_css_files = ["custom.css"]
html_js_files = ["legacy-anchors.js"]
html_last_updated_fmt = "%B %d, %Y"
html_show_sourcelink = False

html_theme_options = {
    "navigation_depth": 3,
    "collapse_navigation": False,
    "style_external_links": True,
}

# "Edit on GitHub" links point at the repo and branch being built, so a fork
# (e.g. a work-in-progress copy on someone's own GitHub Pages) links to itself.
# GitHub Actions sets GITHUB_REPOSITORY; the workflow sets DOCS_BRANCH.
# Local and Read the Docs builds fall back to the main repo.
_gh_owner, _gh_repo = os.environ.get(
    "GITHUB_REPOSITORY", "andyrozman/AAPS_Tandem_Testing"
).split("/", 1)

html_context = {
    "display_github": True,
    "github_user": _gh_owner,
    "github_repo": _gh_repo,
    "github_version": os.environ.get("DOCS_BRANCH", "testing"),
    "conf_py_path": "/docs_src/",
}

# -- Canonical URL: Read the Docs and GitHub Pages ---------------------------
# Read the Docs no longer injects settings into conf.py, so take the canonical
# URL from the environment it provides and tell the theme it is running there
# (enables the version and search add-ons).
# The GitHub Pages workflow passes the site URL in DOCS_BASEURL. If that is a
# custom domain, sphinx.ext.githubpages also writes the CNAME file.
# Local builds set neither, so they get no canonical link.

html_baseurl = (
    os.environ.get("READTHEDOCS_CANONICAL_URL")
    or os.environ.get("DOCS_BASEURL", "")
)
if html_baseurl and not html_baseurl.endswith("/"):
    html_baseurl += "/"
if ON_RTD:
    html_context["READTHEDOCS"] = True
