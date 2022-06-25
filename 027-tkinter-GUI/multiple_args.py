
# many positional args
def add(*args):  
    print(type(args)) #tuple 
    total = 0
    for n in args:
        total+=n
    print(total)

add(1,2,3)

# many keyword args
def calculate(n, **kargs):
    print(type(kargs)) # dict
    # for key, value in kargs.items():
    #     print(key)
    #     print(value)

    n += kargs["add"]
    n *= kargs["multiply"]
    print(n)        

calculate(2, add=3,multiply=5)


class Car:
    def __init__(self, **kw) :
        self.make = kw.get("make")
        self.color = kw.get("color")
        
my_car = Car(make="Nissan")
print(my_car.make)
