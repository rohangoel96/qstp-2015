# -*- coding: utf-8 -*-

'''

3. Do the following
	3.1 Add more fields to the object student. Date of Birth, Year of Enrollment, Class Enrolled in,
		Section enrolled in. All dates should be stored in DDMMYYYY format and read directly from raw input.
		These fields should be asked during createStudent.
		
	3.2 Create a rollnumber during __init__ for the student based on the last 4 digits of the year enrolled and and the first two letters of 
		first and last name. So the roll number for Parthey Agrawal enrolled in 2014 would be PaAg14.
		
	3.2 Create a list called TeacherList and create a class called Teacher. Add the required fields to it.
		First Name, Last Name, Year Joined, DOB. Create a createTeacherList function as well.
		
	3.3 Create functions for searching by last name, Date of Birth for both Teachers and Students.
	
	3.4 Create a function called promoteStudent which takes in a student object as an input and increases his 
		class enrolled in by 1.
		
	3.5 Create a function called addStudent which adds a student to the studentList. Same for the teachers.
	
	3.6 Search a student by firstname using the function. Store this in a temp_student variable. Feed it to 
		promote student function.
		
4. This one is little tough.
	4.1 Create a function called searchByYearEnrolled. Now this function has to return a list. 
		It should ask for year enrolled, iterate over the studentList and match the year enrolled. 
		For every hit found it should add the student object to a temporary list. It should return the 
		list after the for loop is over.
'''


#Global Variables
studentList = []
teacherList = []


#Class Declarations
class Teacher():
	'''Create a list called TeacherList and create a class called Teacher. Add the required fields to it.
		First Name, Last Name, Year Joined, DOB. Create a createTeacherList function as well.'''
	
	def __init__ (self,firstname,lastname,dob,year_joined): 
		self.FirstName = firstname
		self.LastName = lastname
		self.dob = dob
		self.year_joined = year_joined



class Student():
	
	def __init__(self,firstname,lastname,dob,year_enroll,class_enroll,section_enrol):
		self.FirstName = firstname
		self.LastName = lastname
		self.dob = dob
		self.year_enroll = year_enroll
		self.class_enroll = class_enroll
		self.section_enrol = section_enrol
		self.roll=firstname[:2]+lastname[:2]+year_enroll[-2:]

#Function Declarations
def printDetails(student):
	print "First Name: %s\nLast Name: %s\n" %(student.FirstName,student.LastName)
	
def createStudentList():
	print("Creating a list of students.")
	numberOfStudents = int(raw_input("How many students to be created?\n"))
	
	for i in range(numberOfStudents):
		print "Enter details of student number %d" %(i+1)
		temporary_student = Student(raw_input("First Name\n"),raw_input("Last Name\n"),raw_input("Date of Birth (DDMMYYYY)\n"),\
									raw_input("Year of Enrollment\n"),raw_input("Class Enrolled in\n"),\
									raw_input("Section Enrolled in\n"))

		studentList.append(temporary_student)


'''3.3 Create functions for searching by last name, Date of Birth for both Teachers and Students.'''


def createTeacherList():
	print("Creating a list of Teachers.")
	numberOfTeachers = int(raw_input("How many teachers to be created?\n"))
	
	for i in range(numberOfTeachers):
		print "Enter details of Teacher number %d" %(i+1)
		temporary_teacher = Teacher(raw_input("First Name\n"),raw_input("Last Name\n"),raw_input("Date of Birth (DDMMYYYY)\n"),\
									raw_input("Year of Joining\n"))

		teacherList.append(temporary_teacher)

def findStudentByFirstName():
	print ("Find student by first name")
	firstname = raw_input("Enter first name\n")
	
	for temp_student in studentList:
		if( temp_student.FirstName == firstname):
			return temp_student

def findTeacherByFirstName():
	print ("Find teacher by first name")
	firstname = raw_input("Enter first name\n")
	
	for temp_teacher in teacherList:
		if( temp_teacher.FirstName == firstname):
			return temp_teacher


def findStudentByLastName():
	print ("Find student by last name")
	name = raw_input("Enter last name\n")

	for temp_student in studentList:
		if( temp_student.LastName == name):
			return temp_student

def findTeacherByLastName():
	print ("Find teacher by last name")
	name = raw_input("Enter last name\n")

	for temp_teacher in teacherList:
		if( temp_teacher.LastName == name):
			return temp_teacher


def promoteStudent(student):
'''
3.4 Create a function called promoteStudent which takes in a student object as an input and increases his 
		class enrolled in by 1.
'''
	student.class_enroll+=1

'''
	3.5 Create a function called addStudent which adds a student to the studentList. Same for the teachers.
	
'''

def addStudent():
	print "Add a student"
	temporary_student = Student(raw_input("First Name\n"),raw_input("Last Name\n"),raw_input("Date of Birth (DDMMYYYY)\n"),\
									raw_input("Year of Enrollment\n"),raw_input("Class Enrolled in\n"),\
									raw_input("Section Enrolled in\n"))

	studentList.append(temporary_student)

def addTeacher():
	print "Add a teacher"
	temporary_teacher = Teacher(raw_input("First Name\n"),raw_input("Last Name\n"),raw_input("Date of Birth (DDMMYYYY)\n"),\
									raw_input("Year of Joining\n"))

	teacherList.append(temporary_teacher)

'''
3.6 Search a student by firstname using the function. Store this in a temp_student variable. Feed it to 
		promote student function.	
'''	


print "Create Student List"
createStudentList()

print "Promote class of student"
promote(findStudentByFirstName(raw_input("First Name of the Student")))

'''
Create a function called searchByYearEnrolled. Now this function has to return a list. 
		It should ask for year enrolled, iterate over the studentList and match the year enrolled. 
		For every hit found it should add the student object to a temporary list. It should return the 
		list after the for loop is over.
'''

def searchByYearEnrolled():
	templist = []
	year = raw_input("Enter the year enrolled")

	for student in studentList:
		if student.year_enroll == year:
			templist.append(student)
	return templist
	