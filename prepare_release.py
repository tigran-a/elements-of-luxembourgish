#!/usr/bin/env python3
"""
Prepares assets and release notes for GitHub Releases.
Resolves dynamic URLs for finalized volumes and packages modified PDFs.
"""
import os
import json
import shutil
import urllib.request

def main():
    repo = os.environ.get("GITHUB_REPOSITORY", "tigran-a/elements-of-luxembourgish")
    token = os.environ.get("GITHUB_TOKEN")
    rebuild_v1 = os.environ.get("REBUILD_V1") == "true"
    rebuild_v2 = os.environ.get("REBUILD_V2") == "true"
    rebuild_v3 = os.environ.get("REBUILD_V3") == "true"
    force = os.environ.get("FORCE_REBUILD") == "true"
    tag = os.environ.get("GITHUB_REF_NAME", "latest")

    os.makedirs("release_assets", exist_ok=True)

    # Fallback URLs if API query fails
    v1_url = f"https://github.com/{repo}/releases/download/v0.1.35/letz.pdf"
    v2_url = f"https://github.com/{repo}/releases/download/v0.1.35/letz2.pdf"

    # Query GitHub API to locate the latest published releases containing Volume 1 and Volume 2
    try:
        headers = {"User-Agent": "CI"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        req = urllib.request.Request(f"https://api.github.com/repos/{repo}/releases", headers=headers)
        with urllib.request.urlopen(req) as resp:
            releases = json.loads(resp.read().decode())
        
        found_v1, found_v2 = False, False
        for rel in releases:
            for asset in rel.get("assets", []):
                name = asset.get("name")
                dl = asset.get("browser_download_url")
                if name == "letz.pdf" and not found_v1:
                    v1_url = dl
                    found_v1 = True
                if name == "letz2.pdf" and not found_v2:
                    v2_url = dl
                    found_v2 = True
    except Exception as e:
        print(f"Notice: using default release asset URLs ({e})")

    # If rebuilt in THIS release, it will be uploaded under this tag
    if rebuild_v1 or force:
        v1_url = f"https://github.com/{repo}/releases/download/{tag}/letz.pdf"
    if rebuild_v2 or force:
        v2_url = f"https://github.com/{repo}/releases/download/{tag}/letz2.pdf"

    print(f"Target Volume 1 download URL: {v1_url}")
    print(f"Target Volume 2 download URL: {v2_url}")

    # Write browser shortcut files
    with open("release_assets/Volume_1_Download_Link.url", "w", encoding="utf-8") as f:
        f.write(f"[InternetShortcut]\nURL={v1_url}\n")
    with open("release_assets/Volume_2_Download_Link.url", "w", encoding="utf-8") as f:
        f.write(f"[InternetShortcut]\nURL={v2_url}\n")

    # Write text summary file
    with open("release_assets/VOLUMES_LINKS.txt", "w", encoding="utf-8") as f:
        f.write("Elements of Luxembourgish - Volume Download Links\n\n")
        f.write(f"Volume 1 (Lessons 1-20):\n{v1_url}\n\n")
        f.write(f"Volume 2 (Lessons 21-31):\n{v2_url}\n\n")
        f.write(f"Volume 3 (Lessons 32+, Active):\nAttached as letz3.pdf in release {tag}\n")

    # Generate dynamic release body markdown
    v1_status = "*(Updated & attached to this release)*" if (rebuild_v1 or force) else "*(Stable / Finalized)*"
    v2_status = "*(Updated & attached to this release)*" if (rebuild_v2 or force) else "*(Stable / Finalized)*"

    body = (
        f"## Elements of Luxembourgish ({tag})\n\n"
        f"### Course Volumes:\n"
        f"* **Volume 1 (Lessons 1–20)**: [Download `letz.pdf`]({v1_url}) {v1_status}\n"
        f"* **Volume 2 (Lessons 21–31)**: [Download `letz2.pdf`]({v2_url}) {v2_status}\n"
        f"* **Volume 3 (Lessons 32+)**: Download attached `letz3.pdf` below *(Active / Growing)*\n"
    )

    with open("release_body.md", "w", encoding="utf-8") as f:
        f.write(body)

    # Attach PDFs only for volumes that were rebuilt or changed
    if (rebuild_v1 or force) and os.path.exists("letz.pdf"):
        print("Attaching Volume 1 PDF to this release...")
        shutil.copy("letz.pdf", "release_assets/letz.pdf")

    if (rebuild_v2 or force) and os.path.exists("letz2.pdf"):
        print("Attaching Volume 2 PDF to this release...")
        shutil.copy("letz2.pdf", "release_assets/letz2.pdf")

    if (rebuild_v3 or force or os.path.exists("letz3.pdf")) and os.path.exists("letz3.pdf"):
        print("Attaching Volume 3 PDF to this release...")
        shutil.copy("letz3.pdf", "release_assets/letz3.pdf")

if __name__ == "__main__":
    main()
