#!/bin/sh
./mkvideolist.sh
if [[ $? -ne 0 ]] ; then
    exit 1
fi

./mkdescs.sh
if [[ $? -ne 0 ]] ; then
    exit 1
fi

python genindex.py
if [[ $? -ne 0 ]] ; then
    exit 1
fi

scp index.html root@suborbital.io:/var/www/suborbital/chimpire.html
