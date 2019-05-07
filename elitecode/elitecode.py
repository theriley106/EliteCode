import json
import os
import requests
import random

print os.path.dirname(os.path.abspath(__file__))

def gen_problems():
	res = requests.session()
	headers = {'Host':'leetcode.com', 'Origin':'https://leetcode.com', 'Referer':'https://leetcode.com/accounts/login/', 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'}
	res.headers.update(headers)

	response = res.get('https://leetcode.com/accounts/login')

	csrf_token = res.cookies['csrftoken']

	username = raw_input("Username: ")
	password = raw_input("Password: ")
	loginurl = 'https://leetcode.com/accounts/login/'       
	loginparams = {'csrfmiddlewaretoken':csrf_token,'login':username, 'password':password}

	req = res.post(loginurl, data=loginparams, headers=headers)

	x = res.get("https://leetcode.com/api/problems/all/").json()
	with open(os.path.dirname(os.path.abspath(__file__)) + "/problems.json", "w") as f:
	    json.dump(x, f, indent=4)

def check_problems_missing():
	return os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/problems.json") == False

def gen_old(countVal=1):
	count = 0
	a = []
	for val in json.load(open(os.path.dirname(os.path.abspath(__file__)) + "/problems.json"))["stat_status_pairs"]:
		if val['status'] == "ac":
			a.append(val['stat']["question__title_slug"])
			count += 1
	loop = 0
	problemList = []
	for i in range(countVal):
		x = random.choice(a)
		while x in problemList:
			x = random.choice(a)
			loop += 1
			if loop > 5000:
				raise Exception("No problems exist")
		problemList.append(x)
	return ["https://leetcode.com/problems/" + question for question in problemList]

def gen_new(tempArgs, countVal):
	a = []
	eCount = 0
	mCount = 0
	hCount = 0
	for val in json.load(open(os.path.dirname(os.path.abspath(__file__)) + "/problems.json"))["stat_status_pairs"]:
		if val['status'] != "ac" and val["paid_only"] == False:
			a.append(val['stat']["question__title_slug"])
	totalQuestions = len(a)
	args = {'easy': tempArgs['easy'], 'medium': tempArgs['medium'], 'hard': tempArgs['hard']}
	totalCount = float(sum(args.values()))
	if totalCount == 0:
		raise Exception("Command line argument sum must be greater than 0")
	easyCount = int((args['easy'] / totalCount) * totalQuestions) / 10
	mediumCount = int((args['medium'] / totalCount) * totalQuestions) / 10
	hardCount = int((args['hard'] / totalCount) * totalQuestions) / 10
	#print("Generating Easy: {} Medium: {} Hard: {}".format(easyCount, mediumCount, hardCount))
	toSearch = json.load(open(os.path.dirname(os.path.abspath(__file__)) + "/problems.json"))["stat_status_pairs"]
	random.shuffle(toSearch)
	a = []
	for val in toSearch:
		#print val["difficulty"]['level']
		if val['status'] != "ac" and val["paid_only"] == False:
			if val["difficulty"]['level'] == 3:
					if hCount < hardCount:
						hCount += 1
						a.append(val['stat']["question__title_slug"])
			elif val["difficulty"]['level'] == 2:
				if mCount < mediumCount:
					mCount += 1
					a.append(val['stat']["question__title_slug"])
			else:
				if eCount < easyCount:
					eCount += 1
					a.append(val['stat']["question__title_slug"])
	problemList = []
	#print("E: {} M: {} H: {}".format(eCount, mCount, hCount))
	for i in range(countVal):
		x = random.choice(a)
		while x in problemList:
			x = random.choice(a)
			loop += 1
			if loop > 10000:
				raise Exception("No problems exist")
		problemList.append(x)
	return ["https://leetcode.com/problems/" + question for question in problemList]

if __name__ == '__main__':
	print gen_new({'medium': 30, 'hard': 10, 'easy': 60}, 10)
