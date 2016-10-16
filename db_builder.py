import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops
c.execute("DELETE FROM students;") #clean db before new execution
c.execute("DELETE FROM courses;") 

#============================================================================= students
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

#q = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);"
#c.execute(q)    #run SQL query

fObj = open("peeps.csv")
d=csv.DictReader(fObj)

for k in d:
    #print k
    p="INSERT INTO students VALUES (\'"+k['name']+"\',"+k['age']+","+k['id']+");"
    c.execute(p)

#============================================================================= courses
#q = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"
#c.execute(q)    #run SQL query

gObj = open("courses.csv")
e=csv.DictReader(gObj)

for l in e:
    #print l
    p="INSERT INTO courses VALUES (\'"+l['code']+"\',"+l['mark']+","+l['id']+");"
    c.execute(p)

#============================================================================= closing db

db.commit()
db.close()



'''
#============================================================================= testing
sqlite> .mode column
sqlite> .header on

sqlite> SELECT * FROM students;
name        age         id        
----------  ----------  ----------
kruder      44          1         
dorfmeiste  33          2         
sasha       22          3         
digweed     11          4         
tiesto      99          5         
bassnectar  13          6         
TOKiMONSTA  972         7         
jphlip      27          8         
tINI        23          9         
alison      23          10    

sqlite> SELECT * FROM courses;
code        mark        id        
----------  ----------  ----------
systems     75          1         
softdev     65          1         
ceramics    99          1         
systems     65          2         
softdev     75          2         
ceramics    98          2         
systems     55          3         
greatbooks  85          3         
softdev     75          4         
greatbooks  65          4         
greatbooks  55          5         
ceramics    90          6         
systems     90          6         
softdev     99          6         
greatbooks  70          7         
systems     88          7         
softdev     85          7         
systems     98          8         
softdev     55          9         
systems     85          10        
softdev     80          10   
'''

