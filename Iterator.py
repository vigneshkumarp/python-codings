my_list = [4, 7, 0, 3]
my_iter = iter(my_list) # get an iterator using iter()
print(next(my_iter))
print(next(my_iter))

print(my_iter.__next__())
print(my_iter.__next__())
next(my_iter)
