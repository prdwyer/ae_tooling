import json
import requests
import logging
import re
import argparse
import os
import zipfile
import sys
import requests
import shutil

banner = '''
    _       _         _____
   / \   __| |_   __ | ____|_ __ ___  _   _
  / _ \ / _` \ \ / / |  _| | '_ ` _ \| | | |
 / ___ \ (_| |\ V /  | |___| | | | | | |_| |
/_/   \_\__,_| \_/   |_____|_| |_| |_|\__,_|

'''


parser = argparse.ArgumentParser(description='scythe json runner')
parser.add_argument('--json', help='json file to run', dest='json_file')
parser.add_argument('--interactive', help='run in interactive mode', dest='interactive')
parser.add_argument('--getscythefiles', help='retrieve sythce rules', dest='getscythefiles')
args=parser.parse_args()



def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename


def print_campaign(commands):
    i = 0
    for command in commands:
        print("(" + str(i) +") " + command)
        i=i+1

def build_campaign(data):
    threatdict = data['threat']

    print('running the following campaign:"')
    print(threatdict['display_name'])
    print(threatdict['description'])
    executable = threatdict['script']



    commands = []
    for key in executable.keys():
        step = executable[key]
        if 'request' in step:
            commands.append(step['request'])



    commands_out = []

    x = True
    while(x == True):
        print(banner)
        print("==================================COMMAND POOL============================")
        print_campaign(commands)
        print("==================================CURRENT PALLETTE============================")
        print_campaign(commands_out)
        n = input("enter number of commands to add to pallet (x to exit): ")
        if n =="x":
            x = False
            pass
        elif int(n) <= len(commands):
            index = int(n)
            commands_out.append(commands[index])

    return commands_out

def execution(to_execute):
    print(banner)
    print("==================================Execution============================")

    for comm in to_execute:
        print("Executing...... "+ comm)
        #(comm)

def main():
    print(banner)
	
    if args.json_file:
        f = open(args.json_file)
        data = json.load(f)
        to_execute = build_campaign(data)
        execution(to_execute)

    if args.getscythefiles:
        #git clone the scythe repo
        url = "https://github.com/scythe-io/community-threats/archive/refs/heads/master.zip"

        r = requests.get(url)
        sys.exit()

	#logging.info("STARTING MAIN")
	#output=list()
	#output.append(do_directory(args.directory))

	#get_inputs()
	#old_town()

if __name__== "__main__":
	main()

