#Unlimited (positional) arugments

def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(1,2,3,4,5,6,7,8,9,10)

#Many Keyword Arguments

def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    n=+ kwargs['add']
    n*= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply = 5)
#output in a dictionary, which represents each keyword argument and it's value. 

class Car:
    def __init__(self, **kw) -> None:
        self.make=kw.get["make"]
        self.model = kw.get['model']
        #benefit of get, is that if it is note called, it will return none as the value of the keyword. 

my_car = Car(make="Nissan", model="GT-R")

print(my_car.model, my_car.model)