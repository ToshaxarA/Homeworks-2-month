import re

class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        self.__full_name = full_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self):
        self.__email = email

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name):
        self.__file_name = file_name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


datas = []

with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    for i in content:
        datas.append(Data(re.findall(r"^[a-zA-Z-'.\\]+[\s\t][a-zA-Z-'.\\]+[\s\t]", i)[0],
                          re.findall(r"[a-zA-Z0-9-_\\]+@[a-zA-Z0-9-_\\.]+", i)[0],
                          re.findall(r"[a-zA-Z0-9\\_-]+.[a-zA-Z0-9]+",
                                     re.findall(r"[a-zA-Z0-9\\_-]+.[a-zA-Z0-9]+[\t\s]#", i)[0])[0],
                          re.findall(r"#[a-zA-Z0-9\\_-]+", i)[0]))

files = [open('full_names.txt', 'w'), open('emails.txt', 'w'), open('file_names.txt', 'w'), open('colors.txt', 'w')]
for i in datas:
    files[0].write(i.full_name + '\n')
    files[1].write(i.email + '\n')
    files[2].write(i.file_name + '\n')
    files[3].write(i.color + '\n')

for i in files:
    i.close()
