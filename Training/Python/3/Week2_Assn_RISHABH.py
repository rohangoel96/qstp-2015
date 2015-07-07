#RISHABH

#Global Variables
studentList = [] 
TeacherList = []

#Class Declarations
class Student():
	
	def __init__(self, firstname, lastname, dob, year_enrolled, _class, section):
		self.FirstName = firstname
		self.LastName = lastname
		self.dob = dob
		self.year_enrolled = year_enrolled
		self._class = _class
		self.section = section
		self.rollnumber = firstname[ : 2] + lastname[ : 2] + str(year_enrolled)[2 : ]

class Teacher() :
        def __init__(self, firstname, lastname, dob, year_joined) :
                self.FirstName = firstname
                self.LastName = lastname
                self.dob = dob
                self.year_enrolled = year_enrolled

#Function Declarations
def printDetails(Student):
	print "First Name: %s\nLast Name: %s\n" %(Student.FirstName,Student.LastName)
	
def createStudentList():
	print("Creating a list of students.")
	numberOfStudents = int(raw_input("How many students to be created?\n"))
	
	for i in range(numberOfStudents):
		print "Enter details of student number %d" %(i+1)
		temporary_student = Student(raw_input("First Name\n"),raw_input("Last Name\n"), raw_input("Date of birth\n"), int(raw_input("Year enrolled in\n")), int(raw_input("Class\n")), raw_input("Section"))
		studentList.append(temporary_student)

def createTeacherList() :
        print "Creating a list of teachers."
        numberOfTeachers = int(raw_input("How many teachers to be created?\n"))

        for i in range(numberOfTeachers) :
                print "Enter details of teacher number %d" %(i + 1)
                temporary_teacher = Teacher(raw_input("First Name\n"),raw_input("Last Name\n"), raw_input("Date of birth\n"), int(raw_input("Year enrolled in\n")))
                TeacherList.append(temporary_teacher)
                
def findStudentByFirstName():
	print ("Find student by first name")
	firstname = raw_input("Enter first name\n")
	
	for temp_student in studentList:
		if( temp_student.FirstName == firstname):
			return temp_student
def findStudentByLastName() :
        print "Find student by last name"
        lastname = raw_input("Enter last name\n")

        for temp_student in studentList :
                if temp_student.LastName == lastname :
                        return True
        return False

def findStudentByDOB() :
        print "Find student by DOB"
        DOB = raw_input("Enter DOB\n")

        for temp_student in studentList :
                if temp_student.dob == DOB :
                        return True
        return False

def findTeacherByLastName() :
        print "Find teacher by last name"
        lastname = raw_input("Enter last name\n")

        for temp_teacher in TeacherList :
                if temp_teacher.LastName == lastname :
                        return True
        return False

def findTeacherByDOB() :
        print "Find teacher by DOB"
        DOB = raw_input("Enter DOB\n")

        for temp_teacher in TeacherList :
                if temp_teacher.dob == DOB :
                        return True
        return False

def promoteStudent(student) :
        student._class += 1

def addStudent(student) :
        studentList.append(student)

def addTeacher(teacher) :
        TeacherList.append(teacher)


temp_student = findStudentByFirstName()
promoteStudent(temp_student)

def findStudentByYearEnrolled() :
        print "Find students by year enrolled."
        YEAR_ENROLLED = int(raw_input("Enter year enrolled : \n"))
        temp_list = []
        for temp_student in studentList :
                if temp_student.year_enrolled == YEAR_ENROLLED :
                        temp_list.append(temp_student)
        return temp_list
