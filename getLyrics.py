#! /usr/bin/env python3

import re, requests, sys, bs4, subprocess, os

def main():
	if len(sys.argv) != 4:
		sys.stderr.write("Usage: {0} (artist name) (song title) (path to espeak)\n".format(sys.argv[0]))
		sys.stderr.write("Perhaps you didn't put quotes around the song title and the artist's name?\n")
		sys.exit(-1)

	urlFormat = "http://www.metrolyrics.com/{songTitle}-lyrics-{artist}.html"
	url = urlFormat.format(artist=re.sub(" ", "-", sys.argv[1]),\
songTitle=re.sub(" ", "-", sys.argv[2]))

	resp = requests.get(url, allow_redirects=True)

	if str(resp.status_code) != "200":
		sys.stderr.write("Could not find webpage \"{0}\"\n".format(url))
		sys.exit(-1)

	html = bs4.BeautifulSoup(resp.text, "html.parser")

	for tag in html.find_all('p'):
		if "class" in tag.attrs and tag.attrs["class"][0] == "verse":
			for content in tag.contents:
				text = re.sub("<[^>]*>", "", str(content))
				retVal = os.system("echo \"{0}\" | {1}".format(text, sys.argv[3]))

				if retVal != 0:
					sys.stderr.write("espeak failed with error code {0}\n".format(retVal))
					sys.exit(-1)

if __name__ == "__main__":
    main()
