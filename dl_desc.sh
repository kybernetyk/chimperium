#!/bin/sh
destfn="desc/$1.txt"
if [ -f "$destfn" ]; then
	echo "$destfn exists!"
	exit
fi
youtube-dl --default-search "ytsearch" --skip-download -j "https://www.youtube.com/watch?v=$1" |jq .description > $destfn
