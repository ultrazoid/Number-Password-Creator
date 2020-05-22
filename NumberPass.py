'''
Created on 23/02/2012

Last Update on 22/05/2020

@author: ultrazoid_
'''

import random 
import time
import string

"""
^ imports needed core features
"""

"""
### NOTES: WHAT TO DO

ALL WANTED FEATURES ADDED
"""

print "Welcome to:\nultrazoid_'s\nPassword number generator" #prints a welcome message to the program
filename2 = "pass.settings"
sf = open (filename2, "r")
sef = sf.read(8)
if sef == ' ':
	sf.close()
	print "Settings file not found creating..."
	sf = open (filename2, "w")
	ff = raw_input('Please enter a filename to store password numbers in:')
	ff += '.yml'
	sf.write(ff)
else:
	ff=sef
sf.close()
filename=ff
try:
        fo = open (filename, "r")
except IOError:
        print "Allocated file note found"
        fo = open (filename, "a")
        print "Creating"
        fo.close()
        print "Created!"

ss = raw_input('press any key to continue(end to end):') #asks user to press any key or enter 'end' to stop the program

while ss != 'end':
    fo = open (filename, "r")
    pass_name = raw_input('What is this Password number for:')
    twin = pass_name + ':'
    #check to see if line needs to be overwritten
    overCheck = fo.readlines()
    overDo = False
    for locale in overCheck:
        form = string.split(locale, ' ')
    	if twin == form[0]:
    		overDo = True
    		overCheck.remove(locale)
    	else:
    		do = "nothing"
    fo.close()
    if overDo == True:
    	open(filename, 'w').close()
    	fo = open (filename, "a")
    	for line in overCheck: 
    		fo.write(line)
 	fo.close()
 	fo = open (filename, "a")
    if overDo == False:   
        fo = open (filename, "a")

    ab = str(random.randrange(0,9))
    
    length = int(raw_input('how long should the PIN be?:'))

    start_p = 0
    pinn = str('')

    while start_p != length:
        num = str(random.randrange(0,9))
        pinn = str(pinn + num)
        start_p = start_p + 1

    """
    Asks the user how long the pin should be then generates a PIN of that length with random numbers
    """
    print pinn #prints the pin
    fo.write(pass_name)
    fo.write(':   ')
    fo.write(pinn)
    fo.write('\n')
    fo.close()
    ss = raw_input('press any key to continue(end to end):') #asks user to press any key or enter 'end' to stop the program
print 'ending...' #prints ending...
print 'saving...'
fo.close
time.sleep(5) #waits 5 seconds before ending
