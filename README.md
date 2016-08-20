INSTALLATION:

This software is targeted toward Linux and Mac OSX platforms. It is not guaranteed to work on Windows.

To install this software, run setup.sh. If setup.sh fails, please ensure that you have python version 3, espeak,
and these Python 3 libraries installed:

requests
beautifulsoup4

RUNNING THE SOFTWARE:

open a terminal, cd to the directory where you installed this library, and type

./getLyrics.py <your favorite artist> <your favorite song> | /usr/bin/espeak

PLEASE replace all spaces in the artist and song's name with dashes.
