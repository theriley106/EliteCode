import requests
import bs4
import json
import random



def grabSite(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(url, headers=headers)



if __name__ == '__main__':
	count = 0
	a = []
	for val in json.load(open("problems.json"))["stat_status_pairs"]:
		if val['status'] == "ac":
			a.append(val['stat']["question__title_slug"])
			count += 1
	print("https://leetcode.com/problems/" + random.choice(a))
	#res = grabSite(url)
	#page = bs4.BeautifulSoup(res.text, 'lxml')


