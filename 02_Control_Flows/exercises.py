print("-------- exercise 1 - if/else --------")
number = 2
if number % 2 == 0:
    print("even")
else:
    print("odd\n")

print("-------- exercise 2 - for loop --------")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)
print("\n")

print("-------- exercise 3 - while loop --------")
j = 10
while j > 0:
    print(j)
    j-=1
print("Start!")

print("-------- exercise 4 - for loop --------")
for i in range(1,100):
    if i % 3 == 0 and i % 7 == 0:
        print(i)
        break