set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#set_1.remove(8)
x = 'remove 8'
y = x.split()[0] #+ (x.split()[1])
#set1 = f'set_1.{x.split()[0]}({x.split()[1]})'  #.format(x.split()[0], x.split()[1])
exec(f'set_1.{x.split()[0]}({x.split()[1]})')
print(set_1)
