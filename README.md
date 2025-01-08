slack emoji downloader
======================

Getting emoji JSON
------------------

* Open up your Slack workspace's "Customize Emoji" page.
* Copy the code from `fetch-all-emoji-console-script.js` into the developer console
  on that page. (You may want to read the code first to make sure I'm not stealing
  your Slack token.)  
  The code will copy a JSON object onto your clipboard.
* Paste the JSON object into a file, say, `myworkspace.json`.

Downloading emoji from the JSON
-------------------------------

* Run `python3 download_from_lists.py myworkspace.json` using Python 3.6 or newer. 
  Multiple JSON filenames are accepted.
  * If you have [uv] installed, `uv run download_from_lists.py ...` will be much faster,
    as `uv` will install the `httpx` HTTP client for you, instead of the script needing to
    shell out to `curl`.
* The script downloads all emoji described in the given JSON file into a directory named by
  the file's name, i.e. `myworkspace/partyparrot.gif`, etc.

The `download_from_lists.py` script works faster if you have `requests` installed.
It will fall back to `curl` otherwise.

[uv]: https://docs.astral.sh/uv/
