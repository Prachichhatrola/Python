class SuperList(list):
    def __len__(self):
        return 100


my_list = [1, 2, 3,]
new_list = SuperList()
new_list.append(5)

print(my_list)
print(len(my_list))

print(new_list)
print(len(new_list))
