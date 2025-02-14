# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Bob', 12)
cat2 = Cat('Nob', 5)
cat3 = Cat('Tob', 8)

cats = [cat1, cat2, cat3]

for c in cats:
    print(f'{c.name} is {c.age} years old')

# 2 Create a function that finds the oldest cat


def findOldest(l):
    ages = []
    for c in l:
        ages.append(c.age)
    oldest = max(ages)

    for c in l:
        if c.age == oldest:
            print(f'{c.name} is the oldest cat, with {c.age} years')


findOldest(cats)
# print(oldest)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
