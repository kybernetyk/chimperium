import json

class Video:
	url = ""
	title = ""
	guest = ""
	guest_who = ""
	ep_num = 0
	def __repr__(self):
		return repr((self.ep_num, self.gues))

def is_video_valid(video):
	if "from the Joe Rogan Experience" in video.title:
		return False
	if "(Joe Rogan Experience" in video.title:
		return False
	if "From Joe Rogan Experience" in video.title:
		return False
	if "form Joe Rogan Experience" in video.title:
		return False
	if "from Joe Rogan Experience" in video.title:
		return False
	if "Joe Rogan Experience" not in video.title:
		return False
	if "- #" in video.title:
		return False
	if "#" not in video.title:
		return False
	if "Best of the Week" in video.title:
		return False
	if "JRE MMA Show" in video.title:
		return False
	if "Public Service Announcement" in video.title:
		return False
	return True

def mk_guest_from_title(title):
	title = title.replace(" -- ", " - ").strip()
	guest = title.split(" - ")
	if len(guest) > 1:
		return guest[1].strip()
	return ""

def mk_epnum_from_title(title):
	epnum = title.split("#")
	if len(epnum) > 1:
		x = epnum[1].split("-")
		if len(x) > 1:
			return int(x[0])
		else:
			x = epnum[1].split(" ")
			if len(x) > 1:
				return int(x[0])
	return 0

def mk_desc(vid_id):
	fn = "desc/" + vid_id + ".txt"
	with open(fn) as f:
		desc = f.read()
		desc = desc.replace('\\"', '$HANS$' )
		desc = desc.replace('"', '')
		desc = desc.replace('$HANS$', '"')
		return desc
	return ""

def mk_video_from_json_string(json_string):
	j = json.loads(json_string)
	vid = Video()
	vid.url = j['url']
	vid.title = j['title']
	if is_video_valid(vid):
		vid.guest = mk_guest_from_title(vid.title).strip()
		vid.ep_num = mk_epnum_from_title(vid.title)
		vid.guest_who = mk_desc(vid.url)
	return vid

def load_videos(filename):
	ret = []
	with open(filename) as json_file:
		for cnt, line in enumerate(json_file):
			vid = mk_video_from_json_string(line)
			if is_video_valid(vid) and vid.ep_num > 0 and len(vid.guest) > 0:
				ret.append(vid)
	return ret

def mk_html_lineitem(vid):
	html = "<tr>"
	# html += "<td><a href='https://youtu.be/" + vid.url + "'>[Watch on YouTube]</td>")
	html += ("<td style='width: 5%;'>#" + str(vid.ep_num) + "</td>")
	html += ("<td style='width: 5%;'>" + vid.guest + "</td>")
	html += ("<td>" + vid.guest_who + "</td>")
	html += "<td style='width: 5%;'>"
	# html += '<iframe width="560" height="315" src="https://www.youtube.com/embed/' + vid.url +' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
	html += ("<a target=_blank href='https://youtu.be/" + vid.url + "'>[Watch on YouTube]</td>")
	html += "</td>"
	html += "</tr>"
	return html

def make_html(vids):
	html = "<html><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width'><title>chimpire</title></head>"
	html += '''<style>
				body {background-color: #f3ffbd; color: #247ba0; font-family: monospace; }
				a {color: #ff1654;}
				a:visited {color: #b2dbbf; }
				h1   {color: #ff1654; font-size: 300%;}
				table {border-collapse: collapse; font-size:125%; width: auto; min-width: 25; max-width: 70%; margin-left: auto; margin-right: auto;
				 }
				td {border: 1px solid #ff1654;
					padding: 15px;
					max-width: 600px;
				}
				</style>'''
	html += "<body><center><h1>☆ ★ ☆ C H I M P I R E ☆ ★ ☆</h1><br><img src=joe.png><br><h1>🍄🍄🍄</h1></center><br><table cols=4>"
	for v in vids:
		html += mk_html_lineitem(v)
	html += "</table></div></body></html>"
	return html


videos = load_videos("videos.json")
vids = sorted(videos, key=lambda x: x.ep_num, reverse=True)
html = make_html(vids)
with open("index.html", "w") as index:
	index.write(html)
print("done")

# for v in vids:
# 	print("https://youtu.be/"+ v.url + " : " + v.guest + " => " + v.guest_who)