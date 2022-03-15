cook_book = {}
ingredient_list = []
recipe_name = ''
with open('recipes.txt', encoding='utf-8') as file:
    while True:
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
print(cook_book)