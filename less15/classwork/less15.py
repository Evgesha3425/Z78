# fruit = ["mango", "banana", "apple", "peach"]
# iter_fruit = iter(fruit)
# print(next(iter_fruit))
# print(next(iter_fruit))
# print(next(iter_fruit))
# print(next(iter_fruit))
# for i in iter_fruit:
#     print(i)
# next(iter_fruit)


# class Iterator:
#     def __init__(self, start, step):
#         self.step = step
#         self.start = start - step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += self.step
#         if self.start > 10000:
#             raise StopIteration
#         return self.start
#
#
# iterator = Iterator(20, 50)
#
# f_obj = filter(lambda x: x % 30 == 0, iterator)
# for i in iterator:
#     print(i)


# d = {2: 2, 5: 2, 7: 2}
# d_iter = iter(d.values())
# print(next(d_iter))
# print(next(d_iter))


# def generator():
#     print("start generator")
#     fruits = ["mango", "banana", "apple", "peach"]
#     for fruit in fruits:
#         print(f"I yield {fruit}")
#         try:
#             result = yield fruit
#             print(f"I yielded {fruit} and got {result}")
#         except ValueError:
#             print("I know that you is clever boy")
#
#     print("finishing generator")
#
#
# f_gen = generator()
# gen_iter = iter(f_gen)


# def numb_generator():
#     i = 1
#     while True:
#         result = yield i
#         print(f"I yielded {i} and got {result}")
#         if i > 20:
#             raise StopIteration
#         i += 1
#
#
# n_gen = numb_generator()


# def numb_generator():
#     print("start")
#     result = yield 1
#     print(f"I yielded 1 and got {result}")
#     result = yield 2
#     print(f"I yielded 1 and got {result}")
#     result = yield 3
#     print(f"I yielded 1 and got {result}")
#     result = yield 4
#     print(f"I yielded 1 and got {result}")
#     result = yield 5
#     print(f"I yielded 1 and got {result}")
#     print("finish")
#
#
# n_gen = numb_generator()


import re  # регулярные выражения

# match - то что строка начинается с определенного шаблона
# fullmatch - то что строка полностью соответствует шаблону
# split - разбивает по шаблону
# findall - ищет все вхождения шаблона

# print(r"hello\nworld")

"""
. - любая буква
$ - окончание шаблона
\d - любая цифра
\d{3} - 3 любых цифры
\d{2, 5} - от 2 до 5 цифр
\d+ - от 1 до бесконечности
\d{*} == \d+ - от 0 до бесконечности
\d+? == d{0, 1} 
\w - любая буква и цифра кроме пробела
\W - любая не буква не цифра
[1-5]+ - возьми цифры от 1 до 5 жадно (включая крайние значения)
[1-5a-f]+ - возьмет цифры от 1 до 5 и буквы от a до f
"""

# pattern = r"dog"
# some_str = "dog eat my homework"
# print(re.fullmatch(pattern, some_str))

# pattern = r"\(\w*\)"
# some_str = "12(ae3)81 2412()5 (dfsef)(2198das)"
# print(re.findall(pattern, some_str))

# pattern = r"\([a-zA-Z]*\)"
# some_str = "12(ae3)81 2412()5 (dfsef)(2198das)"
# print(re.findall(pattern, some_str))

# pattern = r"\([^142]*\)"
# some_str = "12(ae3)81 2412()5 (dfsef)(2198das)"
# print(re.findall(pattern, some_str))

# pattern = r"\+?\d{3}-?\d{2}-?\d{3}-?\d{2}-?\d{2}"
# some_str = "37529-321-23-12"
# print(re.fullmatch(pattern, some_str))

# pattern = r"[\w\.]+@\w+\.\w+"
# some_str = "den.listapad@mail.ru surovcov@gmail.com vasya_123pupkin@yandex.by"
# print(re.findall(pattern, some_str))

pattern = r"\w*less\b"
some_str = "dasless less lessdasd"
print(re.findall(pattern, some_str))