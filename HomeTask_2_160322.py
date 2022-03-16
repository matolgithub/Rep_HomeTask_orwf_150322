# The cook_book method making
def cook_book(text_file):
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        while True:
            recipe_name = ''
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
        return cook_book

# Nice print method making
def print_book():
    print(f'It is nice cook-book printing:\n\n', 'cook_book = {')
    for i, j in cook_book('recipes.txt').items():
        print(f" '{i}' : [")
        for k in j:
            print(f'\t{k}')
        print('\t],')
    print('}\n', '(-_-)'*20)

# get_shop_list function
def get_shop_list_by_dishes(text_file, dishes, person_count):
    shop_list_by_dishes = {}
    shop_list = {}
    for i in dishes:
        for j, k in cook_book(text_file).items():
            if i == j:
                shop_list_by_dishes[j] = k 
    for l, n in shop_list_by_dishes.items():
        for p in n:
            meas_quant = {}
            meas_quant['measure'] = p['measure']
            meas_quant['quantity'] = int(p['quantity']) * person_count
            shop_list[p['ingredient_name']] = meas_quant
    return shop_list

print(get_shop_list_by_dishes('recipes.txt', ['Запеченный картофель', 'Омлет'], 2))