from decimal import Decimal

#accept real input
val = input('Enter real value here: ')

selector = int(input('''
    Select option 1 to 5:
    option 1 -> all layers
    option 2 -> all layers
    option 3 -> all layers
    option 4 -> all layers
    option 5 -> all layers
'''))

if selector == 1:
    print('All LAYERS SELECTED')
    #separate the real number
    val = val.split('.')

    #print the integer part of the the real value
    layer1 = float(val[0])
    print('First layer:', layer1) #first layer

    #begin processing of the decimal part
    val2 = '0.'+val[1]

    #the second layer
    layer2 = val2[0:4] + '0000'
    new_layer2 = Decimal(layer2)
    print('Second layer:', new_layer2)

    #third layer
    layer2 = val2[0:2] + '00' + val2[4:6] + '00'
    new_layer2 = Decimal(layer2)
    print('Third layer:', new_layer2)

    #fourth layer
    layer2 = val2[0:2] + '0000' + val2[6:8]
    new_layer2 = Decimal(layer2)
    print('Fourth layer:', new_layer2)
elif selector == 2:
    print('FIRST LAYER SELECTED')
    #separate the real number
    val = val.split('.')

    #print the integer part of the the real value
    layer1 = float(val[0])
    print('First layer:', layer1) #first layer
elif selector == 3:
    print('SECOND LAYER SELECTED')
    #the second layer
    layer2 = val2[0:4] + '0000'
    new_layer2 = Decimal(layer2)
    print('Second layer:', new_layer2)
elif selector == 4:
    print('THIRD LAYER SELECTED')
    #third layer
    layer2 = val2[0:2] + '00' + val2[4:6] + '00'
    new_layer2 = Decimal(layer2)
    print('Third layer:', new_layer2)
else:
    print('FOURTH LAYER SELECTED')
    #fourth layer
    layer2 = val2[0:2] + '0000' + val2[6:8]
    new_layer2 = Decimal(layer2)
    print('Fourth layer:', new_layer2)