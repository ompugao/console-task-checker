#!/usr/bin/env python
#coding: utf-8

import sys
import os
import datetime
import termcolor

import lib
from lib import kill

def create_task(arguments):
	if len(arguments) <= 1:
		print "argument is too short."
		lib.help_msg()
		kill(1)

	limit_date = lib.format_convert(arguments[0])
	task_contents = arguments[1]
	task_container = lib.get_task_container()
	sha1_hash = lib.create_sha1_hash(task_contents, datetime.datetime.now())
	task_container.add_task(sha1_hash, limit_date, task_contents)
	lib.serialize_object(task_container)
	print "Added the following task:"
	print "%s : %s" % (arguments[0], arguments[1])

def show_tasks_list(arguments):
	task_container = lib.get_task_container()
	if task_container.length == 0:
		print "There is no TASKS!"
		kill(1)

	if len(arguments) == 0:
		deadlines, sorted_tasks = lib.get_sorted_items(task_container)
	else:
		deadlines, sorted_tasks = lib.get_sorted_items(task_container, arguments[0])

	most_longest_width = sorted([len(str(i)) for i in deadlines])[-1]
	for deadline in deadlines:
		for task_info in sorted_tasks[deadline]:
			strformat_date, contents, colorcode = task_info
			if deadline == 0:
				deadline = " "*(most_longest_width-int(len(str(deadline))))+str(deadline)
				print termcolor.colored(
						"%s : %s : %s" % (
							strformat_date, "今日が期限です!"+(" "*most_longest_width), contents
							
						), colorcode
				)
			elif deadline < 0:
				deadline = " "*(most_longest_width-int(len(str(deadline))))+str(deadline)
				print termcolor.colored(
						"%s : 期限を超えています! : %s" % (
							strformat_date, contents
						), colorcode
				)
			else:
				deadline = " "*(most_longest_width-int(len(str(deadline))))+str(deadline)
				print termcolor.colored(
						"%s : 期限まであと %s 日: %s" % (
							strformat_date, deadline, contents
						), colorcode
				)
		
def delete_task(arguments):
	if len(arguments) == 0:
		# show task number
		task_container = lib.get_task_container()
		if task_container.length == 0:
			print "There is NO TASKS!!"
			kill()

		task_number = 0
		for hash, (limit_date, task_contents) in task_container.iteritems():
			print "[%s] %s : %s " % (
				termcolor.colored(task_number, "yellow"),
				lib.get_string_date(limit_date, 3),
				task_contents,
			)

			task_number += 1

	elif len(arguments) == 1:
		try:
			task_number = int(arguments[0])
		except ValueError:
			print "'%s' is not integer." % arguments[0]

		task_container = lib.get_task_container()

		if task_number > task_container.length-1:
			print "%s or more tasks do not have." % task_number
			kill(1)
		
		delete = task_container.delete_task(task_container.keys()[task_number])
		lib.serialize_object(task_container)
		
		print "Deleted Task :"
		print "%s : %s" % (delete[0].strftime("%Y/%m/%d"), delete[1])




if __name__ == "__main__":
	try:
		option = sys.argv[1]
		args = sys.argv[2:]

	except:
		lib.help_msg()
		kill(1)

	if option == "create":
		create_task(args)
		
	elif option == "list":
		show_tasks_list(args)
	
	elif option == "delete":
		delete_task(args)

	else:
		lib.help_msg()