cook_book = {}
recipe_name = ''
with open('recipes.txt', encoding='utf-8') as file:
    while True:
        ingredient_list = []
        recipe_name = read_data = file.readline().strip()
        sum_ingr = read_data = file.readline().strip()
        for i in range(int(sum_ingr)):
            ingr_dict = {}
            read_data = file.readline()
            ingr_dict['ingredient_name'] = read_data.split('|')[0].strip()
            ingr_dict['quantity'] = read_data.split('|')[1].strip()
            ingr_dict['measure'] = read_data.split('|')[2].strip()
            ingredient_list.append(ingr_dict)  
            cook_book[recipe_name] = ingredient_list 
        read_data = file.readline()    
        if read_data == '\n':
            continue
        else:
            break
print('cook_book = {')
for i, j in cook_book.items():
    print(f" '{i}' : [")
    for k in j:
        print(f'\t{k}')
    print('\t],')
print('}')