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
	diff = limit_date - current_date
	#monthes = diff/31
	#years = 0
	#if monthes >= 12:
	#	years = monthes/
	#days = diff - (diff*monthes)
	return diff.days()

