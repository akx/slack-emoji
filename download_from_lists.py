# /// script
# dependencies = ["httpx"]
# ///
import argparse
import json
import os
import shutil
import subprocess
from multiprocessing.dummy import Pool as ThreadPool

try:
    import httpx

    sess = httpx.Client()
    print("Using httpx for downloads.")
except ImportError:
    sess = None
    curl = shutil.which("curl")
    if not curl:
        raise RuntimeError(
            "Please install the Python `httpx` package, or have curl on your path"
        )
    print(f"Using {curl} for downloads.")


def get_jobs():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", metavar="JSON", nargs="+")
    args = ap.parse_args()
    jobs = []
    for filename in args.file:
        srcfile = os.path.splitext(os.path.basename(filename))[0]
        with open(filename, encoding="utf-8") as infp:
            for emoji in json.load(infp):
                ext = os.path.splitext(emoji["url"])[1]
                name = emoji["name"]
                jobs.append({"src": emoji["url"], "dest": f"{srcfile}/{name}{ext}"})
    return jobs


def download_job(job):
    if os.path.isfile(job["dest"]):
        return
    os.makedirs(os.path.dirname(job["dest"]), exist_ok=True)
    print(job["dest"])
    if sess:
        resp = sess.get(job["src"])
        resp.raise_for_status()
        with open(job["dest"], "wb") as outf:
            outf.write(resp.content)
    else:
        subprocess.check_call([curl, "-R", "-s", "-o", job["dest"], job["src"]])


if __name__ == "__main__":
    jobs = get_jobs()
    with ThreadPool() as pool:
        list(pool.imap_unordered(download_job, jobs))
