print("---------------- exercise 1 - list ----------------")
bands = ["band1", "band2", "band3", "band4", "band5"]
print(bands)
bands.append("band6")
print(bands)
bands.pop(0)
print(bands)

print("---------------- exercise 2 - dictionary ----------------")
student = {
    "name": "John",
    "age" : 15,
    "level": "beginner"
}

for k, v in student.items():
    print(f'key: {k}, value: {v}')

print("---------------- exercise 3 - set ----------------")
grades = [5,4,5,3,4,4,2,5]
print(sorted(set(grades)))

print("---------------- exercise 4 - tuple ----------------")
coordinates = (10, 20)
# coordinates[0] = 5 -> cannot do - tuples are immutable
for item in coordinates:
    print(item)