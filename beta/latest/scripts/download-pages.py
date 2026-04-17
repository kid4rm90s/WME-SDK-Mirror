"""
download-pages.py
=================
Downloads all Waze SDK documentation pages listed in url-list.txt
and saves them as HTML files into the local folder structure that
extract-to-md.py expects.

Also downloads and extracts the SDK TypeScript typings tarball
(wme-sdk-typings.tgz) into the TypeDefs/ folder so type definitions
stay in sync with the HTML docs on every refresh.

Pipeline:
  build-url-list.py  ->  download-pages.py  ->  extract-to-md.py  ->  create-grouped-md-files.py

Usage:
  py download-pages.py               # download HTML pages + typedefs
  py download-pages.py --dry-run     # show what would be saved, don't write files
  py download-pages.py --force       # re-download even if HTML file already exists
  py download-pages.py --no-typedefs # skip the typings tarball
  py download-pages.py --url-list my-other-list.txt
"""

import io
import os
import re
import sys
import time
import tarfile
import argparse
import requests
import urllib3
from urllib.parse import urlparse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_DIR       = os.path.dirname(os.path.abspath(__file__))
URL_LIST       = os.path.join(BASE_DIR, "url-list.txt")
TYPEDEFS_DIR   = os.path.join(BASE_DIR, "TypeDefs")
TYPINGS_URL    = "https://web-assets.waze.com/wme_sdk_docs/beta/latest/wme-sdk-typings.tgz"
VERIFY_SSL     = False
DELAY_SEC      = 0.3   # polite delay between requests


def make_session():
    s = requests.Session()
    s.headers["User-Agent"] = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
    return s


def url_to_local_path(url, base_dir):
    """
    Convert a full URL to a local file path under base_dir.
    e.g. https://www.waze.com/editor/sdk/classes/index.SDK.Foo.html
         -> <base_dir>/classes/index.SDK.Foo.html
    """
    parsed = urlparse(url)
    path = parsed.path
    m = re.search(r'/sdk/(.*)', path)
    if m:
        rel = m.group(1)
    else:
        rel = os.path.basename(path)
    return os.path.join(base_dir, rel.replace("/", os.sep))


def download(url, local_path, session, dry_run=False, force=False):
    """
    Download one URL and save to local_path.
    Returns one of: 'skipped', 'downloaded', 'error'
    """
    if not force and os.path.exists(local_path):
        return "skipped"

    if dry_run:
        print(f"  [dry-run] would save -> {os.path.relpath(local_path, BASE_DIR)}")
        return "dry-run"

    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    try:
        resp = session.get(url, timeout=30, verify=VERIFY_SSL)
        resp.raise_for_status()
        with open(local_path, "wb") as f:
            f.write(resp.content)
        return "downloaded"
    except requests.HTTPError as e:
        print(f"  [HTTP {e.response.status_code}] {url}")
        return "error"
    except Exception as e:
        print(f"  [error] {url}: {e}")
        return "error"


