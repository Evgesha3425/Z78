"""
1. Вашей задачей будет восстановление исходной строки обратно. Напишите программу, которая считывает из файла строку,
соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Для решение вам необходимо открыть файл для чтения 1.txt .
"""

# file = open("1.txt", "r", encoding="utf-8")
# text = file.read()
# encoding_text = ''
# num = ''
# for symbol in range(len(text)-1):
#     if text[symbol].isalpha():
#         continue
#     if text[symbol].isdigit():
#         num += text[symbol]
#         if text[symbol+1].isdigit():
#             continue
#         else:
#             encoding_text += text[symbol-len(num)] * int(num)
#             num = ''
# print(encoding_text.title())
# file.close()

"""
2. Список товаров, имеющихся на складе, включает в себя наименование товара, количество единиц товара, цену единицы 
и дату поступления товара на склад. Вывести список товаров, хранящихся больше месяца и стоимость которых 
превышает 1 000 000 р.
"""

# from datetime import datetime, timedelta
# import csv
#
#
# with open("2.csv", "r", encoding="utf-8") as file_csv:
#     reader = csv.reader(file_csv)
#
#     for line in reader:
#         date_product = datetime.strptime(line[3], "%Y-%m-%d")
#         if date_product + timedelta(days=30) >= datetime.now() and int(line[1]) * int(line[2]) > 1000:
#             print(line)


"""
3. Написать программу “Викторина”. У вас есть 2 файла. В первом содержаться 10 вопросов(каждый вопрос в своей строке) 
во втором 10 ответов( каждый ответ как и вопрос в своей строке). Вам нужно считывать по 1 вопросу из файла с вопросами 
и давать на них ответ. Если ответ верный, добавлять к счётчику верных ответов 1 балл. В конце программа выводит 
количество верных ответов на вопросы.
"""

# file1 = open("3_1.txt", "r", encoding="utf-8")
# file2 = open("3_2.txt", "r", encoding="utf-8")
# questions = file1.readlines()
# answer = file2.readlines()
# counter = 0
#
# for i in range(len(questions)):
#     print(questions[i].replace('\n', ' '))
#     ask = input('Введите ваш ответ: ')
#     if ask == str(answer[i].rstrip()):
#         counter += 1
#
# print(f'Правильных ответов {counter} из 10.')
# file1.close()
# file2.close()

"""
4. Создать словарь в качестве ключа которого будет 5-ти значное число, а в качестве значений кортеж состоящий из 
2-ух элементов – имя(str) и возраста(int). Сделать 5-6 элементов словаря и записать данный словарь на диск в файл 
json формата
"""

# import json
# my_dict = {
#     12345: ('Yauheni', 25,),
#     23456: ('Denis', 30,),
#     34567: ('Anna', 35,),
#     87654: ('Victor', 40,),
#     98765: ('Nastya', 45,),
# }
# with open("4.json", "w", encoding="utf-8") as file_json:
#     file_json.write(json.dumps(my_dict, indent=4))


"""
5. Прочитать сохранённый json – файл и записать данные на диск в csv файл. Первое значение каждой строки должно 
начинаться со слова person, значения разделить ;
"""

# import json
# import csv
#
#
# file_json = open("4.json", "r", encoding="utf-8")
# text = json.load(file_json)
#
# with open("5.csv", "w", encoding="utf-8") as file_csv:
#     for key, values in text.items():
#         file_csv.write('person' + ';' + key + ';')
#         file_csv.write(values[0] + ';' + str(values[1])+ '\n')
#
#
# file_json.close()

