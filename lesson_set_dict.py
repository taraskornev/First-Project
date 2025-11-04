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
def task6()
    text = "lorem ipsum dolor sit amet"
    text = list(text)
    letters = {i: text.count(i) for i in text}
    print(letters)
#task6()

# Напишіть програму, яка приймає рядок символів, і обчислює кількість букв і цифр.

# Вхідні дані:

# Project Gutenberg offers over 59,000 free eBooks
# Вихідні дані:

# LETTERS 36
# DIGITS 5
