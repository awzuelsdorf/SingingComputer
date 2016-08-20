#! /bin/bash

#Copyright 2016 Andrew Zuelsdorf
#Inspired by Randall Munson's XKCD comic entitled "Universal Install Script"

if [ $# -ne 1 ]; then
	echo "Usage: $0 <package to install>"
	exit -1
fi

dnf install -y "$1" || sudo dnf install -y "$1" || yum install -y "$1" || sudo yum install -g "$1" || dpkg install "$1" || brew install "$1" || apt-get --yes install "$1" || sudo apt-get --yes install "$1" || sudo -H pip3 install "$1" ; sudo -H pip install "$1" || echo "FATAL ERROR: Was not able to install \"$1\"" 1>&2
