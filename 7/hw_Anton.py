class Data:
    
    def __init__(self, full_name, email, file_name, color) -> None:
        self.__fullname = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color
    string = []
    @property
    def full_name(self):
        return self.__fullname
    @full_name.setter
    def fullname(self, value):
        self.__fullname = value
        
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name
    @email.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, value):
        self.__color = value
new_line = []
spisok_obj = []
otherinfo = ""
with open(r"C:\Users\Антон\Desktop\Geeks\ДЗ_2_месяц\7\MOCK_DATA.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        a = line.split()
        # print(a)
        name1 = a[0]; surname1 = a[1]; fullname = name1+" "+surname1
        a[0] = fullname
        a[1] = a[3]
        a[3] = a[4]
        # print(a)
        obj= Data(a[0],a[1],a[2],a[3])
        spisok_obj.append(obj)
    
        my_file1 = open("Фамилии и имена.txt", "w+")
        for i in spisok_obj:
            my_file1.write(str(i.full_name)+'\n')
        my_file1.close()

        my_file2 = open("Почта.txt", "w+")
        for i in spisok_obj:
            my_file2.write(str(i.email)+'\n')
        my_file2.close()

        my_file3 = open("Названия файлов с расширением.txt", "w+")
        for i in spisok_obj:
            my_file3.write(str(i.file_name)+'\n')
        my_file3.close()

        my_file4 = open("Коды цветов.txt", "w+")
        for i in spisok_obj:
            my_file4.write(str(i.color)+'\n')
        my_file4.close()
