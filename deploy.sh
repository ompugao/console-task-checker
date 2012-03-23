#!/bin/sh
#coding: utf-8

if [ -d "bin" ]; then
	cp task.py bin/task
	chmod +x ./bin/task
else
	mkdir bin
	cp task.py bin/task
	chmod +x ./bin/task

git add bin/task
	
