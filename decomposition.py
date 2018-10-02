#accept the real number
val = float(input('Enter the real value: '))

#separating the integer from the real value
i, d = divmod(val, 1)

#first layer
#print('First layer:', i)

#second layer
val2 = str(d.split())
print(val2)
#print(d)
