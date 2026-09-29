print("------ exercise 1 ------")
instruments = ["Drums", "Piano","Bass","Guitar"]
iterator = iter(instruments)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("------ exercise 2 ------")
def count_down(n):
    for i in range(n,0,-1):
        yield i
    yield "Start"


for i in count_down(3):
    print(i)

for i in count_down(5):
    print(i)

print("------ exercise 3 ------")
def even_up_to(n):
    for i in range(2, n+1, 2):
        yield i

for i in even_up_to(12):
    print(i)

print("------ exercise 4 ------")
import sys
sys.path.insert(0, "../07_Modules_Files")
import tools

SECONDS = [65, 130, 200, 45, 300]
def format_seconds():
    for time in SECONDS:
        yield tools.seconds_to_mmss(time)

for i in format_seconds():
    print(i)

mmss = list(i for i in format_seconds())
print(mmss)
mmss_list = [i for i in format_seconds()]
print(mmss_list)