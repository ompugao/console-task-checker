#!/usr/bin/env python
#coding: utf-8

import os
import sys
import cPickle as pickle
import datetime
import hashlib
import termcolor

container_file = os.environ["HOME"]+"/.task_container"
kill = sys.exit
app_version = "0.2.5"

class TaskContainer(dict):
	def __init__(self):
		self.length = len(self.keys())
		pass
	
	def add_task(self, sha1_hash, datetime_object, task_contents):
		self[sha1_hash] = (datetime_object, task_contents)
		self.length = len(self.keys())

	def delete_task(self, sha1_hash):
		delete = self.pop(sha1_hash)
		self.length = len(self.keys())
		return delete

	def update_task(self, sha1_hash, datetime_object, task_contents):
		self.delete_task(sha1_hash)
		self.add_task(sha1_hash, datetime_object, task_contents)

	
	def tasks(self):
		return self.__dict__

def help_msg():
	print "ConsoleTaskChecker Version %s" % app_version
	print "$ task [option] [Args]"
	print "  help"
	print "     Show this help msg."
	print "  version"
	print "     Show this application's version"
	print "  create [date] [task contents]"
	print "      Add new task. Please input date format to second argument, and task contents to thirt argument."
	print "      Date Format : YYYY/MM/DD"
	print "  list [[date]]"
	print "      Show task list. If you input date format to second argument, you can show task list for that date."
	print "      in addition, if you input month format, you can show task list for that month."
	print "      Date Format : YYYY/MM/DD or YYYY/MM"
	print "  update [[task number], [update dateformat], [updated task contents]]"
	print "      Update Task."
	print "      If you run update option wituout argument, This application provide task number to you."
	print "      And, if you decided on the task that you want to update,  "
	print "      please input task number at third argument, updated task date format at fourth argument"
	print "      and updated task contents at fifth argument."
	print "  delete [[task number]]"
	print "      Delete Task."
	print "      If you run delete option without argument, This application provide task number to you."
	print "      And you input delete option with task number to second argument. Then, this application delete task."  

def show_version():
	print "ConsoleTaskChecker Version %s" % app_version 
	
def raise_not_along_format_error(dateformat):
	print "'%s' is not along the format." % dateformat
	print "Date Format : YYYY/MM/DD"
	kill(1)

def check_task_length(task_container):
	if task_container.length == 0:
		print "There is NO TASKS!!"
		kill()

def check_format(dateformat):
	if dateformat.endswith("/"):
		dateformat = dateformat[:-1]
	
	clip = dateformat.split("/")
	for i in clip:
		result = 0
		try:
			j = int(i)
			result = True
		except:
			result = False
	if result == False:
		print "'%s' does not contain an integer" % dateformat
		kill(1)

	if len(clip) == 1:
		raise_not_along_format_error(dateformat)
	else:
		return dateformat

def format_convert(dateformat):
	if dateformat == "today":
		dateformat = datetime.datetime.today().strftime("%Y/%m/%d")
	else:
		dateformat = check_format(dateformat)

	clip = dateformat.split("/")
	try:
		year, month, day = [int(i) for i in clip]
	except ValueError:
		print "'%s' does not contain an integer" % dateformat
		kill(1)

	try:
		target_date = datetime.datetime(year, month, day)
	except ValueError:
		print "day is out of range for year or month or day"
		kill(1)
	return target_date

def create_sha1_hash(task_contents, datetime_object):
	return hashlib.sha1(task_contents+datetime_object.strftime("%Y/%m/%d+%H:%M:%S")).hexdigest()


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

def get_string_date(dateobject, sep):
	if sep == 2:
		return dateobject.strftime("%Y/%m")
	elif sep == 3:
		return dateobject.strftime("%Y/%m/%d")


def get_task_iter_on_date(dateformat, task_container):
	clip = dateformat.split("/")

	# if dateformat is 'YYYY/M' -> 'YYYY/0M'
	for index in range(len(clip)):
		if len(clip[index]) == 1:
			clip[index] = "0"+clip[index]

	dateformat = "/".join(clip)
			
	# to check whether the correct format and determine separater num
	sep = 0
	if len(clip) == 2:
		sep = 2
	elif len(clip) == 3:
		sep = 3
	else:
		raise_not_along_format_error(dateformat)

	result = {}
	dont_exist_task = []
	for hash, (limit_date, task_contents) in task_container.iteritems():
		string_date = get_string_date(limit_date, sep)
		if string_date == dateformat:
			result[hash] = (limit_date, task_contents)
			dont_exist_task.append(True)
		
		else:
			dont_exist_task.append(False)
	
	if True not in dont_exist_task:
		print "There is no TASKS on %s !" % dateformat
		kill(1)

	return result.iteritems()

def get_sorted_items(task_container, dateformat=None):
	if dateformat:
		dateformat = check_format(dateformat)
		task_container_iter = get_task_iter_on_date(dateformat, task_container)
	else:
		task_container_iter = task_container.iteritems()

	current_date = get_current_datetime_object()
	task_contents_list = {}

	# original data : {hash: tuple(datetime obj, task contents)}
	# tasklist data struct : {"1" : [(strformat, taskcontents, colorcode)]}
	# return [sorted deadlines], [sorted task items]

	for hash, (limit_date, task_contents) in task_container_iter:
		days_until_the_deadline = get_number_of_days_until_the_deadline(limit_date, current_date)
		strformat = get_string_date(limit_date, 3)

		# set color code
		colorcode = "white"
		if days_until_the_deadline == 0:
			colorcode = "red"
		elif days_until_the_deadline < 0:
			colorcode = "yellow"
		elif days_until_the_deadline <= 3:
			colorcode = "magenta"
		elif days_until_the_deadline <= 7:
			colorcode = "cyan"
		elif days_until_the_deadline <= 31:
			colorcode = "blue"
		
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

	return sorted(task_contents_list.keys()), task_contents_list

def show_tasks_number(task_container):
	task_number = 0
	for hash, (limit_date, task_contents) in task_container.iteritems():
		print "[%s] %s : %s " % (
			termcolor.colored(task_number, "yellow"),
			get_string_date(limit_date, 3),
			task_contents,
		)

		task_number += 1

def delete_all_tasks():
	task_container = TaskContainer()
	serialize_object(task_container)
