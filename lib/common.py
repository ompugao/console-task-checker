#!/usr/bin/env python
#coding: utf-8

import os
import sys
import cPickle as pickle
import datetime

container_file = os.environ["HOME"]+"/.task_conteiner"
kill = sys.exit

class TaskContainer(dict):
	def __init__(self):
		self.length = len(self.keys())
		pass
	
	def add_task(self, datetime_object, task_content):
		self[datetime_object] = task_content
		self.length = len(self.keys())
	
	def tasks(self):
		return self.__dict__

def help_msg():
	print "ConsoleTaskChecker Version%s" % app_version
	print "$ taskcheck.py [option] [Args]"
	print "  --add [date] [task contents]"
	print "      Add new task. Please input date format to second argument, and task contents to thirt argument."
	print "      Date Format : YYYY/MM/DD"
	print "  --show [[date]]"
	print "      Show task list. If you input date format to second argument, you can show task list for that date."
	print "      in addition, if you input month format, you can show task list for that month."
	print "      Date Format : YYYY/MM/DD or YYYY/MM"

def check_file_existence():
	if os.access(container_file, os.F_OK):
		return True
	else:
		return False

def get_task_container():
	if check_file_existence():
		fp = open(container_file, "r")
		task_container = pickle.load(fp)
	else:
		task_container = TaskContainer()
		
	return task_container

def serialize_object(object):
	fp = open(container_file, "w")
	pickle.dump(object, fp)

def get_current_datetime_object():
	return datetime.datetime.now()

def get_number_of_days_until_the_deadline(limit_date, current_date):
	if isinstance(limit_date, datetime.datetime) == False and isinstance(current_date, datetime.datetime):
		raise ValueError("limit date or currennt date is not datetime object")
	
	diff = limit_date - current_date
	return diff.days+1

def get_sorted_items(task_container):
	current_date = get_current_datetime_object()
	# tasklist data struct : {"1" : [(strformat, taskcontents, colorcode)]}
	task_contents_list = {}
	for limit_date, task_contents in task_container.iteritems():
		days_until_the_deadline = get_number_of_days_until_the_deadline(limit_date, current_date)
		strformat = limit_date.strftime("%Y/%m/%d")

		# set color code
		colorcode = "white"
		if days_until_the_deadline <= 0:
			colorcode = "red"
		elif days_until_the_deadline <= 3:
			colorcode = "magenta"
		elif days_until_the_deadline <= 7:
			colorcode = "cyan"
		elif days_until_the_deadline <= 31:
			colorcode = "green"
		
		if days_until_the_deadline in task_contents_list.keys():
			task_contents_list[days_until_the_deadline].append((
				strformat,
				task_contents,
				colorcode
			))

		else:
			task_contents_list[days_until_the_deadline] = []
			task_contents_list[days_until_the_deadline].append((
				strformat,
				task_contents,
				colorcode
			))

	return task_contents_list
