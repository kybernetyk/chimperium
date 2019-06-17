#!/bin/sh
cat videos.json |jq -r .url > video_urls.txt
parallel --eta -a video_urls.txt ./dl_desc.sh
