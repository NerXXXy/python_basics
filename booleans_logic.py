a = 3
b = 4
c = 5



print(f"{True and True}")  # true
print(f'{True and False}')  # false  because 1 of statements is false
print(f'{False and False}')  # false

print(f'{True or False}')  # true   because 1 of 2 statements is true
print('_____________')

print(a == 3 and b == 4)
print(a == 3 and b == 4 and c == 5)
print((a == 3 or b == 555) and c == 555)  # false
print(a == 3 or (b == 555 and c == 555))  # true