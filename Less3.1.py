# Первая задача !!!
# string = input()
# summ= 0
# pr = 1
# count1, count2 = 0, 0
# for i in string:
#     if int(i) % 2 == 0:
#         summ += int(i)
#         count1 += 1
#     else:
#         pr *= int(i)
#         count2 += 1
# if count1 > count2:
#     print('Сумма четных чисел равна:', summ)
# elif count1 < count2:
#     print('Произведение нечетных чисел равно:', pr)
# else:
#     print('Сумма четных чисел равна:', summ)
#     print('Произведение нечетных чисел равно:', pr)



# Вторая задача !!!
# string = input()
# count1, count2 = 0, 0
# a = 'аиеёоуыэюя'
# for letter in string:
#     if letter in a:
#         count1 += 1
#     else:
#         count2 += 1
# if count1 == count2:
#     print(string)
# else:
#     print('Гласных букв:', count1, 'согласных букв:', count2)



# Третья задача !!!
# from random import randint
# a, b = int(input()), int(input())
# array = []
# count1 = 0
# count2 = 0
# for i in range(7):
#     c = randint(1, 20)
#     d = randint(1, 20)
#     if i == 4:
#         array.append(c)
#         array.append(d)
#     if a > c and b > d:
#         count1 += 1
#     elif a < c and b < d:
#         count2 += 1
# if count1 == count2:
#     print(array)
# else:
#     if count2 == 0:
#         print('Все числа введенные с клавиатуры больше')
#     elif count1 == 0:
#         print('Все случайные числа больше')
#     else:
#         print('В', count1 / count2, 'раз числа введеные с клавиатуры больше')



# Четвертая задача !!!
# from random import randint
# n = int(input('Введите сколько раз будем проверять: '))
# a = input('Введите ваше число: ')
# counter = 0
# for _ in range(n):
#     b = randint(1, 9)
#     if str(b) in a:
#         counter += 1
# print('Случайное число встречается', counter, 'раз')



# Пятая задача !!!
# string = input('Введите любую строку: ')
# array = []
# for i in string:
#     if i.isdigit():
#         print(i, end=' ')



# Шестая задача !!!
# string = input()
# counter1 = 0
# counter2 = 0
# counter3 = 0
# counter4 = 0
# counter5 = 0
# vowels = 'аиеёоуыэюя'
#
# for i in range(0, len(string) - 1):
#     if string[i].islower() and string[i+1].islower():
#         counter1 += 1
#     elif string[i].isupper() and string[i+1].isupper():
#         counter2 += 1
# for j in range(len(string)):
#     if string[j].lower() in vowels:
#         counter3 += 1
#         counter5 += 1
#     else:
#         counter4 += 1
#         counter5 += 1
#
# print(f'Пар нижнего регистра - {counter1} , верхнего - {counter2}')
# print(f'Гласных букв - {counter3} , согласных - {counter4}')
# print(f'Всего букв в слове - {counter5} ')

