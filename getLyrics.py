import re, requests, sys, bs4, subprocess, os

def main():
	if len(sys.argv) < 3:
		sys.stderr.write("Usage: {0} (artist name) (song title) (path to espeak or say)\n".format(sys.argv[0]))
		sys.stderr.write("Perhaps you didn't put quotes around the song title and the artist's name?\n")
		sys.exit(-1)

	urlFormat = "http://www.metrolyrics.com/{songTitle}-lyrics-{artist}.html"
	url = urlFormat.format(artist=re.sub(" ", "-", sys.argv[1]),\
songTitle=re.sub(" ", "-", sys.argv[2]))

	resp = requests.get(url, allow_redirects=True)

	if str(resp.status_code) != "200":
		sys.stderr.write("Could not find song \"{0}\" by \"{1}\".\n".format(sys.argv[2],\
sys.argv[2]))
		sys.stderr.write("Please check that you spelled the artist and song names correctly.\n")
		sys.stderr.write("Also, please check that you did not switch the name of the artist\n")
		sys.stderr.write("with the name of the song by accident. Then, please try again.\n")
		sys.exit(-1)

	html = bs4.BeautifulSoup(resp.text, "html.parser")

	#Find the path to espeak/say if it was not provided
	if len(sys.argv) <= 3:
		if os.path.isfile("/usr/bin/say") and os.access("/usr/bin/say", os.X_OK):
			espeakPath = "/usr/bin/say"
		elif os.path.isfile("/usr/bin/espeak") and os.access("/usr/bin/espeak", os.X_OK):
			espeakPath = "/usr/bin/espeak"
		else:
			sys.stderr.write("Could not find espeak or say. Please make sure the path\n")
			sys.stderr.write("you entered is valid and then try again.\n")
			sys.exit(-1)
	else:
		espeakPath = "{0}".format(sys.argv[3])
		if not os.path.isfile(espeakPath) or not os.access(espeakPath, os.X_OK):
			sys.stderr.write("Could not find espeak or say. Please make sure the path\n")
			sys.stderr.write("you entered is valid and then try again.\n")
			sys.exit(-1)

	for tag in html.find_all('p'):
		if "class" in tag.attrs and tag.attrs["class"][0] == "verse":
			for content in tag.contents:
				#Remove extra <br>, </br>, and <br /> tags.
				text = re.sub("<[^>]*>", "", str(content))

				#Let espeak do its work
				retVal = os.system("echo \"{0}\" | {1}".format(text, espeakPath))

				#Did espeak/say work?
				if retVal != 0:
					sys.stderr.write("Could not play song \"{0}\" by \"{1}\".\n".format(\
sys.argv[2], sys.argv[1]))
					sys.stderr.write("Please make sure your path to espeak or say is correct.\n")
					sys.exit(-1)

if __name__ == "__main__":
    main()
