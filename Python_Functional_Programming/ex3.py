from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(item):
    return item.upper()


capitalized = list(map(capitalize, my_pets))
print(capitalized)


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

order = list(zip(my_strings, sorted(my_numbers)))
print(order)


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def over_50(item):
    return item > 50


filtered = list(filter(over_50, scores))
print(filtered)


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item


total = reduce(accumulator, (my_numbers + scores))
print(total)
