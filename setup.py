#!/usr/bin/env python
#coding: utf-8

from distutils.core import setup
import os

app_version = "0.2.1"

if os.path.isdir("bin") == False:
	os.mkdir("bin")

open("./bin/task", "w").write(open("task.py").read())
os.system("chmod +x ./bin/task")


DISTUTILS_DEBUG = True

setup(
	name = "taskChecker-on-Console",
	author = "alice",
	author_email = "takemehighermore@gmail.com",
	version = app_version,
	license = "MIT License",
	url = "",
	download_url = "",
	description = "this application support management your task on console.",
	py_modules = ['task', 'lib.functions', 'setup'],
	packages = ['lib','lib.functions'],
	scripts = ['bin/task']
)
