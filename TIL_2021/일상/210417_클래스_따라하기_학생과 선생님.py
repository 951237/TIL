class Person:
	def __init__(self, name, number):
		self.name = name
		self.number = number
		
class Student(Person):
	UNDERGRADUATE = 0
	POSTGRADuATE = 1
	
	def __init__(self, name, number, studentType):
		super().__init__(name, number)
		self.studentType = studentType
		self.gpa = 0
		self.classes = []
		
	def enrollCourse(self, course):
		self.classes.append(course)
		
	def __str__(self):
		return "\nName = " + self.name + "\nScoNum = " + self.number + "\nSubject = " + str(self.classes) + "\nRate = " + str(self.gpa)
		
class Teacher(Person):
	def __init__(self, name, number):
		super().__init__(name, number)
		self.courses = []
		self.salary = 3000000
		
	def assignTeaching(self, course):
		self.courses.append(course)
		
	def __str__(self):
		return "\nName = " + self.name + "\nScoNum = " + self.number + "\nteachingSubject = " + str(self.courses) + "\nSarary = " + str(self.salary)
		
hong = Student("호기도", "12345678", Student.UNDERGRADUATE)
hong.enrollCourse("자료구조")
print(hong)

kim = Teacher("기처수", "12345678")
kim.assignTeaching("Python")
print(kim)
