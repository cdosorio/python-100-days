# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__} {args}")
        print(f"It returned {function(*args)}")
    return wrapper


# Use the decorator 👇
@logging_decorator
def add(*args):      
    total = 0
    for n in args:
        total+=n
    return total

add(1,2,3)