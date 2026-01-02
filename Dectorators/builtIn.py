#  @property = 
# It turns a method into an attribute Used for encapsulation and data hiding.


class Student:
    def __init__(self,marks):
        self.marks = marks

    def get_marks(self):
        return self.marks    


s = Student(85)
print(s.get_marks())  # Output: 85  



#    with using property decorator

class Student:
    def __init__(self,marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks    

s = Student(90)
print(s.marks)  # Output: 90    - look like an attribute access, but actually calls the method




class Student:
    def __init__(self,marks):
        self._marks = marks


    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,value):
        if value < 0:
            raise ValueError("Marks cannot be negative")
        self._marks = value


s = Student(75)
print(s.marks)  # Output: 75            

s.marks = -80
print(s.marks)  # Output: 80




# @staticmethod =
# It defines a method that does not receive an implicit first argument (neither self nor cls).
# It behaves like a regular function but belongs to the class's namespace.
# benefits - It can be called on the class itself without creating an instance.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(MathUtils.add(5, 3))        # Output: 8
print(MathUtils.multiply(4, 2))   # Output: 8        



#  @classmethod =
# It defines a method that receives the class itself as the first argument (cls) instead of the instance (self).
# It is used for factory methods or methods that need to access class-level data.   


class Person:
    school = "ABC High School"

    @classmethod
    def change_school(cls,name):
        cls.school = name


Person.change_school("XYZ High School")
print(Person.school)  # Output: XYZ High School



| Decorator       | First arg | Access   | Use case             |
| --------------- | --------- | -------- | -------------------- |
| `@property`     | `self`    | Instance | Controlled attribute |
| `@staticmethod` | none      | Class    | Utility logic        |
| `@classmethod`  | `cls`     | Class    | Class-level logic    |
