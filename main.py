import random

import homework1

HELP = """
help - напечатать справку по программе.
add -  добавить задачу в список (название задачи задаёт пользователь).
show - напечатать все добавленные задачи.
exit - выход.
random - добавлять случайную задачу на сегодня."""

RANDOM_TASKS = ["Учить питон", "Поесть", "Посмотреть курсы различных школ", "Посмотреть мероприятия"]

tasks = {
}

run = True

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print(f"Задача {task} добавлена по дате {date}!")

while run:
    command = input("Для отображения доступных команд введите - `HELP`. \nВведите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print(f"- {task}")
        else:
            print("Такой даты не обнаружено!")
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
    elif command == "exit":
        run = False
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("Сегодня", task)
    else:
        print("Данная команда неизвестна!")
        run = False

print("Спасибо за использование! До свидания!")

words = ['python', 'c++', 'c', 'scala', 'java']
print(homework1.count_letter(words, "c"))
