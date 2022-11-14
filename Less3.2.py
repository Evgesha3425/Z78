"""
1. Ввести предложение состоящее из двух слов. Поменять местами слова, добавить восклицательный знак в начало и конец,
слова разделить 3 символами (пробел, восклицательный знак и еще пробел), вывести итоговое предложение на экран.
Задание необходимо выполнить 3-мя разными способами форматирования.
"""

# Сделал только одним способом
# string = 'привет друг'
# print(string[string.find(' ')+1:], '!', string[:string.find(' ')])


"""
2. Написать программу, которая получит имя и возраст пользователя, проверяет возраст и выдает приветственное 
сообщение в зависимости от возраста: 
* меньше нуля или ноль или не число: "Ошибка, повторите ввод";
* больше нуля до 10 не включая: "Привет, шкет #Имя#";
* от 10 до 18 включая: "Как жизнь #Имя#?";
* больше 18 и меньше 100: "Что желаете #Имя#?";
* в противном случае: "#Имя#, вы лжете - в наше время столько не живут..."

3. Завернуть это в вечный цикл
"""

# name = input('Введите имя: ')
# while True:
#     age = input('Введите возраст: ')
#     try:
#         age = int(age)
#     except ValueError:
#         print('Ошибка. Повторите ввод.')
#         continue
#     if 0 < age < 10:
#         print(f'Привет, шкет {name}')
#         break
#     elif 10 <= age <= 18:
#         print(f'Как жизнь {name}?')
#         break
#     elif 18 < age <= 100:
#         print(f'Что желаете {name}?')
#         break
#     elif age > 100:
#         print(f'{name}, вы лжете - в наше время столько не живут...')
#         break


"""
4. Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n (включая n).
Реализовать в 2-х вариантах: используя цикл while и цикл for
"""

# Через цикл for
# n = int(input('Введите число n: '))
# summ = 0
# for i in range(1, n+1):
#     summ += i ** 3
# print(summ)


# Через цикл while
# n = int(input('Введите число n: '))
# summ = 0
# j = 0
# while j != n:
#     j += 1
#     summ += j ** 3
# print(summ)


"""
5. Сделать программу, в которой нужно будет угадывать число.
"""


# from random import randint
# counter = 0
# ask = 'Компьютер загадал число. Попробуешь угадать? (да/нет): '
# if input(ask) == 'нет':
#     print('Ну и ладно!')
# else:
#     print('Ха! Игра началась!')
#     n = randint(1, 9)
#     while True:
#         counter += 1
#         print('Выбери число  от 1 до 9: ')
#         if int(input()) == n:
#             print(f'Ух ты! Угадал с {counter} раза!')
#             break
#         else:
#             print('Не угадал!... Попробуй еще раз :)')
#             continue