for item in 'Hello':
    print(item)

for item in range(5):
    print(item)


names = ['Sergiy', 'Sasha', 'Volodymyr'] ;

for name in names:
    if name == 'Volodymyr':
        print(f'{name} is me!')
        for name in names:
            print('Im inside the if clause')
    else:
        print(f'Hello, {name}')



