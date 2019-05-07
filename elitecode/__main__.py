import elitecode
import argparse
import sys

DEFAULTS = {'medium': 30, 'hard': 10, 'easy': 60}



if __name__ == '__main__':
	if 'regenerate' in str(sys.argv).lower():
		print("Regenerating problem set")
		elitecode.gen_problems()
	parser = argparse.ArgumentParser(description='Description of your program')
	parser.add_argument('--new', help='Signifies the number of new questions returned', required=False, default=2)
	parser.add_argument('--old', help='Signifies the number of old questions returned', required=False, default=1)
	parser.add_argument('--easy', help='Signifies the ratio of questions classified as "Easy" in the problem pool', required=False)
	parser.add_argument('--medium', help='Signifies the ratio of questions classified as "Medium" in the problem pool', required=False)
	parser.add_argument('--hard', help='Signifies the ratio of questions classified as "Hard" in the problem pool', required=False)
	args = {k: v for k, v in vars(parser.parse_args()).iteritems() if v is not None}
	multiply = False
	count = 0
	for k in DEFAULTS.keys():
		if k not in args:
			count += 1
	if count != 0 and count != 3:
		raise Exception("Please specify ratios for all 3 types of Leetcode question (--easy, --medium, --hard)")
	#print args
	if len(args) > 2:
		for key, val in args.iteritems():
			try:
				DEFAULTS[key] = float(val)
				if DEFAULTS[key] < 10:
					multiply = True
			except:
				raise Exception("Numerical values required for command line arguments")
	if multiply == True:
		for k, v in DEFAULTS.iteritems():
			DEFAULTS[k] = v * 10
	easy = DEFAULTS['easy']
	medium = DEFAULTS['medium']
	hard = DEFAULTS['hard']
	# Specifies default args
	print("Shuffling Leetcode questions with ratio: E: {} M: {} H: {}".format(easy, medium, hard))
	if elitecode.check_problems_missing():
		print("Problems file missing - Please login with Leetcode account to generate personalized problems file:")
		elitecode.gen_problems()
	print("\n_____NEW QUESTIONS_____\n")
	for i, val in enumerate(elitecode.gen_new(DEFAULTS, int(args['new']))):
		print("{}. ".format(i+1) + val + "\n")
	print("\n_____OLD QUESTIONS_____\n")
	for i, val in enumerate(elitecode.gen_old(int(args['old']))):
		print("{}. ".format(i+1) + val + "\n")
