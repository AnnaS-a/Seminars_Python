# Задача 3: Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры: 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# 1

a = int(input('Введите число N '))
s = ''
for i in range (-a, a + 1):
    s = s + ' ' + str(i)
#    print (s)
print (s[1:])


# 2

# a = int(input("Введите число N"))
# b = -a
# for i in range(b, a + 1):
#   print(i)

# 3

# a = int(input ("введите число  "))
# num_list = list(range(-a, a + 1))
# print(num_list)