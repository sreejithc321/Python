
## Class
class Person(object):
	
	def __init__(self, name, surname, year_of_birth):
		self.name = name
		self.surname = surname
		self.year_of_birth = year_of_birth
	
	## function	
	def age(self, current_year):
		return current_year - self.year_of_birth
	
	def print_statement(self):
		return self.name, " is a person " 
		
## inheritance
class Student(Person):
	def __init__(self,student_id, *args, **kwargs):
		super(Student,self).__init__(*args, **kwargs)
		self.student_id = student_id
	
	## overriding	
	def print_statement(self):
		return self.name, " is a student " 


## polymorphism

def sum (item1,item2):
	return item1 + item2
	
## Testing		
user = Student(101,"sreejith","c",1990)
print user.age(2014)
print user.print_statement()

print sum(1,1)
print sum ("aaa","bbb")
print sum (['a','b','c'],['1','2','3'])
