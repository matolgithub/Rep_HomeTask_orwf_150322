import os

# Function for analize path and files in catalog
def path_dir_files():
    path_files = os.getcwd()
    dir_files = os.listdir()

# To create list with txt-files
def list_files():
    list_txt_files = []
    for item1 in os.listdir():
        if '.txt' in item1:
            list_txt_files.append(item1)
    return list_txt_files

# Reading txt-files function
def read_txt(file):
    with open(file, 'r', encoding='utf-8') as f:
        rt = f.readlines()
    return rt

# Create sorted files dictionary
def files_dict():
    files_txt_dict = {}
    lf = list_files()
    for item2 in lf:
        files_txt_dict[item2] = len(read_txt(file=item2))
    dict_txt_sort = dict(sorted(files_txt_dict.items(), key=lambda item: item[1]))
    return dict_txt_sort

# Create total_file.txt function
def total_file():
    with open('total_file.txt', 'w', encoding='utf-8') as f1:
        for item3, item4 in files_dict().items():
            if item3 == 'total_file.txt':
                continue
            f1.write(f'{item3}\n')
            f1.write(f'{item4}\n')
            with open(str(item3), 'r', encoding='utf-8') as f2:
                f1.write(f'{f2.read()}\n')

# Test results
# print(list_files())
# print(read_txt('2.txt.txt'))
# print(files_dict())
# total_file()