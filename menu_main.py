import pathlib
from menu import Menu
import simpleaudio
from  data_base import Db
class MenuMain(Menu): # MenuMain inheriting Menu
    APPLAUSE = simpleaudio.WaveObject.from_wave_file(pathlib.Path("./Soundss/applause.wav").__str__())
    
    # help_menu: MenuHelp
    def __init__(self) -> None:
        super().__init__(options=[
            { "description": "add teacher", "action": self.createTeacherData}, # done
            { "description": "addStudent", "action": self.createStudentData },# done
            { "description": "addGrade", "action": self.insertNewGrade },# done  
            { "description": "Top student ", "action": self.PrintTopStudents },# done
        ])
        self.Db = Db()
        return None
    
    def applause(self) -> None: # to play applause sound
        print("Congratulations!")
        play_obj = self.APPLAUSE.play()
        play_obj.wait_done()
        return None
    
    def createStudentData(self) -> None: 
        print("Insert student details:")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        birth_date = (input("Date of birth: "))
        student_data = (first_name, last_name, birth_date,) 
        self.Db.addStudent(student_data)
        return None
    
    def createTeacherData(self) -> None: 
        print("Insert Teacher details:")
        TeacherName = input("Enter teacher name: ")
        self.Db.addteacher(TeacherName)
        return None
    
    def createStudentGrade(self) -> None:
        print("Insert student grade:")
        course_name = input("Course name: ")
        teacher_id = (input("Teacher mame: "))
        student_id = (input("Student id: "))
        course_grade = float(input("Course grade: "))
        course_date = float(input("Course date: "))
        student_grade = (course_name, teacher_id, student_id, course_grade, course_date,) 
        return student_grade
    

    
    def insertNewGrade(self) -> None: 
        print("Insert grade details:")
        course_name = input("Course name: ")
        while True:
            teacher_Name = input("Teacher Name: ")
            teacher_data = self.Db.getteacher(teacher_Name)
            if teacher_data is not None:
                break
            else:
                print("teacher dosent exsist try again.")
        
        while True:

            student_firstName = input("Student first Name: ")
            student_lastname = input("student last name: ")
            student_data = self.Db.getstudents(student_firstName,student_lastname)
            
            
            if student_data is not None:
                break
            else:
                print("student dosent exisit try again.")
            
        
        grade = float(input("Course grade: "))
        
        student_new_grade = (course_name, teacher_data[0], student_data[0], grade,) 
        self.Db.addStudentGrade(student_new_grade)
        return None
    
    def PrintTopStudents(self) -> None:
        while True:
            course_name=input("course name: ")
            max_grade1 = self.Db.getTopStudent(course_name)
            if max_grade1 is not None:
                break 
            else:
                print("wrong course name")
        student = self.Db.get_student_byID(max_grade1[0])
        print(f"The top grade: {max_grade1[1]} belongs to {student[1]} {student[2]}")
        self.applause()
    
    