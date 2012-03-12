#!/usr/bin/env python
#coding: utf-8

import sys
import os
import datetime
import termcolor

__version__ = "0.1"

def help_msg():
	print "ConsoleTaskChecker Version%s" % __version__
	print "$ taskcheck.py [option] [Args]"
	print "  --add [date] [task contents]"
	print "      Add new task. Please input date format to second argument, and task contents to thirt argument."
	print "      Date Format : YYYY/MM/DD"
	print "  --show [[date]]"
	print "      Show task list. If you input date format to second argument, you can show task list for that date."
	print "      in addition, if you input month format, you can show task list for that month."
	print "      Date Format : YYYY/MM/DD or YYYY/MM"

def format_convert(dateformat):
	if dateformat.endswith("/"):
		dateformat = dateformat[:-1]
	
	clip = dateformat.split("/")
	if len(clip) == 1:
		# not along the format
		print "'%s' is not along the format." % dateformat
		print "Date Format : YYYY/MM/DD"
		sys.exit(1)
	
	year, month, day = [int(i) for i in clip]
	target_date = datetime.datetime(year, month, day)
	return target_date

def add_new_task(arguments):
	if len(arguments) <= 1:
		print "argument is too short."
		help_msg()
		sys.exit(1)

	request_date = format_convert(args[0])
	task_contents = args[1]
	




if __name__ == "__main__":
	try:
		option = sys.argv[1]
		args = sys.argv[2:]

	except:
		help_msg()
		sys.exit(1)

	if option == "--add":
		add_new_task(args)
		
