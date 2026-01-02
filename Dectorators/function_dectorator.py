#  A function decorator is a special type of decorator that takes another
   # function as an argument and adds extra behavior to it without modifying it and returns a new function.


def my_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")
    
say_hello()
