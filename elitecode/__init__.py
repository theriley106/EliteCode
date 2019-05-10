import argparse
import sys
import json
import os
import requests
import random

DEFAULTS = {'medium': 30, 'hard': 10, 'easy': 60}

try:
    input = raw_input
except NameError:
    pass

def gen_problems():
	if os.getuid() != 0:
		print("Please rerun script with Sudo/Administrator access")
		exit()
	res = requests.session()
	headers = {'Host':'leetcode.com', 'Origin':'https://leetcode.com', 'Referer':'https://leetcode.com/accounts/login/', 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'}
	res.headers.update(headers)

	response = res.get('https://leetcode.com/accounts/login')

	csrf_token = res.cookies['csrftoken']

	username = input("Username: ")
	password = input("Password: ")
	loginurl = 'https://leetcode.com/accounts/login/'       
	loginparams = {'csrfmiddlewaretoken':csrf_token,'login':username, 'password':password}

	req = res.post(loginurl, data=loginparams, headers=headers)

	x = res.get("https://leetcode.com/api/problems/all/").json()
	with open(os.path.dirname(os.path.abspath(__file__)) + "/problems.json", "w") as f:
	    json.dump(x, f, indent=4)
	print("\nProblems Generated.  Elitecode has been successfully configured")
	exit()

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
	loop = 0
	for i in range(countVal):
		x = random.choice(a)
		while x in problemList:
			x = random.choice(a)
			loop += 1
			if loop > 10000:
				raise Exception("No problems exist")
		problemList.append(x)
	return ["https://leetcode.com/problems/" + question for question in problemList]

def main(args):
	multiply = False
	count = 0
	for k in DEFAULTS.keys():
		if k not in args:
			count += 1
	if count != 0 and count != 3:
		raise Exception("Please specify ratios for all 3 types of Leetcode question (--easy, --medium, --hard)")
	#print args
	if len(args) > 2:
		for key, val in args.items():
			try:
				DEFAULTS[key] = float(val)
				if DEFAULTS[key] < 10:
					multiply = True
			except:
				raise Exception("Numerical values required for command line arguments")
	if multiply == True:
		for k, v in DEFAULTS.items():
			DEFAULTS[k] = v * 10
	easy = DEFAULTS['easy']
	medium = DEFAULTS['medium']
	hard = DEFAULTS['hard']
	# Specifies default args
	#print("Shuffling Leetcode questions with ratio: E: {} M: {} H: {}".format(easy, medium, hard))
	if check_problems_missing():
		print("Problems file missing - Please login with Leetcode account to generate personalized problems file:")
		gen_problems()
	print("\n_____NEW QUESTIONS_____\n")
	for i, val in enumerate(gen_new(DEFAULTS, int(args['new']))):
		print("{}. ".format(i+1) + val + "\n")
	print("\n_____OLD QUESTIONS_____\n")
	for i, val in enumerate(gen_old(int(args['old']))):
		print("{}. ".format(i+1) + val + "\n")

if __name__ == '__main__':
	if 'regenerate' in str(sys.argv).lower():
		print("Regenerating problem set\n")
		gen_problems()
	parser = argparse.ArgumentParser(description='Description of your program')
	parser.add_argument('--new', help='Signifies the number of new questions returned', required=False, default=2)
	parser.add_argument('--old', help='Signifies the number of old questions returned', required=False, default=1)
	parser.add_argument('--easy', help='Signifies the ratio of questions classified as "Easy" in the problem pool', required=False)
	parser.add_argument('--medium', help='Signifies the ratio of questions classified as "Medium" in the problem pool', required=False)
	parser.add_argument('--hard', help='Signifies the ratio of questions classified as "Hard" in the problem pool', required=False)
	args = {k: v for k, v in vars(parser.parse_args()).items() if v is not None}
	main(args)
