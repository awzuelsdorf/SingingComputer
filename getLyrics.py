#! /usr/bin/env python3

import re, requests, os, sys, bs4

def main():
	if len(sys.argv) != 3:
		sys.stderr.write("Usage: {0} <artist name> <song title>\n".format(sys.argv[0]))
		sys.exit(-1)

	urlFormat = "http://www.metrolyrics.com/{songTitle}-lyrics-{artist}.html"
	url = urlFormat.format(artist=sys.argv[1], songTitle=sys.argv[2])
    
	resp = requests.get(url, allow_redirects=True)

	if str(resp.status_code) != "200":
		sys.stderr.write("Could not find webpage \"{0}\"\n".format(url))
		sys.exit(-1)

	html = bs4.BeautifulSoup(resp.text, "html.parser")

	tempFile = open("/tmp/temp.html", "w")

	for tag in html.find_all('p'):
		if "class" in tag.attrs and tag.attrs["class"][0] == "verse":
			for content in tag.contents:
				print(re.sub("<[^>]*>", "", str(content)))

	tempFile.close()

if __name__ == "__main__":
    main()
