"""
Создайте шаблон template.html, 
который будет содержать HTML-код для отображения списка пользователей.
Шаблон должен использовать цикл for для перебора элементов списка,
и выводить имя и email каждого пользователя. 
Затем создайте список пользователей в виде списка словарей,
передайте его в шаблон и отобразите результат на экране.
"""

import os
from jinja2 import Template

conf_name = 'user_list.conf'
tmpl_name = 'template.html'
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
tmpl_data = {
    "title": "User list",
    "user": "admin",
    "users": [
        { "name": "Ivan", "mail": "ivan@gmail.com" },
        { "name": "Igor", "mail": "igor@gmail.com" },
        { "name": "Olya", "mail": "olya@gmail.com" }
    ]
}

def main():  
    file_path = os.path.join(script_directory, tmpl_name)

    with open(file_path, 'r') as file:
        template = Template(file.read())
        list_conf = template.render(**tmpl_data)

        list_conf_path = os.path.join(script_directory, conf_name)
        with open(list_conf_path, 'w') as conf:
            conf.write(list_conf)

if __name__ == "__main__":
    main()