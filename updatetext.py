import numpy as np
import matplotlib.pyplot as plt
import sys
from sys import argv
import os
import fileinput

# still a work in progress!

#################had to update text file: make first couple twomassid's floats 

# set path to text file
filepath = os.path.abspath('../APO_KeplerMd_target.txt')

# set column names up (will make it easier to generalize later)
KIC = 'KIC'
Prot = 'Prot'
Prot_e = 'Prot_e'
Teff = 'Teff'
logg = 'logg'
kpmag = 'kpmag'
gmag = 'gmag'
zmag = 'zmag'
jmag = 'jmag'
kmag = 'kmag'
planet = 'planet'
twomassid = 'twomassid'
twomassid2 = 'twomassid2'
obsLR = 'obsLR'
obsHR = 'obsHR'

# set types to columns
types = \
	[
		(KIC, int),
		(Prot, float),
		(Prot_e,float),
		(Teff,float),
		(logg,float),
		(kpmag,float),
		(gmag,float),
		(zmag,float),
		(jmag,float),
		(kmag,float),
		(planet,int),
		(twomassid,float),
		(twomassid2,object),
		(obsLR, object),
		(obsHR, object)
	]

# load these with loadtext
data = np.loadtxt(filepath, usecols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], dtype = types, skiprows = 2)

#test:
print data[0]
#print data[KIC][0]
#print data[planet][0]
#print data[twomassid][0]
#print data[obsLR][0]
#print data[obsHR][0]


#Starting program Checks: 
print 'Update-Text Activated.' 
print 'Reading %s' % filepath	




#Beginning Program:

while True:

	row = None

	print 'Please type the KIC Number or "exit":'
	
	userinput_1 = raw_input('>  ')
	
	if userinput_1 == ('exit'):
		break
	
	if userinput_1 == '':
		continue

	for index, value in enumerate(data[KIC]): # enumerate numbers the items in this column
		if userinput_1 == str(value):
			row = data[index]
			break  #this tells the for loop to stop checking the column
	if row==None:
		print 'KIC Number not found.'
		continue

	print 'This is the data currently for this star: '
	print row

	# Ask which property to update:
	print 'Enter 1 = Update a property '
	print 'Enter 2 = Update another star: '
	
	
	userinput_2 = raw_input('>  ')
	if userinput_2 == ('1'):
		print 'Choose Property to update:'
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
	
	
		def printfunc(colname, index):
			print 'Current ' + colname + ': '
			print row[index]
			print 'Enter value to update to: '

	
		# user chooses parameter to update
		userinput_3 = raw_input('>  ')

		# user updates parameters
		if userinput_3 == '1':
			printfunc('Rotation Period', 1)
			userinput_Prot = raw_input('>  ')			
			row[1] = userinput_Prot
			print row

		if userinput_3 == '2':
			printfunc('Rotation Period Error', 2)
			userinput_Prot_e = raw_input('>  ')			
			row[2] = userinput_Prot_e
			print row

		if userinput_3 == '3':
			printfunc('Effective Temperature', 3)
			userinput_Teff = raw_input('>  ')
			row[3] = userinput_Teff
			print row

		if userinput_3 == '4':
			printfunc('Log g', 4)
			userinput_logg = raw_input('>  ')			
			row[4] = userinput_logg
			print row

		if userinput_3 == '5':
			printfunc('Current KP mag',5)
			userinput_KPmag = raw_input('>  ')			
			row[5] = userinput_KPmag
			print row

		if userinput_3 == '6':
			printfunc('Current g mag', 6)
			userinput_gmag = raw_input('>  ')			
			row[6] = userinput_gmag
			print row		

		if userinput_3 == '7':
			printfunc('Current zmag', 7)		
			print 'Enter value to update to: '
			userinput_zmag = raw_input('>  ')	
			row[7] = userinput_zmag
			print row

		if userinput_3 == '8':
			printfunc('Current J mag', 8)
			userinput_jmag = raw_input('>  ')			
			row[8] = userinput_jmag
			print row

		if userinput_3 == '9':
			printfunc('Current K mag', 9)
			userinput_kmag = raw_input('>  ')			
			row[9] = userinput_kmag
			print row

		if userinput_3 == '10':
			printfunc('Current Planet Count', 10)
			userinput_planet = raw_input('>  ')			
			row[10] = userinput_planet
			print row

		if userinput_3 == '11':    #This one takes up two columns currently and needs to be re-defined better
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
				print row


	elif userinput_2 == ('2'):
		continue
	
	




def writeToFile(data):
	newfile = filepath[0:len(filepath) - 4] + '.star' + '.txt'   # so that star is appended to the file name
	f = open(newfile, 'w')
	f.write('# Column Names \n')
	f.write('#  \n')
	for i in range(len(data)):  # for each row index
		for j in range(13): # for each column index (change to total number of columns)
			f.write(str(data[i][j]).rjust(12)) #write to file + tab 
		f.write(str(data[i][13]).rjust(30))
		f.write(str(data[i][14]).rjust(30))
		f.write('\n')
	f.flush # read in memory of the writer and commit to file
	f.close #close after editing

writeToFile(data)

print 'Saved new version of: %s.' % filepath


'''

#helpful links:
# http://learnpythonthehardway.org/book/ex15.html
# https://docs.python.org/2/library/functions.html#raw_input
'''
