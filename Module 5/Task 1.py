import random

numberofdice = int(input("How many dice would you like to roll? "))
sum_ = 0
for i in range(numberofdice):
    roll = random.randint(1, 6)
    sum_ += roll

print(f"The sum of the rolls is: {sum_}")