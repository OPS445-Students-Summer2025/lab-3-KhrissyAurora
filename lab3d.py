#!/usr/bin/env python3
'''Lab 3 Part 2 - free space'''
# Author ID: 114163223

import subprocess

def free_space():
	cmd = "df -h | grep '/$' | awk '{print $4}'"
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	output =  p.communicate()
	return output[0].decode('utf-8').strip()

if __name__ == '__main__':
	print(free_space())
