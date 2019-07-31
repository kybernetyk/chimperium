#!/bin/sh
./mkvideolist.sh
if [[ $? -ne 0 ]] ; then
    exit 1
fi

./mkdescs.sh
if [[ $? -ne 0 ]] ; then
    exit 1
fi

./genhtml.py
if [[ $? -ne 0 ]] ; then
    exit 1
fi

