#!/usr/bin/env python
#coding: utf-8

import sys
import os
import datetime
import termcolor

from lib import common
from lib.common import kill

common.app_version = " 0.2"

def format_convert(dateformat):
	if dateformat.endswith("/"):
		dateformat = dateformat[:-1]
	
	clip = dateformat.split("/")
	if len(clip) == 1:
		# not along the format
		print "'%s' is not along the format." % dateformat
		print "Date Format : YYYY/MM/DD"
		kill(1)
	
	year, month, day = [int(i) for i in clip]
	target_date = datetime.datetime(year, month, day)
	return target_date

def add_new_task(arguments):
	if len(arguments) <= 1:
		print "argument is too short."
		common.help_msg()
		kill(1)

	limit_date = format_convert(arguments[0])
	task_contents = arguments[1]
	task_container = common.get_task_container()
	task_container.add_task(request_date, task_contents)
	common.serialize_object(task_container)
	print "Added the following task:"
	print "%s : %s" % (arguments[0], arguments[1])

def show_tasks_list(arguments):
	task_container = common.get_task_container()
	if task_container.length == 0:
		print "There is no TASKS!"
		kill(1)

	current_date = common.get_current_datetime_object()
	if len(arguments[0]) == 0:
		# Date is not specified
		for limit_date, task_contents in task_container.iteritems():
			days_until_the_deadline = common.get_number_of_days_until_the_deadline(limit_date, current_date)
		pass

if __name__ == "__main__":
	try:
		option = sys.argv[1]
		args = sys.argv[2:]

	except:
		common.help_msg()
		kill(1)

	if option == "--add":
		add_new_task(args)
		
	elif option == "--show":
		show_tasks_list(args)
