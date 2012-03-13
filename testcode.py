#!/usr/bin/env python
#coding: utf-8

import unittest
import cPickle as pickle
import os

class Test_TaskChecker(unittest.TestCase):
	def setUp(self):
		pass

	def test_save_object(self):
		os.system("rm ~/.task_conteiner")
		os.system("python taskcheck.py --add 2012/03/15 確定申告")
		fp = open(os.path.expanduser("~/.task_conteiner"))
		loads = pickle.load(fp)
		print loads.length


if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_TaskChecker)
	unittest.TextTestRunner().run(suite)