def download_typedefs(session, dry_run=False, force=False):
    """
    Downloads wme-sdk-typings.tgz and extracts all .d.ts files into TypeDefs/.
    Returns list of extracted file names, or empty list on failure.
    """
    print(f"\n[Typedefs] Fetching {TYPINGS_URL}")

    if dry_run:
        print("  [dry-run] would download and extract .d.ts files to TypeDefs/")
        return []

    try:
        resp = session.get(TYPINGS_URL, timeout=60, verify=VERIFY_SSL)
        resp.raise_for_status()
    except Exception as e:
        print(f"  [error] Could not download typings tarball: {e}")
        return []

    os.makedirs(TYPEDEFS_DIR, exist_ok=True)
    extracted = []

    # The tarball contains package/index.d.ts — the main WME SDK type definitions.
    # We save it as wmeSDK_typedefs.d.ts to match the name the rest of the pipeline expects.
    TARBALL_MAP = {
        "package/index.d.ts": "wmeSDK_typedefs.d.ts",
    }

    try:
        with tarfile.open(fileobj=io.BytesIO(resp.content), mode="r:gz") as tar:
            for member in tar.getmembers():
                if member.name not in TARBALL_MAP:
                    continue
                dst_name = TARBALL_MAP[member.name]
                dst_path = os.path.join(TYPEDEFS_DIR, dst_name)

                if not force and os.path.exists(dst_path):
                    print(f"  exists  TypeDefs/{dst_name}")
                    continue

                f = tar.extractfile(member)
                if f is None:
                    continue
                content = f.read()
                with open(dst_path, "wb") as out:
                    out.write(content)
                print(f"  OK      TypeDefs/{dst_name}")
                extracted.append(dst_name)
    except Exception as e:
        print(f"  [error] Could not extract typings tarball: {e}")
        return []

    if not extracted:
        print("  (all .d.ts files already up to date)")
    else:
        print(f"  Extracted {len(extracted)} .d.ts file(s)")

    return extracted


def main():
    parser = argparse.ArgumentParser(
        description="Download Waze SDK HTML pages and TypeScript typedefs"
    )
    parser.add_argument(
        "--url-list", default=URL_LIST,
        help="Path to URL list file (default: url-list.txt)"
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Re-download files even if they already exist locally"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be downloaded without writing any files"
    )
    parser.add_argument(
        "--delay", type=float, default=DELAY_SEC,
        help=f"Seconds to wait between requests (default: {DELAY_SEC})"
    )
    parser.add_argument(
        "--no-typedefs", action="store_true",
        help="Skip downloading the TypeScript typings tarball"
    )
    args = parser.parse_args()

    # Read URL list
    if not os.path.exists(args.url_list):
        print(f"ERROR: URL list not found: {args.url_list}")
        print("Run build-url-list.py first.")
        sys.exit(1)

    with open(args.url_list, encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    print(f"URL list: {args.url_list} ({len(urls)} URLs)")
    if args.dry_run:
        print("Mode: dry-run (no files will be written)")
    elif args.force:
        print("Mode: force (re-downloading all files)")
    else:
        print("Mode: incremental (skipping files that already exist)")
    print()

    session = make_session()
    counts = {"downloaded": 0, "skipped": 0, "dry-run": 0, "error": 0}
    errors = []

    # Top-level pages always re-downloaded (they carry the WME version string)
    TOP_LEVEL_PAGES = {"index.html", "modules.html"}

    # ── HTML pages ────────────────────────────────────────────────────────────
    for i, url in enumerate(urls, 1):
        local_path = url_to_local_path(url, BASE_DIR)
        rel = os.path.relpath(local_path, BASE_DIR)
        force_this = args.force or (os.path.basename(local_path) in TOP_LEVEL_PAGES)

        status = download(url, local_path, session, dry_run=args.dry_run, force=force_this)
        counts[status] += 1

        if status == "downloaded":
            print(f"  [{i:3d}/{len(urls)}] OK      {rel}")
            time.sleep(args.delay)
        elif status == "skipped":
            print(f"  [{i:3d}/{len(urls)}] exists  {rel}")
        elif status == "error":
            errors.append(url)

    # ── TypeScript typedefs ───────────────────────────────────────────────────
    if not args.no_typedefs:
        download_typedefs(session, dry_run=args.dry_run, force=args.force)

    # ── Summary ───────────────────────────────────────────────────────────────
    print()
    print("=" * 50)
    print("Done.")
    if args.dry_run:
        print(f"  Would download: {counts['dry-run']}")
    else:
        print(f"  Downloaded: {counts['downloaded']}")
        print(f"  Skipped:    {counts['skipped']}  (already existed)")
        print(f"  Errors:     {counts['error']}")

    if errors:
        print()
        print("Failed URLs:")
        for e in errors:
            print(f"  {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
