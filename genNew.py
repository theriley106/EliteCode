import requests
import bs4
import json
import random




if __name__ == '__main__':
	a = []
	count = 0
	for val in json.load(open("problems.json"))["stat_status_pairs"]:
		if val['status'] != "ac" and val["paid_only"] == False:
			if val["difficulty"]['level'] == 3:
				count += 1
				if count < 10:
					a.append(val['stat']["question__title_slug"])
			else:
				a.append(val['stat']["question__title_slug"])
	print a
	print("https://leetcode.com/problems/" + random.choice(a))
	#res = grabSite(url)
	#page = bs4.BeautifulSoup(res.text, 'lxml')


