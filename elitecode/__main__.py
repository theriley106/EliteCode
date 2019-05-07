import elitecode
import argparse

DEFAULTS = {'medium': 30, 'hard': 10, 'easy': 60}



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Description of your program')
	parser.add_argument('--easy', help='Signifies the ratio of questions classified as "Easy" in the problem pool', required=False)
	parser.add_argument('--medium', help='Signifies the ratio of questions classified as "Medium" in the problem pool', required=False)
	parser.add_argument('--hard', help='Signifies the ratio of questions classified as "Hard" in the problem pool', required=False)
	args = {k: v for k, v in vars(parser.parse_args()).iteritems() if v is not None}
	print args
	if len(args) > 0:
		if len(args) != 3:
			raise Exception("Please specify ratios for all 3 types of Leetcode question (--easy, --medium, --hard)")
		for key, val in args.iteritems():
			try:
				DEFAULTS[key] = float(val)
			except:
				raise Exception("Numerical values required for command line arguments")
	easy = DEFAULTS['easy']
	medium = DEFAULTS['medium']
	hard = DEFAULTS['hard']
	# Specifies default args
	print("Shuffling Leetcode questions with ratio: E: {} M: {} H: {}".format(easy, medium, hard))