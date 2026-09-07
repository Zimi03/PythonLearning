print("------ exercise 1 ------")

value = input("Enter value: \n")
try:
    number = int(value)
except ValueError:
    print("Cannot convert to int")

print("------ exercise 2 ------")

def division (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("cannot divide by 0")
        return None

quotient_1 = division(5,0)
quotient_2 = division(5,5)

print(quotient_1)
print(quotient_2)

print("------ exercise 3 ------")

def convert_str_to_int(text):
    try:
        number = int(text)
        print(number)
    except ValueError:
        print("Cannot convert to int")
    else:
        print("convertion success")
    finally:
        print("attempt finished")

convert_str_to_int("1")
convert_str_to_int("abc")

print("------ exercise 4 ------")
def check_age(age):
    if age < 0 or age > 130:
        raise ValueError (f"incorrect age: {age}")
    print(age)
    return age
ages = [-1,15,150]
for age in ages:
    try:
        check_age(age)
    except ValueError as e:
        print(f'error occured:{e}')
