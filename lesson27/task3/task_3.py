"""
Создайте пустую директорию mydir в текущей рабочей директории.
Затем перейдите в эту директорию и создайте в ней три пустых файла:
file1.txt, file2.txt и file3.txt.
Наконец, выведите список файлов в директории на экран.
"""

import os

def create_dir(name: str):
    script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(script_path)
    folder_path = os.path.join(script_directory, name)
    
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    
    return folder_path

def create_files(path: str, name: str, count: int):
    if os.path.exists(path):
        for i in range(count):
            file_name = name + str(i + 1) + ".txt"
            file_path = os.path.join(path, file_name)

            with open(file_path, 'w') as _:
                pass

def show_files_in(path: str):
    if os.path.exists(path):
        files = os.listdir(path)
        for file in files:
            print(file)

def main():
    dir_name = 'mydir'
    file_name = 'file'

    dir_path = create_dir(dir_name)
    create_files(dir_path, file_name, 3)
    show_files_in(dir_path)

if __name__ == "__main__":
    main()