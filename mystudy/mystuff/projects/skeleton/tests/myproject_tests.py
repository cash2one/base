#!/usr/bin/env python
# coding=utf-8

from nose.tools import *
import myproject

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

