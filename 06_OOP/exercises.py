print("------ exercise 1 ------")
class Track:
    def __init__(self, title, author, duration_seconds):
        self.title = title
        self.author = author
        self.duration_seconds = duration_seconds

    def duration_seconds_to_mmss(self):
        minutes = self.duration_seconds//60
        seconds = self.duration_seconds-((self.duration_seconds//60)*60)
        result = f'{minutes}:{seconds:02d}'
        return result

    def information(self):
        print(f'author: {self.author}')
        print(f'title: {self.title}')
        print(f'duration: {self.duration_seconds_to_mmss()}')

track1 = Track("Something", "John", 130)
track2 = Track("Interesting", "Joanna", 345)
track1.information()
track2.information()

print("------ exercise 2 ------")
class Student:
    

    def __init__(self, name, age, level):
        self.name = name
        self.age = age
        self.level = level
        self.hours_played = 0

    def practise(self, session_duration):
        self.hours_played += session_duration
        if self.hours_played > 10:
            self.level = "Intermediate"

student1 = Student("John", 15, "Beginner")
student2 = Student("Anthony", 25, "Intermediate")
student2.hours_played = 10.5

student1.practise(0.5)
student1.practise(1.5)
student1.practise(2)

student2.practise(1)
student2.practise(3)
student2.practise(0.5)

print(f'student 1 has practised for {student1.hours_played} hours his level is {student1.level}')
print(f'student 2 has practised for {student2.hours_played} hours his level is {student2.level}')

student1.practise(2.5)
student1.practise(3)
student1.practise(1)

print(f'student 1 has practised for {student1.hours_played} hours his level is {student1.level}')

print("------ exercise 3 ------")
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError ("not enough cash")
        else:
            self.balance -= amount


bank_account = BankAccount("John", 1000)
bank_account.deposit(2000)
print(f'balance1 is {bank_account.balance}')
for amount in [100, 3500]:
    try:
        bank_account.withdraw(amount)
    except ValueError as e:
        print(f'error occured: {e}')
    print(f'balance is {bank_account.balance}')
