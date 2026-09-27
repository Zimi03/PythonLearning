print("------ exercise 1 ------")
class Instrument:
    def __init__(self, name):
        self.name = name

    def play(self):
        return f'I\'m playing {self.name}'

class Drums(Instrument):
    def __init__(self, name):
        super().__init__(name)
    
    def play(self):
        return "I'm hitting stuff with sticks"


piano = Instrument("piano")
print(piano.play())

drums = Drums("drums")
print(drums.play())

print("------ exercise 2 ------")

class Track:
    def __init__(self, title, author, duration_seconds):
        self.title = title
        self.author = author
        self.duration_seconds = duration_seconds

    def duration_seconds_to_mmss(self):
        minutes = self.duration_seconds//60
        seconds = self.duration_seconds-((self.duration_seconds//60)*60)
        result = f'{minutes}:{seconds:02d}'
        return str(result)

    def __str__(self):
        return f'''
author: {self.author}
title: {self.title}
duration: {self.duration_seconds_to_mmss()}
'''
    
track1 = Track("Something", "John", 130)
track2 = Track("Interesting", "Joanna", 345)
print(track1)
print(track2)

print("------ exercise 3 -------")
class Student:
    def __init__(self, name, level):
        self.name = name
        self._level = level

    def change_level(self, new_level):
        if new_level not in ["beginner", "intermediate", "advanced"]:
            raise ValueError(f"incorrect level")
        else:
            self._level = new_level

    def __str__(self):
        return f"name: {self.name}, level {self._level}"
        

student = Student("John", "beginner")
for level in ['xd', 'intermediate']:
    try:
        student.change_level(level)
    except ValueError as e:
        print(f"Error occured: {e}")
    finally:
        print(student)

print("------ exercise 4 ------")
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError ("not enough cash")
        else:
            self._balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest):
        super().__init__(owner, balance)
        self.interest = interest

    def __str__(self):
        return f'''
owner: {self.owner}
balance: {self._balance}
intrest: {self.interest}'''

    
    def charging_interest(self):
        self._balance += self._balance*self.interest

savings_account = SavingsAccount("Simon", 4000, 0.06)

print(savings_account)
savings_account.deposit(1000)
print(savings_account)
savings_account.charging_interest()
print(savings_account)