#!/usr/bin/python
import re,sys,os,commands,subprocess
os.system('touch xft6.txt')
os.system('chmod 755 xft6.txt')
a = commands.getoutput('ls -lrt xft6*')
print a
x = subprocess.check_output('pwd')
print x
a = "naveen"
z,x,w,q,t,y = a
print z,x,w,q,t,y
c = a.split(' ')
print c , "list is defined"
abc = ['naveen','mahesh','suresh','ramesh','dinesh']
print "Reversing alternate elements from a list"
print abc
for i in range(1,len(abc),2):
    d = abc[i][::-1]
    abc.pop(i+1)
    abc.insert(i,d) 
    print abc

sys.stdout = open('xft6.txt','w')
print "Hello-world"
print "Welcome"
print "Bangalore"
sys.stdout.close()
os.system('rm -rf xft6.txt')
