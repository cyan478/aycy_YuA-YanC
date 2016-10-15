import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

#q = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"
#c.execute(q)    #run SQL query

fObj = open("peeps.csv")
d=csv.DictReader(fObj)

for k in d:
    #print k
    p="INSERT INTO students VALUES (\'"+k['name']+"\',"+k['age']+","+k['id']+")"
    c.execute(p)
#================================================================
#q = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"
#c.execute(q)    #run SQL query

gObj = open("courses.csv")
e=csv.DictReader(fObj)

for l in e:
    #print k
    p="INSERT INTO courses VALUES (\'"+l['code']+"\',"+l['mark']+","+l['id']+")"
    c.execute(p)
#==========================
c.execute("SELECT * FROM students")
c.execute("SELECT * FROM courses")

db.commit()
db.close()
