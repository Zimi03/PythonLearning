print("------ exercise 1 -------")

def first_half():
    yield 1 
    yield 2 
    yield 3 

def second_half():
    yield 4
    yield 5
    yield 6

def all_data():
    yield from first_half()
    yield from second_half()

for i in all_data():
    print(i)

print("------ exercie 2 ------")

def count_from(start):
    while True:
        yield start
        start += 1

start = 0

for x in count_from(start):
    print(x)
    if x == 5:
        break

print("------ exercise 3 ------")
import itertools

numbers = itertools.islice(count_from(10), 5)
for number in numbers:
    print(number)

print("------ exercise 4 ------")
DRUMS = ["Kick", "Snare", "Tom"]

def cymbals():
    yield "Hi-hat"
    yield "Crash"
    yield "Ride"
    yield "Splash"

def drum_instruments():
    yield from DRUMS
    yield from cymbals()

for x in drum_instruments():
    print(x)