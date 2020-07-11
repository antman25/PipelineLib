#!/usr/bin/python3

import ast
import traceback
import sys
import glob
import os

def test_file(path):
	valid = True
	tracebackoutput=''
	with open(path) as f:
		source = f.read()
	try:
		ast.parse(source)
	except SyntaxError:
		valid = False
		traceoutput = traceback.print_exc()
	return valid


if __name__ == '__main__':
	if len(sys.argv) == 1:
		print("Provide a list of file paths to check")
		sys.exit(0)

	results = []
	exit_code = 0

	for file_path_idx in range(1,len(sys.argv)): 
		current_filepath = sys.argv[file_path_idx]
		if os.path.isfile(current_filepath):
			filename, file_extension = os.path.splitext(current_filepath)
			if file_extension == '.py':
				print ("################  Checking path %s  ############" % (current_filepath))
				valid = test_file(current_filepath)
				results.append((current_filepath,valid))
			else:
				print ("Skipping %s - not a .py extension" % current_filepath)

	print ("############### SUMMARY ################")
	for path, valid in results:
		print ("%s = %s" % (path,valid))
		if (valid == False):
			exit_code = 1


	if exit_code == 1:
		sys.exit(1)
	sys.exit(0)
