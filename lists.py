a = [1, 10, 3, 4, 10.123, "hello", [44, 55, [99, 120]]]

print(a.index(3))  # returns the index of item you search

# a.reverse()  #  reverse your list

a.pop(4)  #  pops the item from list. To choose item you need to know the index of it

a.append(99)  # adds item to your list at last index (if you need only ONE item)

print(a.count(1))  # calculates the number of items are calculated in your list

a += [44, 55, 66]  # we added new items to our list (min 2+ items)

print(a[5][0])  # here we get 44 (list in list)
print(a[5][2][0])  # here we get 99 (list in list in list)


print(a)

if 10 in a:    # if there is item 10 in list
    print('10 is in list a')