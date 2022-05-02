def linearSearch(item,my_list):
    found = False
    position = 0
    while position < len(my_list) and not found:
        if my_list[position]==item:
            found = True
        position = position + 1
    return found
bag = ['libro','lápiz','pluma','libreta','marcador','regla']
item = input('Que articulo quieres revisar de la mochila?')
itemFound = linearSearch(item,bag)
if itemFound:
    print('Si,El aritculo esta en la mochila')
else:
    print('No,El articulo no esta en la mochila')