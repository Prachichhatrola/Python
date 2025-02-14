some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

new_list = []

for i in some_list:
    if i not in new_list:
        new_list.append(i)

print(some_list)
print(new_list)
