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

* In a Python 3 virtualenv (setting one up is beyond the scope of this document)
  with the `requests` package installed, 
  run `python3 download_from_lists.py myworkspace.json`.  Multiple JSON filenames
  are accepted.
* The script downloads all emoji described in the given JSON file into a directory named by
  the file's name, i.e. `myworkspace/partyparrot.gif`, etc.