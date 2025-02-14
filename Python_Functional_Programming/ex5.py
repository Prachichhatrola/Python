some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

duplicates = list(
    set([value for value in some_list if some_list.count(value) > 1]))

print(duplicates)
