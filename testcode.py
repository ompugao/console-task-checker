#!/usr/bin/env python
#coding: utf-8

import unittest

class [TestClass](unittest.TestCase):
	def setUp(self):
		pass

	def test_[testmethod]():
		pass



if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase([TestClass])
	unittest.TextTestRunner().run(suite)
