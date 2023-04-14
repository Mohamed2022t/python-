from pathlib import Path
from sqlite3 import Connection
import sqlite3

class Db:
    DB_FILEPATH: Path
    DB_CONN: Connection
    def __init__(self) -> None:
        self.DB_FILEPATH = Path().joinpath("course_grades.db")
        self.DB_CONN = sqlite3.connect(self.DB_FILEPATH)
        
        self.cursor = self.DB_CONN.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS teacher (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_name  TEXT NOT NULL
            )''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            birth_date TEXT NOT NULL
            )''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS course_grade (
            course_name TEXT PRIMARY KEY ,
            teacher_id INTEGER NOT NULL,
            student_id INTEGER NOT NULL,
            grade NUMBER NOT NULL, 
            
            FOREIGN KEY(teacher_id) REFERENCES teacher(id),
            FOREIGN KEY(student_id) REFERENCES student(id)
            )''')
        self.DB_CONN.commit()


    def addStudent(self,record_data) -> None:
            sql_statement = "INSERT INTO student(first_name, last_name, birth_date)  VALUES(?, ?, ?)"
            self.cursor.execute(sql_statement, record_data)
            self.DB_CONN.commit() 
            return None 

    def addteacher(self,name) -> None:
        sql_statement = "INSERT INTO teacher(teacher_name)  VALUES(?)"
        self.cursor.execute(sql_statement, (name,))
        self.DB_CONN.commit()
    

    def addStudentGrade(self,record_data) -> None:
             
            sql_statement = "INSERT INTO course_grade(course_name, teacher_id, student_id, grade)  VALUES(?, ?, ?,?)"
            self.cursor.execute(sql_statement, record_data)
            self.DB_CONN.commit() 
            return None

    
    def getstudents (self,first_name,last_name) ->tuple:
        self.cursor.execute("SELECT * FROM student WHERE first_name = ? AND last_name = ?", (first_name, last_name))
        data = self.cursor.fetchone()
        return data
    
    def getteacher(self,teacher_name) -> tuple:
        self.cursor.execute("SELECT * FROM teacher WHERE teacher_name = ?", (teacher_name,))
        data = self.cursor.fetchone()
        return data
    
    def getTopStudent(self,course_name) -> float:
         
        self.cursor.execute('''SELECT student_id ,MAX(grade)  FROM course_grade
                 WHERE course_name = ? ''', (course_name,))
        max_grade1 = self.cursor.fetchone()
       
        return max_grade1 
    
    def showStudents(self) -> list:
        
        self.cursor.execute('''SELECT * FROM student,''') 
        self.DB_CONN.commit()
        self.cursor.close()
        return None

    def getcourse(self,course_name):
         
        self.cursor.execute("SELECT * FROM course_grade WHERE course_name = ? ", (course_name))
        data = self.cursor.fetchone()
        return data

    def get_student_byID(self,studentId):
        self.cursor.execute("SELECT * FROM student WHERE id = ? ", (studentId,))
        data = self.cursor.fetchone()
        return data
         
    def close_DB(self) ->None:
        
        self.cursor.close()
        return None