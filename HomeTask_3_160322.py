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

# reading txt-files function
def read_txt(file):
    with open(file, 'r', encoding='utf-8') as f:
        rt = f.readlines()
    return rt

# create sorted files dictionary
def files_dict():
    files_txt_dict = {}
    lf = list_files()
    for item2 in lf:
        files_txt_dict[item2] = len(read_txt(file=item2))
    list_txt_sort = dict(sorted(files_txt_dict.items(), key=lambda item: item[1]))
    return list_txt_sort

print(list_files())
print(read_txt('3.txt.txt'))
print(files_dict())