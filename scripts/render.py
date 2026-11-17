"""Local preview and freeze tool for the Research Design site.

GitHub Pages builds the real site with Jekyll. This script imitates the
small part of Jekyll the site uses (Liquid includes, the schedule data,
Markdown, the default layout), so the site can be checked on a machine
without Ruby, and so the assignment briefs can be frozen with their dates
written out for the yearly archive.

  python3 scripts/render.py preview OUTDIR       build an HTML preview
  python3 scripts/render.py freeze YEAR          write archive/YEAR/*.md

Needs: pip install python-liquid markdown-it-py pyyaml
"""
import datetime
import os
import re
import sys

import liquid
import yaml
from markdown_it import MarkdownIt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = yaml.safe_load(open(os.path.join(ROOT, "_config.yml")))
BASEURL = CONFIG.get("baseurl", "")
SITEURL = CONFIG.get("url", "")
BRIEFS = ["checkpoint-1", "checkpoint-2", "communication-portfolio", "research-proposal"]


def load_site():
    site = dict(CONFIG)
    site["data"] = {}
    for name in os.listdir(os.path.join(ROOT, "_data")):
        if name.endswith(".yml"):
            site["data"][name[:-4]] = yaml.safe_load(open(os.path.join(ROOT, "_data", name)))
    return site


# --- Liquid filters that behave like Jekyll's -----------------------------

def _strip_ctx(args):
    return [a for a in args if type(a).__name__ != "FilterContext"]


def f_where(*args, **_):
    seq, prop, value = _strip_ctx(args)[:3]
    return [x for x in (seq or []) if str(x.get(prop)) == str(value)]


def f_date(*args, **_):
    value, fmt = _strip_ctx(args)[:2]
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.strftime(fmt)
    return value


def make_env(absolute=False):
    env = liquid.Environment()
    env.filters["where"] = f_where
    env.filters["date"] = f_date
    prefix = (SITEURL + BASEURL) if absolute else BASEURL
    env.filters["relative_url"] = lambda *a, **k: prefix + _strip_ctx(a)[0]
    env.filters["absolute_url"] = lambda *a, **k: SITEURL + BASEURL + _strip_ctx(a)[0]
    return env


INCLUDE_RE = re.compile(r"\{%-?\s*include\s+([\w./-]+)((?:\s+\w+=\"[^\"]*\")*)\s*-?%\}")
PARAM_RE = re.compile(r"(\w+)=\"([^\"]*)\"")


def render_includes(text, env, site):
    def repl(m):
        params = dict(PARAM_RE.findall(m.group(2)))
        src = open(os.path.join(ROOT, "_includes", m.group(1))).read()
        return env.parse(src).render({"site": site, "include": params})
    return INCLUDE_RE.sub(repl, text)


def split_front_matter(text):
    if text.startswith("---\n"):
        _, fm, body = text.split("---\n", 2)
        return yaml.safe_load(fm) or {}, body
    return {}, text


def render_liquid(body, page, site, absolute=False):
    env = make_env(absolute)
    body = render_includes(body, env, site)
    return env.parse(body).render({"site": site, "page": page})


def page_url(path):
    rel = os.path.relpath(path, ROOT)
    stem = rel[:-3]
    if stem == "index":
        return "/"
    if stem.endswith("/index"):
        return "/" + stem[:-6] + "/"
    return "/" + stem + "/"


def preview(outdir):
    site = load_site()
    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    layout = open(os.path.join(ROOT, "_layouts", "default.html")).read()
    count = 0
    for dirpath, dirnames, files in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith((".", "_")) and d not in ("scripts",)]
        for f in files:
            if not f.endswith(".md") or f == "README.md":
                continue
            path = os.path.join(dirpath, f)
            fm, body = split_front_matter(open(path).read())
            page = dict(fm, url=page_url(path))
            html = md.render(render_liquid(body, page, site))
            html = add_ids(html)
            env = make_env()
            full = env.parse(render_includes(layout, env, site)).render({"site": site, "page": page, "content": html})
            out = os.path.join(outdir, page["url"].strip("/"), "index.html")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, "w").write(full)
            count += 1
    css = os.path.join(outdir, "assets", "css")
    os.makedirs(css, exist_ok=True)
    open(os.path.join(css, "style.css"), "w").write(open(os.path.join(ROOT, "assets", "css", "style.css")).read())
    print(f"preview: {count} pages in {outdir}")


def slug(text):
    # kramdown's auto_ids: lowercase, drop anything not a letter, digit, space or hyphen, spaces to hyphens
    text = re.sub(r"<[^>]+>", "", text).lower()
    text = re.sub(r"[^a-z0-9 \-]", "", text)
    text = re.sub(r"^[^a-z]+", "", text)
    return text.replace(" ", "-")


def add_ids(html):
    return re.sub(r"<h([1-6])>(.*?)</h\1>", lambda m: f'<h{m.group(1)} id="{slug(m.group(2))}">{m.group(2)}</h{m.group(1)}>', html)


def freeze(year):
    site = load_site()
    outdir = os.path.join(ROOT, "archive", year)
    os.makedirs(outdir, exist_ok=True)
    for b in BRIEFS:
        fm, body = split_front_matter(open(os.path.join(ROOT, "assignments", b + ".md")).read())
        text = render_liquid(body, dict(fm), site, absolute=True)
        head = f"---\ntitle: \"{fm['title']} ({year})\"\narchived: \"{year}\"\n---\n"
        open(os.path.join(outdir, b + ".md"), "w").write(head + text)
    index = [f"---\ntitle: \"Archive {year}\"\narchived: \"{year}\"\n---\n",
             f"# Assignment briefs as issued, {year}\n"]
    for b in BRIEFS:
        fm, _ = split_front_matter(open(os.path.join(ROOT, "assignments", b + ".md")).read())
        index.append(f"- [{fm['title']}]({{{{ '/archive/{year}/{b}/' | relative_url }}}})")
    open(os.path.join(outdir, "index.md"), "w").write("\n".join(index) + "\n")
    print(f"froze {len(BRIEFS)} briefs into {outdir}")


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "preview":
        preview(sys.argv[2])
    elif len(sys.argv) == 3 and sys.argv[1] == "freeze":
        freeze(sys.argv[2])
    else:
        print(__doc__)
        sys.exit(1)
