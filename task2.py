# Напишіть програму, в якій користувач вводить пароль і якщо він співпадає
# із наперед визначеним паролем для цього користувача, то виводиться
# повідомлення Password accepted.. У іншому випадку повідомлення буде Sorry,
# that is the wrong password..

# a = str(1234)
# print("Enter password:",)
# b = str(input())
# if b == a: print ("Password accepted")
# else : print ("Wrong password")

# Користувачем вводиться два імені. Використовуючи конструкцію розгалуження
# програма повинна вивести імена в алфавітному порядку.

# name1 = input("Enter name1: ")
# name2 = input("Enter name2: ")
# if name1 <= name2:
#     print(name1, name2)
# else:
#     print(name2, name1)

# Напишіть програму, яка виводить назви введених чисел. Користувач вводить
# ціле число. Якщо це число або 1 або 2 або 3, то виводиться повідомлення -
# назва числа, відповідно, One, Two, Three. В усіх інших випадках виводиться
# слово Unknown.

# name_of_number = ""
# number = int(input(Enter number:""))
# if number == 1:
#     name_of_number = "One"
# elif number == 2:
#     name_of_number = "Two"
# elif number == 3:
#     name_of_number = "Three"
# else:
#     print("Unknown")

# Користувач вводить дві різних англійські літери в окремих рядках. Напишіть
# програму, яка виводить повідомлення про місце розташування однієї літери
# відносно іншої у алфавіті.

# letter1 = input("Enter letter1: ").lower()
# letter2 = input("Enter letter2: ").lower()
# if letter1 <= letter2:
#     print("First letter: ", "Second letter:", letter2)
# else:
#         print("First letter: ", "Second letter:", letter2)

# if register matters        
# letter1 = input("Enter letter1: ")
# letter2 = input("Enter letter2: ")
# if letter1.lower() <= letter2.lower():
#     print("First letter: ", "Second letter:", letter2)
# else:
#         print("First letter: ", "Second letter:", letter2)


# 5. Напишіть програму, в якій користувач вводить значення температури,
# і, якщо це значення менше або дорівнює 0 градусів Цельсія, необхідно
# вивести повідомлення A cold, isn’t it?. Якщо ж температура становить
# більше 0 і менше 10 градусів Цельсія повідомлення буде Cool.,
# у інших випадках Nice weather we’re having..

# temp1 = int(input ("Enter temperature1: "))
# if temp1 <= 0:
#     print("cold, isn’t it?")
# elif temp1 <= 10:
#     print("cool")
# else:
#     print("Nice weather we’re having")

# Визначте назву геометричної фігури за введеною кількістю її сторін. Програма
# повинна підтримувати фігури від 3 до 6 сторін. Якщо введена кількість сторін
# поза межами цього діапазону, програма повинна відображати відповідне
# повідомлення.

# print ("Enter amount of sides:")
# sides = int(input())
# if sides == int(3):
#         print ("triangle")
# elif sides == int(4):
#          print ("rect")
# elif sides == int(5):
#          print ("pentagon")
# elif sides == int(6):
#          print ("hexa")
# else:
#         print ("unknown")

# Ігрове поле рулетки поділено на номери від 0 до 36, які мають чорний,
# червоний або зелений кольори. Номер 0 має зелений колір, для номерів
# від 1 до 10, непарні номери - червоні, а парні - чорні. Непарні номери
# від 11 до 18 - чорні, а парні номери - червоні. Непарні номери від 19 до 28 
# - червоні, а парні номери - чорні. Непарні номери від 29 до 36 - чорні,
# а парні номери - червоні. Напишіть програму, яка отримує номер
# (число від 0 до 36) та показує, чи є номер зеленим, червоним або чорним.
# Програма повинна враховувати варіант, якщо користувач вводить номер,
# # який знаходиться за межами діапазону від 0 до 36.

print ("Enter number from 0 to 36:")
number = int(input())
if number == 0:
    print("green")
elif 1 <= number <= 10:
    if number % 2 == 0:
        print("black")
    else:
        print("red")
elif 11 <= number <= 18:
    if number % 2 == 0:
        print("red")
    else:
        print("black")
elif 19 <= number <= 28:
    if number % 2 == 0:
        print("black")
    else:
        print("red")
elif 29 <= number <= 36:
    if number % 2 == 0:
        print("red")
    else:
        print("black")
else:
    print("error")




# Дано дві точки: A (x1, y1) і B (x2, y2). Напишіть програму, яка визначає,
# яка із точок знаходиться далі від початку координат.
#  Вхідні дані:
#  1
#  2
#  3
#  2
#  4
#  4
#  4
#  4
#  Вихідні дані:
#  B
#  The distance is the same





# Вводяться координати (x, y) точки A і радіус кола (r). Визначити, чи належить дана точка колу, якщо його центр знаходиться в початку координат.
# Вхідні дані:
# 3
# 4
# 5
# -2
# 5
# 3
# Вихідні дані:
# The point belongs to the circle
# The point is outside the circle

# Дано натуральное число. Визначити, чи закінчується число парною цифрою.
# Вхідні дані:
# 1234
# 35
# Вихідні дані:
# True
# False