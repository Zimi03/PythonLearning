print("------- exercise 1 - variables and fstring --------")
name = "Random"
age = 18
height = 1.72
plays = True
print(f'name: {name}\nage: {age}\nheight: {height}\nplays: {plays}\n')


print("------- exercise 2 - type conversion --------")
age_str = "27"
print(f'{int(age_str)+5}\n')


print("------- exercise 3 - type() function --------")
print(type(10))
print(type(10.5))
print(type("10"))
print(type(True))
print(type(10==10))
print("\n")

print("------- exercise 4 - type error--------")
number_int = int("5") + 5 
string = "5" + str(5)
print(number_int)
print(string)
