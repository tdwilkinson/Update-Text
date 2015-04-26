import numpy as np
import matplotlib.pyplot as plt
import sys
from sys import argv
import os
import fileinput



# I want to replace all -99 as -
# make a window that pops up? maybe just promt
# select item from list of 1st row  options. KID, Date OBservered
# type in number and it pulls up list and options from chart
# can update options for these text files
# add in observing dates via name of star

# search txt file by column then by row. 
'''
with open('APO_KeplerMd_target.txt') as input_file: #open file
	lines =  [line.rstrip().split('\t') # read the lines, split by tab
	for line in input_file.readlines()]

def find_mdwarf(search_term, column):
	return next((('\t').join(line) for line in lines
		if line[column-1] == search_term), None)
'''
# For easy changing:

filepath = os.path.abspath('../APO_KeplerMd_target.txt')

f = open(filepath,'r+')
# Set Column titles:
#KIC,Prot,Prot_e,Teff,logg,kpmag,gmag,zmag,jmag,kmag,planet,twomassid,obsLR,obsHR = np.loadtxt('APO_KeplerMd_target.txt', usecols = (0,1,2,3,4,5,6,7,8,9,10,11,12,13), unpack=True)
#Start Updating!
#properties = (Prot,Prot_e,Teff,logg,kpmag,gmag,zmag,jmag,kmag,planet,twomassid,obsLR,obsHR)

print 'Update-Text Activated.' 
print 'Reading %s' % filepath	
print 'Please type the KIC Number:'

userinput_1 = raw_input('>  ')
#print userinput_1
# test  2285598   36.493999    0.096000  3951    4.4930   11.9730   13.2920   11.1060    9.8970    9.1030      0 19072124 +3741480   20130514

#for index, line in enumerate(fileinput.input(filepath, inplace = 1)): 
#	newline = line

for line in f:
	if userinput_1 in line:
		print 'Enter 1 = Update /n or 2 = List Properties'
# need to add: if it doesn't find it, print not found, just make sure it doesn't go through every line

		userinput_2 = raw_input('>  ')
		if userinput_2.startswith('1'):
			print 'Enter Property to update:'
			print '1 = Rotation Period'
			print '2 = Rotation Period Error'
			print '3 = Effective Temperature' 
			print '4 = Log G'
			print '5 = KP mag' 
			print "6 = g mag"
			print "7 = z mag"
			print '8 = J mag'
			print '9 = K mag'
			print '10 = Planet Count'
			print '11 = 2Mass ID Number'
			print '12 = Observation Date in Low Resolution'
			print '13 = Observation Date in High Resolution'
			print '14 = List All Properties'
	
		userinput_3 = raw_input('>  ')
		if userinput_3 == '1':
			parameter1 = line.split()
			print parameter1[1]

# next repeat for all columns: onlyworks for 1 and 12 so far

		if userinput_3 == '12':
			LRobs = line.split()
			print LRobs[13] # need to fix columns in this file
			print 'Add Low Res Observing Date [yearmonthday]:'
			
#may need to add catch to star name
			userinput_LRobs = raw_input('>  ')
			thingToAddTo = LRobs[13]
			
		for num in thingToAddTo:	
			if "-99" in thingToAddTo:
				thingToAddTo = userinput_LRobs
			else:
				thingToAddTo = thingToAddTo + "/" + userinput_LRobs
				thingToAdd = '/' + userinput_LRobs
				#f.write(str(thingToAdd))
			print thingToAddTo


# rays notes; read in whole file,  find one columna and column replace value in column do for multiple stuff and then rewrite file
			
'''
		if userinput_3 == '13':
			parameter1 = line.split()
			print parameter1[13]

			for item in Prot:
				Prot_match = Prot[item == kicnumber]
				print Prot_match
				print Prot[kicnumber]
		if userinput_2 == '2':
			print txt.read([0][2])
		
			
		
		

		elif userinput.startswith('2'):
			print txt.read([0][1][2][3])
		else:
			print 'KIC not found.'

'''
#print(find_mdwarf)


#helpful links:
# http://learnpythonthehardway.org/book/ex15.html
# https://docs.python.org/2/library/functions.html#raw_input
