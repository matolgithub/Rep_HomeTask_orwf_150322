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

# All cook-book printing
print(f'It is simple all cook-book printing:\n\n{cook_book("recipes.txt")}\n', '(-_-)'*20, '\n')

# Nice print method making
def print_book():
    print(f'It is nice cook-book printing:\n\n', 'cook_book = {')
    for i, j in cook_book('recipes.txt').items():
        print(f" '{i}' : [")
        for k in j:
            print(f'\t{k}')
        print('\t],')
    print('}\n', '(-_-)'*20)

# Nice cook-book printing
print_book()