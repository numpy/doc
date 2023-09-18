#!/usr/bin/env python
"""
Update versionwarning.js and link it to docs

"""
import re
import os
import argparse
import html.parser
from packaging.version import parse as parse_version


class Scaper(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.numpy_versions = set()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href", "")
            if href:
                m = re.match("^[0-9.]+$", href)
                if m:
                    self.numpy_versions.add(parse_version(href))


def main():
    p = argparse.ArgumentParser(description=__doc__.strip())
    args = p.parse_args()

    scraper = Scaper()
    with open("index.html", "r", encoding="utf-8") as f:
        scraper.feed(f.read())
        scraper.close()

    # Update versionwarning.js
    with open("_static/versionwarning.js_t", "r", encoding="utf-8") as f:
        text = f.read()

    latest_version = str(max(scraper.numpy_versions))
    print("Latest NumPy version:", latest_version)
    text = text.replace("{{ NUMPY_LATEST_VERSION }}", latest_version)

    with open("_static/versionwarning.js", "w", encoding="utf-8") as f:
        f.write(text)

    # Update doctools.js
    for dirname in os.listdir():
        if not os.path.isdir(dirname):
            continue

        doctools_js = os.path.join(dirname, "_static", "doctools.js")
        if os.path.isfile(doctools_js):
            with open(doctools_js, "r", encoding="utf-8") as f:
                text = f.read()

            if "versionwarning.js" not in text:
                with open(doctools_js, "a", encoding="utf-8") as f:
                    f.write(
                        "\n"
                        'var script = document.createElement("script"); '
                        'script.type = "text/javascript"; '
                        'script.src = "/doc/_static/versionwarning.js"; '
                        "document.head.appendChild(script);"
                    )


if __name__ == "__main__":
    main()
