
name = "Vova"
age = 67
temperature = 36.6
email_for_vova = 'example@gmail.com'

my_info = {'name': name, 'age': age, 'temperature': temperature, 'email': email_for_vova}



a = {'name': "Volodymyr", 'age': 22 , 'my_temperature': 36.6, 'list': [122, 'Hello'],
     'extra_one': {'first': 1}, 67 :'sixty-seven' , 3.14: 'Pi', (1, 45): 'Hello'}

# keys CAN be integers , strings or float. Also we can use tuples
# but we CANT put list in object1


print(a)
print(my_info)
print(my_info.values())  # return only values but not keys
print(my_info.pop('name'))  # pops the key and value we need to delete
print(my_info.get('age'))  # get the key of value
print(my_info.update({'adress':'Ukraine'}))
print(my_info)
print(my_info.popitem())  # pops the LAST item in dictionary
print(my_info)
print(my_info.keys())  #shows all keys that are in your dictionary

