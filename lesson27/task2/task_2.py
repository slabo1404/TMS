"""
Создайте файл test.txt и запишите в него строку 
"Это тестовый файл для домашнего задания по программированию". 
Затем откройте этот файл в режиме чтения, прочитайте его содержимое и выведите на экран.
"""

import os

def create_file(name: str, text: str):
    script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(script_path)

    file_path = os.path.join(script_directory, name)

    with open(file_path, 'w') as file:
        file.write(text)
    
    return file_path

def read_file(path: str):
    with open(path, 'r') as file:
        return file.read()

def main():
    text = 'Это тестовый файл для домашнего задания по программированию'
    file_name = 'file.txt'

    file_path = create_file(file_name, text)

    content = read_file(file_path)
    print(content)

if __name__ == "__main__":
    main()

