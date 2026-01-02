# Inheritance = it allows a class(child) to reuse properties and methods of another class (parent)


# Basic Syntax
class Parent:
    def speak(self):
        print("Person can speak")

class Child(Parent):
    def play(self):
        print("Child can play")


s = Child()
s.speak()  # Output: Person can speak
s.play()   # Output: Child can play



#  Inheritance with __int__ method

class Person:
    def __init__(self,name,section):
        self.name = name
        self.section = section


class Student(Person):
    def __init__(self,name,roll_no,section):
        super().__init__(name,section)  # calling parent class __init__ method
        self.roll_no = roll_no 
               

s = Student("Alice",101,"A")
print(s.name)      # Output: Alice
print(s.roll_no)   # Output: 101
print(s.section)   # Output: A



# Method Overriding = When a child class provides a specific implementation of a method that is already defined in its parent class.

class Person:
    def role(self):   # self is refrence to the actual object created from the class
        print("I am a Person")


class Student(Person):
    def role(self):
        super().role()  # calling parent class methoddef role(self):
        print("I am a Student")

s = Student()
s.role()  # Output: I am a Person
          #         I am a Student




#  MRO (Method Resolution Order) = It is the order in which Python looks for a method in a hierarchy of classes when it is called on an instance of a class.
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    def show(self):
        print("Class D")

d = D()
d.show()  # Output: Class D





