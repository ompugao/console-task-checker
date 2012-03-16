#!/usr/bin/env python
#coding: utf-8

import unittest
import cPickle as pickle
import os

class Test_TaskChecker(unittest.TestCase):
	def setUp(self):
		pass

	def test_add_function(self):
		os.system("python taskcheck.py --add 2012/03/20 確定申告")
		os.system("python taskcheck.py --add 2012/03/30 テストテスト")
		os.system("python taskcheck.py --add 2013/01/01 元旦")
		os.system("python taskcheck.py --add 2012/03/15 テスト")

	def test_show_tasklist(self):
		print "="*50
		os.system("python taskcheck.py --show")






if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_TaskChecker)
	unittest.TextTestRunner().run(suite)
