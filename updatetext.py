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

#mergefiles.py for how I combined data frames
# for reference : 
#colnames = [ 'Prot', 'Prot_e','Teff','logg','kpmag','gmag','zmag','jmag','kmag','planet','twomassid','t2','mystery','obsLR','obsHR','KEPLER_2massid','KEPLERTeff', 'KEPLERrmag','KEPLERJmag','KEPLERmag','KEPLERg_r','KEPLERlogg','KEPLER_Z','KEPLER_Eb_v']

# should load all the information i need: 
df = pd.DataFrame.from_csv('../mergefiles.txt',sep=',',header = 0)
#print df.head(3) #test
#print df.index
#print type(df)

#want to add two columns next to LR HR if Ha or CaIII was observed


#Starting program Checks: 
print 'Update-Text Activated.' 
#print 'Reading %s' % filepath	

#print df

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
	print 'Enter 1 = Change/Append a property'
	print 'Enter 2 = Update another star: '
	userinput_2 = raw_input('>  ')

	if userinput_2 == ('1'):
		print 'Enter in the number for the property to update:'
		choices = []
		num = range(0,23)
		array = [ 'Prot', 'Prot_e','Teff','logg','kpmag','gmag','zmag','jmag','kmag','planet','twomassid','t2','mystery','obsLR','obsHR','KEPLER_2massid','KEPLERTeff', 'KEPLERrmag','KEPLERJmag','KEPLERmag','KEPLERg_r','KEPLERlogg','KEPLER_Z','KEPLER_Eb_v']
		for y in array:
			for x in num:
				print str(x) +'.  '+ y
				break     #not quite but close enough for now

		def printfunc(rowLabel, columnLabel):
			print columnLabel + '\t' + str(df.get_value(rowLabel, columnLabel))
			#print df.get_value(df.loc[KIC],array[int(userinput_3)-1])
			print 'Enter value to update to: '
		
		
		# user chooses parameter to update
		userinput_3 = raw_input('>  ')

		if int(userinput_3) in num:
			printfunc(kicnumber, array[int(userinput_3)])
			userinput_decision = raw_input('>  ')			
			df.set_value(kicnumber, array[int(userinput_3)], userinput_decision)
			print 	str(kicnumber) + '\t' + array[int(userinput_3)] + '\t' + str(df.get_value(kicnumber, array[int(userinput_3)]))
		elif userinput_3 == 'exit':
			print 'nope!'
			break	
		elif userinput_3 != num:
			print 'err... '
			break
'''
####

		# user updates parameters
		if userinput_3 == '1':
		
Prot 45.34356
45.234567	

		if userinput_3 == '2':
			printfunc(KIC,'Prot_e')	
			userinput_Prot_e = raw_input('>  ')			
			enteredvalue = userinput_Prot_e
			print enteredvalue

		if userinput_3 == '3':
			printfunc(KIC,'Teff')	
			userinput_Teff = raw_input('>  ')
			enteredvalue = userinput_Teff
			print enteredvalue

		if userinput_3 == '4':
			printfunc(KIC,'logg')
			userinput_logg = raw_input('>  ')			
			enteredvalue = userinput_logg
			print enteredvalue

		if userinput_3 == '5':
			printfunc(KIC,'kpmag')
			userinput_KPmag = raw_input('>  ')			
			enteredvalue = userinput_KPmag
			print enteredvalue

		if userinput_3 == '6':
			printfunc(KIC, 'gmag')
			userinput_gmag = raw_input('>  ')			
			enteredvalue = userinput_gmag
			print enteredvalue	

		if userinput_3 == '7':
			printfunc(KIC, 'zmag')		
			print 'Enter value to update to: '
			userinput_zmag = raw_input('>  ')	
			enteredvalue = userinput_zmag
			print enteredvalue

		if userinput_3 == '8':
			printfunc(KIC, 'jmag')
			userinput_jmag = raw_input('>  ')			
			enteredvalue = userinput_jmag
			print enteredvalue

		if userinput_3 == '9':
			printfunc(KIC, 'kmag')
			userinput_kmag = raw_input('>  ')			
			enteredvalue = userinput_kmag
			print enteredvalue

		if userinput_3 == '10':
			printfunc(KIC, 'planet')
			userinput_planet = raw_input('>  ')			
			enteredvalue = userinput_planet
			print enteredvalue

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
	
############### do stuffs with columns in panda:

mdwarf.assign(color_g_z = mdwarf['gmag'] - mdwarf['zmag']).head() # to make a new column out of old
dataframe.insert ( to add column)

############## write to file: 

def writeToFile(data):
	newfile = filepath[0:len(filepath) - 4] + 'test' + '.txt'   # increase number right now so that updates are appended to the file name
	f = open(newfile, 'w')
	f.write("# #          KID       Prot       e_Prot   Teff     logg   	 KPmag     	  g'      	 z'       Jmag      Kmag 	 Planet? 	2MassID 	  DATE_OBSERVED_LR   DATE_OBSERVED_HR \n") 
	f.write('#  \n')
	for i in range(len(data)):  # for each row index
		for j in range(15): # for each column index (change to total number of columns)
			f.write(str(data[i][j]) + ',') #write to file + tab 
		#f.write(str(data[i][13]).rjust(18))
		#f.write(str(data[i][14]).rjust(27))
		f.write('\n')
	f.flush # read in memory of the writer and commit to file
	f.close #close after editing

writeToFile(data)

print 'Saved new version of: %s.' % filepath

# ADD PROPERTY TO CHOOSE OPTION - 


#helpful links:
# http://learnpythonthehardway.org/book/ex15.html
# https://docs.python.org/2/library/functions.html#raw_input

# old method: 


# set path to text file
filepath = os.path.abspath('../APO_KeplerMd_target.updated.txt') # does not interate, must change name to appended file name to keep updates from original

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
#KEPLER_Teff = 'KEPLER_Teff'
#KEPLER_rmag = 'KEPLER_rmag'
#KEPLER_Jmag = 'KEPLER_Jmag'
#KEPLER_Mag = 'KEPLER_Mag'
#KEPLER_Colorg-r = 'KEPLER_Color'
#KEPLER_logg = 'KEPLER_logg'
#KEPLER_Z = 'KEPLER_Z' #metallicity
#KEPLER_r = 'KEPLER_r' #solar radius = 0.0
#KEPLER_Eb-v = 'KEPLER_Eb-v'
planet = 'planet'
twomassid = 'twomassid'
twomassid2 = 'twomassid2'
obsLR = 'obsLR'
LRha = 'LRha'
LRcaIII = 'LRcaIII'
obsHR = 'obsHR'
HRha = 'HRha'
HRcaIII = 'HRcaIII'

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
		#(KEPLER_Teff),int),
		#(KEPLER_rmag, float),
		#(KEPLER_Jmag, float),
		#(KEPLER_Mag, float),
		#(KEPLER_Colorg-r, float),
		#(KEPLER_logg, float),
		#(KEPLER_Z, float),
		#(KEPLER_r, float),
		#(KEPLER_Eb-v, float),
		(planet,int),
		(twomassid,float),
		(twomassid2,object),
		(obsLR, object),
		(obsHR, object)
	]

# load these with loadtext
data = np.loadtxt(filepath, usecols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], dtype = types, skiprows = 2)

#test:
#print data[0]
#print data[KIC][0]
#print data[planet][0]
#print data[twomassid][0]
#print data[obsLR][0]
#print data[obsHR][0]

working on this part:

while True:

	#row = None

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
'''
