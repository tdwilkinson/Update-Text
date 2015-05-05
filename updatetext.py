import numpy as np
import matplotlib.pyplot as plt
import sys
from sys import argv
import os
import fileinput
from pandas import *
import pandas as pd

# still need to generalize, which would be really cool!	


################# do not run in background (with &)
################# change what to append the file name to at the bottom! add variable for this up top

#mergefiles.py for how I combined data frames of text file and kepler information. do same for Prot

# should load all the information i need: 

df = pd.DataFrame.from_csv('../mergefiles.txt',sep=',',header = 0)
colnames = list(df.columns.values)

#Starting program Checks: 
print 'Update-Text Activated.' 
#print 'Reading %s' % filepath	

#Beginning Program:

while True:

	print 'Please type the KIC Number or "exit":'
	userinput_1 = raw_input('>  ')	

	if userinput_1 == ('exit'):   #just incase ya wanna quit
		break	

	if userinput_1 == '': #kic number in question
		continue


	kicnumber = -1
	for KIC in df.index:
		if int(userinput_1) == KIC:
			print 'This is the data currently for this star: '
			print df.loc[KIC]
			kicnumber = KIC
			break

	if kicnumber == -1:
		print 'KIC number not found' 
		continue

	# Ask which property to update:
	print 'Enter 1 = Add a property'
	print 'Enter 2 = Change/Append a property' 
	print 'Enter 3 = Update another star: '
	print "or 'exit' "
	userinput_2 = raw_input('>  ')

	# this option allows for a new property (column) to be added
	if userinput_2 == ('1'):
		print 'Enter new column name:'
		userinput_newcol = raw_input('>  ')
		print 'enter value to add to new column'
		userinput_newcolvalue = raw_input('>  ')
		if userinput_newcolvalue == '':
			continue
		else:
			#df.assign(color_g_z = df['gmag'] - df['zmag']).head()
			df.insert(20,userinput_newcol,value = userinput_newcolvalue, allow_duplicates=False)
			continue

	# this option allows a property to be changed or appended to	
	elif userinput_2 == ('2'):
		print 'Enter in the number for the property to update:'
		choices = []
		num = range(0,25)
		for y in colnames:
			for x in num:
				print str(x) +'.  '+  y
				print '99.  ' + userinput_newcol
				break     #not quite but close enough for now

		def printfunc(rowLabel, columnLabel):
			print columnLabel + '\t' + str(df.get_value(rowLabel, columnLabel))
			print 'Enter value to update to: '
		
		# user chooses parameter to update
		userinput_3 = raw_input('>  ')

		# if they chose a property (column) that already existed
		if int(userinput_3) in num:
			printfunc(kicnumber, colnames[int(userinput_3)])
			userinput_decision = raw_input('>  ')	
			if userinput_decision == '':
				continue
			else:
				df.set_value(kicnumber, colnames[int(userinput_3)], userinput_decision)
			print 	str(kicnumber) + '\t' + colnames[int(userinput_3)] + '\t' + str(df.get_value(kicnumber, colnames[int(userinput_3)]))
		
		# if they chose a property (column) that was created with option 1		
		elif userinput_3 == '99':
			printfunc(kicnumber, str(userinput_newcol))
			userinput_decision = raw_input('>  ')	
			if userinput_decision == '':
				continue
			else:
				df.set_value(kicnumber, [str(userinput_newcol)], userinput_decision)
			#print 	str(kicnumber) + '\t' +[str(userinput_newcol)] + '\t' + str(df.get_value(kicnumber, [str(userinput_newcol)]))
			print 'seeing is believing here'
			continue
			#printfunc(kicnumber, colnames[int()])		
		
		# if finished		
		elif userinput_3 == 'exit':
			print 'nope!'
			break	

		# error message when it doesn't understand
		elif userinput_3 != num or '99':
			print 'err... '
			break # for now


		'''if userinput_3 == '11':    #This one takes up two columns currently and needs to be re-defined better
			print 'Current 2MASS ID Number: '
			print str(row[11]) + str(row[12])
			print 'Enter 1st part of value up to +'
			userinput_twomassid = raw_input('>  ')
			row[11] = userinput_twomassid
			print 'Enter 2nd part of value including +'
			userinput_twomassid2 = raw_input('>  ')
			row[12] = userinput_twomassid2
			print row	
		
		if userinput_3 == '12':  # here we may want to append instead of just change
			print 'Current Low-Res Observing Date: '
			print row[13]
			print 'Enter 1 = Append or 2 = Change Date'
			userinput_obsLR = raw_input('>  ')
			if userinput_obsLR == '1':
				print 'Enter Date to append:'
				userinput_addDate = raw_input('>  ')
				addDate = row[13] + '/' + userinput_addDate
				row[13] = addDate
				print row
			if userinput_obsLR == '2':
				print 'Enter Date update to:'
				userinput_newDate = raw_input('>  ')
				row[13] = userinput_newDate
				print row

		if userinput_3 == '13': # same append or change
			print 'Current High-Res Observing Date: '
			print row[14]
			print 'Enter 1 = Append or 2 = Change Date'
			userinput_obsHR = raw_input('>  ')
			if userinput_obsHR == '1':
				print 'Enter Date to append:'
				userinput_addDate = raw_input('>  ')
				addDate = row[14] + '/' + userinput_addDate
				row[14] = addDate
				print row
			if userinput_obsHR == '2':
				print 'Enter Date update to:'
				userinput_newDate = raw_input('>  ')
				row[14] = userinput_newDate
				print row'''
	
	# to get back to choose kic option
	elif userinput_2 == ('3'):
		continue

	# to exit the program
	elif userinput_2 == 'exit':
		break	


#write the file anew each time
df.to_csv('../mergefiles.txt',sep=',',header = (str(colnames)+str(userinput_newcol)))
 # try columns keyword to only get certain columns - get rid of mystery?

#helpful links:
# http://learnpythonthehardway.org/book/ex15.html
# https://docs.python.org/2/library/functions.html#raw_input
# http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.html
