LICENSING:

This software is licensed under the GNU GPLv3.

INSTALLATION:

This software is targeted toward Linux and Mac OSX platforms. It is not guaranteed to work on Windows.

To install this software, run setup.sh. If setup.sh fails, please ensure that you have python version 3, espeak,
and these Python 3 libraries installed:

requests
beautifulsoup4

RUNNING THE SOFTWARE:

open a terminal, cd to the directory where you installed this library, and type

./getLyrics.py <your favorite artist> <your favorite song>

For example, to listen to Jimmy Eat World's "The Middle", run this command:

./getLyrics.py "Jimmy Eat World" "The Middle"

TROUBLESHOOTING AND FREQUENTLY ASKED QUESTIONS:

Question: I found a bug. How can I report it?

Answer: Please create an issue report on this project's Github page:
https://github.com/awzuelsdorf/SingingComputer .
I will fix it as soon as possible.

Question: I wasn't able to listen to (a song title) by (an artist)

Answer: Please make sure you wrap the artists's name and the song's name in
quotes. For example, if you wanted to listen to "Bad Romance" by Lady Gaga,
you WOULD NOT use this command: 

./getLyrics.py Lady Gaga Bad Romance

You WOULD use this command:

./getLyrics.py "Lady Gaga" "Bad Romance"
