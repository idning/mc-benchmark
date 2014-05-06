#!/usr/bin/env python
#coding: utf-8
#file   : test_mget.py
#author : ning
#date   : 2014-04-01 13:15:48

import os
import re
import commands

ports = [
    4101,  # before improve
    4100,  # after improve
    2200   # mc
]

def system(cmd):
    return commands.getoutput(cmd)

def extra(regex, text):
    match = re.search(regex, text, re.DOTALL)
    if match:
        return match.group(1)

def testit():
    for mget_size in [10, 100, 1000, 10000]:
        for port in ports:
            cnt = 1000*1000 / mget_size
            clients = 50
            if mget_size == 10000:
                clients = 2
            cmd = '/home/ning/idning-github/mc-benchmark/mc-benchmark.%d -n %d -p %d -r 1000000000 -c %d' % (mget_size, cnt, port, clients)
            #print cmd
            rst = system(cmd)

            #100.00% <= 2 milliseconds
            #28089.89 requests per second
            rtime = extra('100.00% <= (\d+) milliseconds', rst)
            qps = extra('([\.\d]+) requests per second', rst)

            print 'mget_size=%d on %d: pqs: %s, rtime: %s' % (mget_size, port, qps, rtime)

testit()
