#!/bin/bash
#coding=utf-8
import os
from multiprocessing import Pool

#for k in m:


def runNmap(k):
    cmd2 = r'nmap -A -p' + m[k] + ' -oX nmapResult --append-output ' + k
    os.system(cmd2)


os.system("rm -rf nmapResult")
cmd = r'masscan -c masscan.conf -oL masscanresult'

os.system(cmd)
m = {}
with open('masscanresult', 'r') as f:
    for line in f.readlines():
        l = line.split()
        if l[0] == "open":
            #print (l)
            m[line.split()[3]] = line.split()[2]

pool = Pool(2)
pool.map(runNmap, m)
#os.system("rm -rf masscanresult.xml")
#for k in m:
#def runNmap(k):
#    cmd2=r'nmap -A -p'+m[k]+' -oX nmapResult --append-output '+k
#    print(cmd2)
