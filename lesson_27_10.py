# #ax^2 + bx + c = 0
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# print(f"дано кв уравнение {a} x2 {b} x + {c} = 0")

# d = b ** 2 - 4 * a * c

# if d < 0:
#     print("коренiв нема")
# elif d == 0:
#     x = (-b) / (2 * a)
#     print("корень один: х =", x)
# else:
#     x1 = (-b -d ** 0.5) / (2 * a)
#     x1 = (-b -d ** 0.5) / (2 * a)

 #------------------------------------------------------



# n = int(input("Enter number: "))
# for i in range(n):
#     print("Hello Python!")
#--------------------------------------------------

# a = int(input("a: "))
# b = int(input("b: "))

# if a > b:
#     a, b = b, a
# 5
# for i in range(a, b + 1):
#     print(i)

#-------------------------------------------

# n = int(input("Enter sec: "))
# for i in range(n, 0, -1):
#     print(i)
# print("Start!")
#--------------------------------------------
# n = int(input("Enter sec: "))
# while n > 0:
#     print(n)
#     n -= 1
# print("Start!")
#-------------------------------------------------
# n = int(input("Enter number of steps: "))
# for i in range(1, n + 1):
#     print("#" * i)

# n = int(input("Enter number of steps: "))
# for i in range(1, n + 1):
#     print("#" * i)
#-----------------------------
# n = int(input("Count: "))
# f = 1
# for i in range(1, n + 1):
#     print(i)
#     f *= i
# print(f)

# print("------")
# f = 1
# while n > 0:
#     print(n)
#     f *= n
#     n -= 1
# print(f)

# def average():
#     n = int(input("Count: "))
#     f = 1
#     while n > 0:
#         print(n)
#         f *= n
#         n -= 1
#     print(f)

# average()

# 1. Напишіть функцію, яка отримує ім’я і друкує вітальне повідомлення `Hello, <name>`.
# name = "taras"
# def name1(name = "none"):
#     return f"Hello, {name}!"

# print(name1())
# print(name1(name))

# 2. Напишіть функцію, яка отримує рядок і ціле число `n` та повертає `n` копій заданого рядка.



# def copy_string(text, n):
#     return (text + " ") * n 
# text = input("enter text:")
# n = int(input("Enter n:"))
# print(copy_string(text, n))

# 3. Напишіть функцію для обчислення суми двох цілих чисел.

# def sum_ab(a, b):
#     return a + b
# num1 = int(input("enter number 1: "))
# num2 = int(input("enter number 2: "))

# print(sum_ab(num1, num2))



# 4. Напишіть функцію для отримання рядка з перших `n` символів іншого рядка. 

# def n_letter(word, n):
#     if len(word) < n:
#         return word
#     return word[:n]
# string = "letter"
# n = 3
# print(n_letter(string, n))

# Якщо довжина рядка менше `n`, повернітlenlenь початковий рядок.


# 5. Напишіть функцію для визначення найбільшого з трьох цілих чисел з використанянм вбудованої функції `max()`.




# 6. Напишіть функцію для створення позначок тегів `HTML` навколо введених рядків. Функція отримує назву тега `HTML` і рядок, який необхідно помістити у відповідні теги.

#     Вхідні дані:
#     ```
#     strong Python
#     ```
#     Вихідні дані:
#     ```
#     <strong>Python</strong>
#     ```

# def tag_html(tag, text):
#     return f"<{tag}>{text}<\{tag}>"

# text = input("Enter text: ")
# tag = text.split()[0]
# string = " ".join(text.split()[1:])
# print(tag_html(tag, string))




# 7. Напишіть функцію, яка повертає назву пори року для введеного значення номера місяця.

# 10. Напишіть функцію, яка отримує значення середньомісячної кількості опадів по місяцях (в мм) і повертає загальний обсяг опадів протягом року, середньорічну кількість опадів, назви місяців та значення з найвищим та найменшим числом опадів протягом року.

# 22 22 24 49 72 98 101 82 51 40 36 24
# Вихідні дані:

# (621.0, 51.75, (101.0, 'July'), (22.0, 'January'))

# def rainfall_stats(values):
#     month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#     rain = list(map(float, values.split()))
#     total = sum(rain)3
#     average = total / 12
#     max_rain = max(rain)

#     min_rain = min(rain)

#     min_month = [rain.index(min_rain)]
#     max_month = [rain.index(max_rain)]

#     return (total, average, (max_rain, max_month), (min_rain, min_month))

# data = "22 22 24 49 72 98 101 82 51 40 36 24"

# result = rainfall_stats(data)
# print(result)

# [1, "a", 2.0]
# list()

# 1. Створіть список на основі введеної послідовності цілих чисел і надрукуйте другу половину списку. Якщо кількість не парна, то вивести більшу кількість.

# value = "1 3 45 67 8 9 4 56 89 34 12 6 23 1 6"
# value_list = list(map(int, value.split()))
# print(value_list[len(value_list)//2:])

# 2. Створіть список на основі введеної послідовності цілих чисел і надрукуйте його елементи таким чином: два останні елементи переміщені з кінця в початок списку без зміни їх початкового порядку.

# value = "1 3 45 67 8 9 4 56 89 34 12 6 23 1 6"

# value_list = list(map(int, value.split()))
# list_minus2 = value_list[:-2]
# list_last2 = value_list [-2:]

# print(list_last2 + list_minus2)


# 3. Збережіть назви мов світу, які вводяться в одному рядку через пропуск, у списку. Простежте за тим, щоб елементи у списку не зберігались в алфавітному порядку. Відсортуйте список в алфавітному порядку і виведіть його елементи в рядку через пропуск.

# languages = "english german ukrainian russian polish french portugeese spanish danish norvegian"
# language_list = languages.split()
# language_list.sort()
# print(" ".join(language_list))

# 4. Вивести елементи списку в зворотному порядку, не змінюючи сам список

# languages = "english german ukrainian russian polish french portugeese spanish danish norvegian"
# language_list = languages.split()
# language_list.sort()
# print(" ".join(sorted(language_list, reverse=True)))

# 5. Виведіть всі елементи списку з парними індексами. Вводиться список чисел. Всі числа списку знаходяться на одному рядку.