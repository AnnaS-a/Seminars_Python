# Задача 2: Напишите программу, которая на вход принимает 5 чисел (можно списком) и находит максимальное из них.
# Примеры: 1. 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

# 1
my_list = [3, 6, 54, 10, 12]
max_num = my_list[0]
for i in my_list:
    if i > max_num:
        max_num = i
print(max_num)


# 2
# a = int(input("Введите 1 число "))
# b = int(input("Введите 2 число "))
# c = int(input("Введите 3 число "))
# d = int(input("Введите 4 число "))
# e = int(input("Введите 5 число "))
# my_list = [a, b, c, d , e]

# max_number = max1(list)
# print("Наибольшее число:", max_number)





