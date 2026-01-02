# class - A class is a blueprint that defines the properties and behavior of objects.

class Student:
    pass 

# Creating an object (instance) of the Student class
s1 = Student()
print(s1)  # Output: <__main__.Student object at 0x...>





#  adding a attribute(variables) to the class
class Student:
    def __init__(self, name, age):  # __init__ is a special method called a constructor
        self.name = name   #self refer to the current instance(object) of the class
        self.age = age

s1 = Student("Alice", 20)
s2 = Student("Bob", 22)

print(s1.name)  # Output: Alice
print(s2.age)   # Output: 22


# adding methods (functions) to the class
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)

    def is_pass(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail") 


s1 = Student("Alice", 85)
s1.display()  # Output: Name: Alice Marks: 85
s1.is_pass()  # Output: Pass                       






#  class variables vs instance variables
class Student:
    school = "ABC High School"  # class variable

    def __init__(self, name, age):
        self.name = name        # instance variable
        self.age = age          # instance variable 

s1 = Student("Alice", 20)
s2 = Student("Bob", 22)

# change school for s1 only
s1.school = "XYZ High School"
# python does not change the class variable for s1, it creates a new instance variable for s1

Student.school = "Devam High School"  # class variable remains unchanged


print(s1.school)        # XYZ High School
print(s2.school)        # ABC High School
print(Student.school)   # Devam High School
