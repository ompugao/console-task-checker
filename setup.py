#!/usr/bin/env python
#coding: utf-8

from distutils.core import setup
from lib            import app_version
import os

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
	packages = ['lib'],
	scripts = ['bin/task']
)
