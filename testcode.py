#!/usr/bin/env python
#coding: utf-8

import unittest
import cPickle as pickle
import os
import commands
import json

class Test_TaskChecker(unittest.TestCase):
	def setUp(self):
		pass

	def test_create_function(self):
		os.system("python task.py create 2012/03/20 確定申告")
		os.system("python task.py create 2012/03/30 テストテスト")
		os.system("python task.py create 2013/01/01 元旦")
		os.system("python task.py create 2012/04/15 テスト")

#	def test_show_tasklist(self):
#		print "="*50
#		os.system("python task.py --show")
#
#	def test_show_tasklist_on_date(self):
#		print "="*50
#		os.system("python task.py --show 2012/04")
#		print "="*50
#		os.system("python task.py --show 2012/03/20")
#		print "="*50
		
	def test_delete_task(self):
		print "-"*100
		os.system("python task.py delete 1")

	

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_TaskChecker)
	unittest.TextTestRunner().run(suite)
