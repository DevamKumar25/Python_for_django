# Encapsulation =    It is the bundling of data and methods that operate on that data within one unit, typically a class.
#  It restricts direct access to some of the object's components.



# 📌 Purpose:

# Protect data
# Prevent misuse
# Control how data is accessed


# | Modifier  | Syntax   | Meaning                       |
# | --------- | -------- | ----------------------------- |
# | Public    | `name`   | Accessible everywhere         |
# | Protected | `_name`  | Use within class & subclasses |
# | Private   | `__name` | Name mangling (restricted)    |





# public member

class Student:
    def __init__(self,name):
        self.name = name # public member


    def show(self):
        print(self.name)


s = Student("Devam")
print(s.name)  # Accessing public member
s.show()



# protected member( _variable )

class Student:
    def __init__(self):
        self._roll_no = 101  # protected member


class College(Student):
    def show(self):
        print(self._roll_no)  # Accessing protected member within subclass  


c = College()
c.show()       



# private member ( __variable )

class Student:
    def __init__(self):
        self.__marks = 90  # private member


    def show_marks(self):
        print(self.__marks)  # Accessing private member within class


s = Student()
s.show_marks()  # Accessing private member via public method






#  Getters and setters (Controlled Access)
#  Getters are methods that retrieve the value of a private attribute.
#  Setters are methods that set or update the value of a private attribute.


class Student:
    def __init__(self,marks):
        self.__marks = marks  # private member

    def get_marks(self):          # getter method
        return self.__marks    

    def set_marks(self, marks):   # setter method
        if marks < 0:
            print("Invalid marks")
        else:
            self.__marks = marks

s = Student(85)
print(s.get_marks())  # Accessing private member via getter

s.set_marks(95)       # Modifying private member via setter
print(s.get_marks())