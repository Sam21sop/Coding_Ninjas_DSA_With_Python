'''
class ClassName:
    #body
'''
import sys
#example 
class Student:
    name ='sopan'
    course = 'AIML'
    
    def show_details(self):
        print(self.name)
        print(self.course)

# create object
s1 = Student()
print(type(s1), sys.getsizeof(s1))
print(s1.name)
print(s1.course)