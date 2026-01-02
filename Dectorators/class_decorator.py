# Class-based decorator for functions: stores the function in __init__
# and adds behavior when the function is called via __call__.



class LoggerDecorator:
    def __init__(self, func):
        # store the wrapped function
        self.func = func

    def __call__(self, *args, **kwargs):
        # additional behavior (logging) before calling the function
        print(f"Arguments: {args}, keyword Arguments: {kwargs}")
        # call and return the original function's result
        return self.func(*args, **kwargs)

# Note: this is a function decorator implemented as a class, not a class decorator.
@LoggerDecorator
def greet(name, greeting="Hello"):
    """Return a greeting for name."""
    return f"{greeting}, {name}!"

# Usage
print(greet("Alice"))
print(greet("Bob", greeting="Hiii"))

# Expected output:
# Arguments: ('Alice',), keyword Arguments: {}
# Hello, Alice!
# Arguments: ('Bob',), keyword Arguments: {'greeting': 'Hiii'}
# Hiii, Bob!




class DOubleReturnDecorator:
    def __init__(self,func):
        self.func = func

    def __call__(self,*args,**kwargs):
        result = self.func(*args,**kwargs)
        return result*2


@DOubleReturnDecorator
def add(a,b):
    return a+b

print(add(3,4))  # Output: 14       
print(add(5,7))  # Output: 24