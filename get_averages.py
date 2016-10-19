import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

viewGrades = c.execute("SELECT name,mark FROM students,courses WHERE students.id == courses.id")
for record in viewGrades:
    print record
    

computeAverage

name=""
grade=0
numCourses=0

db.commit()
db.close()
