#1 
def task1():
    to_do = {
        "today": ["read", "clear", "dog"],
        "tomorrow": ["read", "call my mom"]
    }
    # print(to_do)
    print("To do for today:")
    for item in to_do["today"]:
        print("-", item)
        
    print("To do for tomorrow:")
    for item in to_do["tomorrow"]:
        print("-", item)
# task1()

def task2():
    users = {
        0: "Alice",
        1: "Bob",
        2: "Jack",
    }
    user_id = int(input("Your ID: "))
    if user_id in users:
        print(f"Hello, {users[user_id]}")
    else:
        print("Hello, everybody!")
# task2()

# Напишіть програму для сортування за зростанням (за алфавітом) словника за ключами. Словник зберігає пари ключ-значення у вигляді «назва фільму: рік релізу». Інформація виводиться як у вихідних даних: сортування має бути проведено за назвами фільмів.

# Вихідні дані:

# ('Avengers: Endgame', 2019) ('Guardians of the Galaxy', 2014) ('Iron Man', 2008) ('Thor', 2011)

def task3():
    films = {
        'Avengers: Endgame': 2019,
        'Iron Man': 2008,
        'Guardians of the Galaxy': 2014,
        'Thor': 2011
    }
    sorted_films = dict(sorted(films.items()))

    for name in sorted_films.items():
        print(f"{name}")
# task3():

#4. Надрукуйте елементи словника, де ключі - це числа від '1' до 'n' (обидва числа включно), а значення - квадрати ключів. 'n' – ціле число, яке вводить користувач.

def task4():
    n = int(input("n: "))
    # squares = {} #dictionary
    # for i in range(1, n+1):
    #     squares[i] = i ** 2
    squares = {i: i ** 2 for i in range(1,n+1)}
    print(squares)
# task4()

# 5. Створіть словник, в кому ключі – назви днів тижня, а значення - цілі числа, що позначають порядковий номер дня тижня від 0 до 6. Надрукуйте назву дня за введеним порядковим номером дня. Якщо введений номер виходить за межі, програма жодних повідомлень не друкує і не повідомляє про помилку.
def task5():
    weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days = [i for i in range(7)]

    # week_dict = {}
    # for day in range(7):
    #     week_dict[weeks[day]] = days[day]
    week_dict = {weeks[day]: days[day] for day in range(7)}

    n = int(input())
    for day, number in week_dict.items():
        if number == n:
            print(day)
            break
# task5()

#6Напишіть програму для створення словника із введеного рядка символів для підрахунку кількості символів.

# Вхідні дані:

# Lorem ipsum dolor sit amet
# Вихідні дані:

# {'L': 1, 'o': 3, 'r': 2, 'e': 2, 'm': 3, ' ': 4, 'i': 2, 'p': 1, 's': 2, 'u': 1, 'd': 1, 'l': 1, 't': 2, 'a': 1}
def task6():
    text = "lorem ipsum dolor sit amet"
    text = list(text)
    letters = {i: text.count(i) for i in text}
    print(letters)
#task6()

#7. Напишіть програму, яка приймає рядок символів, і обчислює кількість букв і цифр.

# Вхідні дані:

# Project Gutenberg offers over 59,000 free eBooks
# Вихідні дані:

# LETTERS 36
# DIGITS 5
def task7():
    text = "Project Gutenberg offers over 59,000 free eBooks"
    number_count = 0
    alpha_count = 0
    for ch in text:
        if ch.isdigit():
            number_count += 1
        elif ch.isalpha():
            alpha_count += 1
    result = {
        "Letters:": alpha_count,
        "Digits:": number_count
    }

    # print(result)

    for key, value in result.items():
        print(key, value)
#task7()

# 9. Дано список словників. Кожен словники має 2 пари елементів: ключ 'name' і значення імені студента, ключ 'points' і значення - список балів з різних дисциплін (цілі двоцифрові числа). Надрукуйте найменші значення балів, отримані кожним студентом, в один рядок з пропуском.

# 10. Дано два списки чисел. Порахуйте, скільки унікальних цифр міститься в обох з них.
def task10():
    numbers1 = [1, 5, 3, 8, 0, 1]
    numbers2 = [23, 9, 0, 1, 5]
    result = len(set(numbers1 + numbers2))
    print(result)
#task10()

# numbers1 = {1, 5, 3, 8, 0, 1}
# numbers2 = {23, 9, 0, 1, 5}

# # объединение множеств: возвращает все уникальные элементы, которые есть в numbers1 или numbers2 (или в обоих)
# print(numbers1.union(numbers2)) # a | b 
# print(numbers1 | numbers2) # a | b

# # A - B = A (WITHOUT B)
# # разность множеств: возвращает элементы, которые есть в numbers1, но отсутствуют в numbers2
# print(numbers1.difference(numbers2))
# print(numbers1 - numbers2)


# # симметричная разность: элементы, которые есть только в одном из множеств (не пересекаются)
# print(numbers1.symmetric_difference(numbers2))
# print(numbers1 ^ numbers2)

# # пересечение множеств: возвращает только те элементы, которые присутствуют и в numbers1, и в numbers2
# print(numbers1.intersection(numbers2))
# print(numbers1 & numbers2)

# 11. Дано три словники, в яких ключами є малі букви латинського алфавіту, а значеннями - цілі числа. Ключі у всіх словниках – різні, їх є по 3 в кожному словнику. Об’єднайте всі три словники в один і виведіть його вміст. Підказка. скористайтеся оператором **, що використовується для об’єднання довільної кількості словників.
def task11():
    dict1 = {"a": 1,"b": 2,"c": 3,}
    dict2 = {"d": 4,"e": 5,"f": 6,}
    dict3 = {"g": 7,"h": 8,"i": 9,}
    print({**dict1, **dict2, **dict3})
# task11()

# Створіть словник, який відображає ідентифікатори акцій на біржі. Ключами словника є ідентифікатори акцій, а значеннями - дійсні числа - ціни акцій. Надрукуйте ціни акцій та ідентифікатори у порядку зростання ціни.

# Вихідні дані:

# 10.75 FB
# 37.2 HPQ
# 45.23 ACME
# 205.55 IBM
# 612.78 AAPL

def task12():
    stocks = {
        "FB": 10.75,
        "HPQ": 37.75,
        "ACME": 23.75,
        "IBM": 205.75,
        "AAPL": 612.75
        }

    def get_value(item):
        return item[1]

    for key, value in sorted(stocks.items(), key=get_value):
        print(value, key)
# task12()

def count(n):
    if n > 0:
        print(n)
        count(n - 1)
    return ("Start!")
print(count(5))
