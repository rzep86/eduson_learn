# Price calculator
# group_of_visitors = input('Введите возраст участников группы: ').split()
# total_price = 0
# def calcutating():
#     global total_price
#     for i in group_of_visitors:
#         if int(i) <= 2 or int(i) >= 65:
#             total_price += 0
#         elif 3 <=int(i) <= 12:
#             total_price += 200
#         else:
#             total_price += 500
#     return str(total_price) + '.00'
# print(calcutating())

#Date and time
# month = int(input('Insert month: '))
# year = int(input('Insert year: '))
# def days():
#     if year % 4 == 0 and month == 2:
#         return 29
#     elif month > 12:
#         return 'Incorrect value of month'
#     elif month in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     elif month == 2:
#         return 28
#     else:
#         return 30
#
# print(days())

#Cesar's code
# phrase = input('Insert your phrase: ')
# def cesar_code():
#     result = ''
#     for i in phrase:
#         if i.isalpha() and i.isupper():
#             if ord(i) <= 87:
#                 result += chr(ord(i) + 3)
#             else:
#                 result += chr(ord(i) - 23)
#         elif i.isalpha() and i.islower():
#             if ord(i) <= 119:
#                 result += chr(ord(i) + 3)
#             else:
#                 result += chr(ord(i) - 23)
#         else:
#             result += i
#     return result
# print(cesar_code())

#multiply table
# def multiply_table():
#     for i in range(1,11):
#         for j in range(1,11):
#             print(i * j, end=' ')
#         print()
#
# multiply_table()

# 1 of 49
# import random
# print(sorted(random.sample(range(1, 50), 6, counts=None)))

#LIST
# res = []
# num = int(input('Insert number: '))
# while num != 0:
#     res.append(num)
#     num = int(input('Insert number: '))
#
# res.sort()
# for i in res:
#     print(i)

#RECURSION
def add():
    num = input('Insert number: ')
    if num == '':
        return 0
    else:
        return int(num) + add()

print(add())
print()

