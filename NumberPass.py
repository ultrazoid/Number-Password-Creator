'''
Created on 23/02/2012

@author: ultrazoid_
'''

import random 
import time

print "Welcome to:\nultrazoid_'s\nPassword number generator" #prints a welcome message to the program
filename2="pass.settings"
sf=open(filename2, "r")
sef = sf.read(8)
if sef == ' ':
	sf.close()
	print "pass.settings not found creating..."
	sf = open(filename2, "w")
	ff=raw_input('Please enter a filename including a file extension to store password numbers in:')
	sf.write(ff)
else:
	ff=sef
sf.close()
filename=ff
fo= open (filename, "a") 

"""
^ imports time and random features
"""

ss = raw_input('press any key to continue(end to end):') #asks user to press any key or enter 'end' to stop the program


while ss != 'end':
	#if ss = 'clear'
	#	fo.delete(filename)
	#	fo
    bb = raw_input('What is this Password number for:')
    aa = str(random.randrange(1111,9999))
    ee = str(aa)
    """
    ^ defines the values of aa,bb,cc,dd as single digit natural numbers
    """
    print aa #prints the value of variables aa
    fo.write(bb)
    fo.write(':   ')
    fo.write(ee)
    fo.write('\n')
    ss = raw_input('press any key to continue(end to end):') #asks user to press any key or enter 'end' to stop the program
print 'ending...' #prints ending...
print 'saving...'
fo.close
time.sleep(5) #waits 5 seconds before ending