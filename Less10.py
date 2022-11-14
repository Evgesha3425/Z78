# s1 = 'hello'
# s2 = 'мир'
#
#
# encoded = s2.encode("windows-1251")
# print(encoded)

"""
Файлы. Открытие, редактирование.
"""

# r - read - считываем из файла
# w - write - записываем в файл (все что было стерлось)
# a - append - дозапись в файл (добавит в конец файла каку-то информацию)
# x - - создаст файл для записи, если его не существует
# b - binary -бинарный файл (закодированные файлы)
# + - concatenate - r+ - w+ - a+ -

# file = open('name.txt', 'a', encoding="utf-8")
# file.write("Паша" + "\n")
# file.close()

# file = open("/home/yauheni/pythonProject/name.txt", "r")
# names = file.read()
# print(names.replace("\n", " ").rstrip())

# names = file.readlines()
# names = [name.rstrip() for name in names]
# print(names)

# for line in file:
#     print(line.rstrip())
#
# file.close()

# with open("name.txt", "r", encoding="utf-8") as file:
#     names = {}
#     for line in file:
#         lst = line.rstrip().split()
#         names[lst[0]] = int(lst[1])
# print(names)
# print(sum(names.values())/len(names))


"""
Файлы csv() - comma separeted values - разделенные сепаратором(запятой) значения
"""

# import csv
# import random
# with open("marks.csv", "w", encoding="utf-8") as file_csv:
#     for j in range(10):
#         file_csv.write(",".join([str(random.randint(1, 10)) for i in range(10)]) + "\n")


# with open("marks.csv", "r", encoding="utf-8") as file_csv:
#     lst = csv.reader(file_csv, delimiter=',')
#     data_csv = []
#     lst = [data_csv.extend(data) for data in lst]
#     print(list(map(int, data_csv)))

"""
json
"""

# import json

# some_lst = [54, "hello", 231]
#
# serialized = json.dumps(some_lst)
# new_lst = json.loads(serialized)
#
# print(some_lst)
# print(new_lst)
#
#
# # costumers = {"Vasya": 421, "Petya": 1000, "Anna": 402}
# # with open("costumers.json", "w", encoding="utf-8") as file_json:
# #     file_json.write(json.dumps(costumers, indent=4))
#
#
# with open("costumers.json", "r", encoding="utf-8") as file:
#     info = json.load(file)
#     info["Kirill"] = 123
#     print(info)
#
# with open("costumers.json", "w", encoding="utf-8") as file:
#     file.write(json.dumps(info, indent=4))
