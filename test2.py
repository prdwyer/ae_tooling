import json
import requests
import logging
import re
import argparse
import os
import zipfile
import sys

parser = argparse.ArgumentParser(description='scythe json runner')
parser.add_argument('--json', help='json file to run', dest='json_file')
parser.add_argument('--interactive', help='run in interactive mode', dest='interactive')
parser.add_argument('--getscythefiles', help='retrieve sythce rules', dest='get')
args=parser.parse_args()



def build_campaign(data):
	file = 'fiel'
	rjson = r.json()

	threatdict = data['threat']

	print('running teh following caompaign:"')
	print(threadict['display_name')
	print(threadict['description')

	executable = threatdict['script']

	for key in executable.keys():
		step = executable[key]
		if 'request' in step:
		print(step['request'])





if args.json_file:
	f = open(args.json_file)
	data = json.load(f)
	build_campaign(data)
	logging.info("wordlist set run")
	sys.exit()

if args.getscythefiles:
	#git clone the scythe repo
	sys.exit()




def main():
	
	#logging.info("STARTING MAIN")
	#output=list()
	#output.append(do_directory(args.directory))

	#get_inputs()
	#old_town()

if __name__== "__main__":
	main()

