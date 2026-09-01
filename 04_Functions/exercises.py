print("------------ exercise 1 ----------")

def is_even (number):
    return number % 2 == 0

print (is_even(2))
print (is_even(1))
print (is_even(0))
print (is_even(13))

print("------------ exercise 2 ----------")
def rectangle_area (height, length = 1):
    return length*height

print(rectangle_area(4))
print(rectangle_area(2,4))

print("------------ exercise 3 ----------")
def mean(*liczby):
    return sum(liczby)/len(liczby)

print(mean(1,2,3,4))
print(mean(312,124,542))
print(mean(1,2,3,4,5,6,7,8,210))

print("------------ exercise 4 ----------")
def student_overview(**data):
    for k, v in data.items():
        print(f'{k}: {v}')

student_overview(name="John", age = 18, level="beginner")
student_overview(name = "Anthony", age = 28)