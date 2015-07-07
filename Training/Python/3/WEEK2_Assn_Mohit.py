#Global Variables
studentList = []
TeacherList = []

#Class Declarations
class Student(object):
	
	def __init__(self,firstname,lastname,Date_of_birth,Year_of_Enrollment,Class_Enrolled_in,Section_enrolled_in):
		self.FirstName = firstname
		self.LastName = lastname
		self.DOB = Date_of_birth
		self.YearofEN = Year_of_Enrollment
		self.ClassEN = Class_Enrolled_in
		self.SectionEN = Section_enrolled_in
		self.rollnum = self.FirstName[0:2] + self.LastName[0:2] + self.YearofEN[len(Year_of_Enrollment)-2:]
class Teacher(object):
	
	def __init__(self,FirstName, LastName, YearJoined, DOB):
		self.firstname = FirstName
		self.lastname = LastName
		self.yearjoined = YearJoined
		self.dob = DOB	
#Function Declarations
def printDetails(studentList):
    n1 = raw_input("Enter student number:")
    print "First Name: %s\nLast Name: %s\nRoll Number: %s\n" %(studentList[int(n1)-1].FirstName,studentList[int(n1)-1].LastName,studentList[int(n1)-1].rollnum)
	
def createStudentList(studentList):
	print "Creating a list of students."
	numberOfStudents = int(raw_input("How many students to be created?\n"))
	
	for i in range(numberOfStudents):
		print "Enter details of student number %d" %(i+1)
		temporary_student = Student(raw_input("First Name\n"),raw_input("Last Name\n"),raw_input("DOB\n"),raw_input("Year of Enrollment\n"),raw_input("Class of Enrollment\n"),raw_input("Section enrolled in\n"))
		studentList.append(temporary_student)

def findStudentByFirstName(studentList) :
	print "Find student by first name"
	firstname = raw_input("Enter first name\n")
	
	for temp_student in studentList:
		if( temp_student.FirstName == firstname):
			return temp_student

def findStudentByLastName(studentList) :
	print "Find student by last name"
	lastname = raw_input("Enter last name\n")
	
	for temp_student in studentList:
		if( temp_student.LastName == lastname):
			return temp_student
			
def CreateTeacherList(TeacherList):
	print "Creating a list of teachers."
	numberofteachers = int(raw_input("How many teachers to be created?\n"))
	
	for i in range(numberofteachers):
		print "Enter details of student number %d" %(i+1)
		temporary_teacher = Teacher(raw_input("First Name\n"),raw_input("Last Name\n"))
		TeacherList.append(temporary_teacher)
		
def findTeacherByLastName(TeacherList):
	print "Find Teacher by last name"
	lastname = raw_input("Enter last name\n")
	
	for temp_teacher in TeacherList:
		if (temp_teacher.lastname == lastname ):
			return temp_teacher

def findTeacherbyDOB(TeacherList):
	print "Find Teacher by DOB"		
    DOB = raw_input("Enter a DOB\n")
		
	for temp_teacher in TeacherList:	
		if (temp_teacher.dob == DOB):
			return temp_teacher
		
def findStudentbyDOB(studentList):
	print "Find Student by DOB"	
	DOB = raw_input("Enter a DOB\n")	
		
	for temp_student in studentList:	
		if (temp_student.DOB == DOB):
			return temp_student

def Promotestudent(studentList):
	print "Lets promote a deserving student"
	promote_firstname = raw_input("Enter the first name of student\n")
	
	for temp_student in studentList:
		if (temp_student.Firstname == promote_firstname ):
			tmp1 = int(temp_student.ClassEN) 
			tmp1 += 1
			temp_student.ClassEN = str(tmp1)
			
def AddStudent(studentList):
	print "Lets add a student"
    temporary_student = Student(raw_input("First Name\n"),raw_input("Last Name\n"),raw_input("DOB\n"),raw_input("Year of Enrollment\n"),raw_input("Class of Enrollment\n"),raw_input("Section enrolled in\n"))
    
	studentList.append(temporary_student)
	
def AddTeacher():	
	print "Lets add a teacher"
	temporary_teacher = Teacher(raw_input("First Name\n"),raw_input("Last Name\n"),raw_input("Year of joining\n"),raw_input("DOB\n"))
	
	TeacherList.append(temporary_teacher)
	
def searchByYearEnrolled(studentList):
	print "Lets search according to the year of enrollment"
	temporaryList = []
	temp_yearEN = raw_input("Enter a year of enrollment")
	for temporary_student in studentList:
		if (temporary_student.YearofEN == temp_yearEN):
			temporaryList.append(temporary_student)
	return temporaryList
	
	
	
	
