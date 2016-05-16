#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'a test module'
__author__='Jia'

import sys
def test():
	args = sys.argv
	if len(args)==1:
		print 'Hello World!'
	elif len(args)==2:
		print 'Hello,%s!' % args[1]
	elif len(args)==3:
		print 'Hello,%s!' % args[2]
	else:
		print 'Too many argument!'

if __name__=='__main__':
	test()
