#!/usr/bin/env python
#coding: utf-8

import unittest
import cPickle as pickle
import os

class Test_TaskChecker(unittest.TestCase):
	def setUp(self):
		pass

	def test_add_function(self):
		#os.system("rm ~/.task_conteiner")
		os.system("python taskcheck.py --add 2012/03/20 確定申告")
		fp = open(os.path.expanduser("~/.task_conteiner"))
		loads = pickle.load(fp)

	def test_show_tasklist(self):
		os.system("python taskcheck.py --show")




if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_TaskChecker)
	unittest.TextTestRunner().run(suite)
