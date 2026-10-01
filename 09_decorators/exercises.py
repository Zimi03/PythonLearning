print("------ exercise 1 ------")
def log_call(fun):
    def internal():
        print(f"Calling: {fun.__name__}")
        fun()
    return internal

@log_call
def greet():
    print(f"Welcome")

greet()

print("------ exercise 2 ------")
import time
def count_time(fun):    
    def wrapper(*args, **kwargs):
        start = time.time()
        fun()
        stop = time.time()    
        print(f"{stop - start}")
    return wrapper

@count_time
def count():
    for i in range(100000000):
        continue
    return

count()

print("------ exercise 3 ------")
def only_positive(fun):
    def wrapper(*args):
        for num in args:
            if num <= 0:
                raise ValueError("Value of side must be positive")
        wynik = fun(*args)
        return wynik
    return wrapper

@only_positive
def area_of_rectangle(a,b):
    return a * b

for pairs in ((-4,4),(3,4)):
    try:
        area = area_of_rectangle(pairs[0],pairs[1])
        print(area)
    except ValueError as e:
        print(f"error occured: {e}")

print("------ exercise 4 ------")
def count_calls(fun):
    
    def wrapper():
        fun()
        wrapper.counter += 1
        print(wrapper.counter)
    wrapper.counter = 0
    return wrapper

@count_calls
def speak():
    print("Mellon")


speak()
speak()
speak()
speak()