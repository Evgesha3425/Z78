import re
"""
1. Вам дана последовательность строк. Выведите строки, содержащие "cat".
"""

# pattern = r"\w*cat\w*"
# text = "my cat is not dog, my cat is catofei Murzik"
# print(re.findall(pattern, text))

"""
2. Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
"""

# pattern = r"\w*z\w{3}z\w*"
# text = "privet zfesz fsrze_3zfe z23z"
# print(re.findall(pattern, text))

"""
3. Номер должен быть длиной 10 знаков и начинаться с 8 или 9. Есть список телефонных номеров, и нужно проверить их, 
используя регулярные выражения в Python
"""

# pattern = r"[8-9]\d{9}"
# text = "4561237895 8524569636 94562584 9456212574 8945612378"
# print(re.findall(pattern, text))

"""
4. Дана строка, выведите все вхождения слов, начинающиеся на гласную букву.
"""

# pattern = r"\b[aeiouy]\w+"
# text = "apple pineapple orange mango"
# print(re.findall(pattern, text))

"""
5. Дана строка. Вывести все числа этой строки, как отрицательные так и положительные. 
"""

# pattern = r"[+-]?[0-9{\d}]"
# text = "fes43ew -23tgr fsr5-32fse"
# print(re.findall(pattern, text))

"""
6. В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.
"""

# pattern = r"human"
# text = "human is descended from apes. human is not a robot"
# print(re.sub(pattern, "computer", text))

"""
7. Извлечь дату из строки. Формат даты dd –mm-yyyy.
"""

# pattern = r"\d{2}-\d{2}-\d{4}"
# text = "The first date is 22-14-2024. The second date is 12.12.2022. The third date is 15-14-23. " \
#        "And the last date is 14-04-1997."
# print(re.findall(pattern, text))

"""
8. Найти все слова, в которых есть хотя бы одна буква ‘b’
"""

# pattern = r"\w*b\w*"
# text = "It goes without saying, books are our teachers and friends. They teach us to be kind, clever, " \
#        "polite, hardworking, friendly. "
# print(re.findall(pattern, text))

"""
9. В каждой строке замените все вхождения нескольких одинаковых букв на одну букву. 
Буквой считается символ из группы \w.
"""

# pattern = r'(\w)\1+'
# text = "swimming book big loook"
# print(re.sub(pattern, r'\1', text))

