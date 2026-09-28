print("------ exercise 1 ------")
import tools

print(tools.seconds_to_mmss(120))
print(tools.seconds_to_mmss(150))
print(tools.seconds_to_mmss(382))

print(tools.is_even(2))
print(tools.is_even(0))
print(tools.is_even(1))

print("------- exercise 2 ------")
with open("note.txt", "w") as file:
    file.write("PE\n")
    file.write("Math\n")
    file.write("Literature\n")

with open("note.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line.strip()}")

print("------- exercise 3 -------")
with open("note.txt", "a") as file:
    file.write("Computer science\n")

with open("note.txt", "r") as file:
    file_content = file.read()
    print(file_content)


print("------- exercise 4 ------")
def safe_read(file_name):
    try:
        with open(str(file_name), "r") as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"file: {file_name} not found") 
        return None

file_content = safe_read("note.txt")
print(file_content)
file_content = safe_read("something.txt")
print(file_content)