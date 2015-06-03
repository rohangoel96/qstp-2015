#Global Variables
studentList = []


#Class Declarations
class Student():
	
	def __init__(self,firstname,lastname):
		self.FirstName = firstname
		self.LastName = lastname
		
#Function Declarations
def printDetails(Student):
	print "First Name: %s\nLast Name: %s\n" %(Student.FirstName,Student.LastName)
	
def createStudentList():
	print("Creating a list of students.")
	numberOfStudents = int(raw_input("How many students to be created?\n"))
	
	for i in range(numberOfStudents):
		print "Enter details of student number %d" %(i+1)
		temporary_student = Student(raw_input("First Name\n"),raw_input("Last Name\n"))
		studentList.append(temporary_student)

def findStudentByFirstName():
	print ("Find student by first name")
	firstname = raw_input("Enter first name\n")
	
	for temp_student in studentList:
		if( temp_student.FirstName == firstname):
			return temp_student