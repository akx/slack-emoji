import argparse
import requests
import json
import os
from multiprocessing.dummy import Pool as ThreadPool

sess = requests.Session()

def get_jobs():
	ap = argparse.ArgumentParser()
	ap.add_argument('file', metavar='JSON', nargs='+')
	args = ap.parse_args()
	jobs = []
	for filename in args.file:
		srcfile = os.path.splitext(os.path.basename(filename))[0]
		with open(filename) as infp:
			for emoji in json.load(infp):
				ext = os.path.splitext(emoji["url"])[1]
				name = emoji["name"]
				jobs.append({
					"src": emoji["url"],
					"dest": f"{srcfile}/{name}{ext}"
				})
	return jobs


def download_job(job):
	if os.path.isfile(job["dest"]):
		return
	os.makedirs(os.path.dirname(job["dest"]), exist_ok=True)
	print(job["dest"])
	resp = requests.get(job["src"])
	resp.raise_for_status()
	with open(job["dest"], "wb") as outf:
		outf.write(resp.content)


if __name__ == '__main__':
	jobs = get_jobs()
	with ThreadPool() as pool:
		list(pool.imap_unordered(download_job, jobs))