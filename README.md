LICENSING:

This software is licensed under the GNU GPLv3.

INSTALLATION:

This software was developed and tested on Ubuntu 16.04 64-bit Linux.
It should work on Mac OSX but has not been tested on Windows.

To install this software, run setup.sh. If setup.sh fails, please ensure that
you have python version 3, espeak (or "say" on Mac OSX), and these Python 3
libraries installed:

requests
beautifulsoup4

RUNNING THE SOFTWARE:

open a terminal, cd to the directory where you installed this library, and type

./getLyrics.py <your favorite artist> <your favorite song> /path/to/espeak/or/say

For example, to listen to Jimmy Eat World's "The Middle" using "say", run this command:

./getLyrics.py "Jimmy Eat World" "The Middle" /usr/bin/say

TROUBLESHOOTING AND FREQUENTLY ASKED QUESTIONS:

Question: I think I found a bug. How can I report it?

Answer: Please create an issue report on this project's Github page:
https://github.com/awzuelsdorf/SingingComputer .
I will fix it as soon as possible.

Question: The program didn't work. I got a message about "Usage" instead.
What is going on?

Answer: Please make sure you put quotes around the artists's name and the
song's name. Also, make sure you are including the path to espeak or say.
For example, if you wanted to listen to "Bad Romance" by Lady Gaga,
you WOULD NOT use this command: 

./getLyrics.py Lady Gaga Bad Romance

because there is no path to espeak/say and you didn't put quotes around both the
artist's name and the song's name

You WOULD use this command:

./getLyrics.py "Lady Gaga" "Bad Romance" /usr/bin/espeak

Question: The program says it couldn't find my song. What is going on?

Answer: Please make sure that you spelled the artist's name correctly
and the song's name correctly. If that doesn't work, then please submit
a bug report that includes the EXACT command that you used.
