import json
import os
import requests

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
	with open('problems.json', 'w') as f:
	    json.dump(x, f, indent=4)

if __name__ == '__main__':
	if os.path.exists("problems.json") == False:
		gen_problems()
