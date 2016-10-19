import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops


viewGrades = c.execute("SELECT name,students.id,mark FROM students,courses WHERE students.id == courses.id")
#for record in viewGrades:
    #print record
    

def computeAvg():
	name = "" # CURRENT person's name
	gradeSum = 0 # CURRENT person's total grade
	numCourses = 1 
	avg = 0 

	print ("name | id | average ")

	for record in viewGrades: 

		# variables
		recName = record[0]
		recID = record[1]
		recGrade = record[2]

		# if you are on a NEW person
		if (name != recName):

			avg = float(gradeSum) / numCourses #calculate avg of CURRENT person bc ur done w him

			if (name != ""): # executes only when you're on 1ST person
				print ("%s, %d, %f"%(name, recID-1, avg)) # print out CURRENT person's info

			name = recName # NEW person is now your CURRENT person ============================
			gradeSum = avg = 0 # reset counters
			numCourses = 1
			gradeSum += recGrade #add CURRENT grade

		# if you are on the CURRENT/SAME person
		else:
			gradeSum += recGrade # just keep addin'
			numCourses += 1

	# this takes care of the last record info, out of while loop
	avg = float(gradeSum) / numCourses 
	print ("%s, %d, %f"%(name, recID, avg))

computeAvg()

db.commit()
db.close()

'''
OUTPUT OF computeAvg()
===========================
name | id | average 
kruder, 1, 79.666667
dorfmeister, 2, 79.333333
sasha, 3, 70.000000
digweed, 4, 70.000000
tiesto, 5, 55.000000
bassnectar, 6, 93.000000
TOKiMONSTA, 7, 81.000000
jphlip, 8, 98.000000
tINI, 9, 55.000000
alison, 10, 82.500000
'''

