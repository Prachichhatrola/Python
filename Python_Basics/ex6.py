def highest_even(l):
    for i in l:
        if i % 2 != 0:
            l.remove(i)
    return max(l)


print(highest_even([10, 2, 3, 4, 8, 11]))
