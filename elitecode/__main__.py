import elitecode
import argparse

DEFAULTS = {'medium': 30, 'hard': 10, 'easy': 60}

def make_args_100(args):
	countVal = sum(args.values())
	if countVal != 100:
	for k, v in args.iteritems():



if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Description of your program')
	parser.add_argument('--easy', help='Signifies the percentage of questions classified as "Easy" in the problem pool', required=False, default=DEFAULTS['easy'])
	parser.add_argument('--medium', help='Signifies the percentage of questions classified as "Medium" in the problem pool', required=False, default=DEFAULTS['medium'])
	parser.add_argument('--hard', help='Signifies the percentage of questions classified as "Hard" in the problem pool', required=False, default=DEFAULTS['hard'])
	args = vars(parser.parse_args())
	for key, val in args.iteritems():
		try:
			float(val)
		except:
			raise Exception("Numerical values required for command line arguments")
	print args