HELP = """
help - напечатать справку по программе.
add -  добавить задачу в список (название задачи задаёт пользователь).
show - напечатать все добавленные задачи.
exit - выход."""

today = list()
tomorrow = list()
other = list()
tasks = {

}

def add(task):
    date = input("Введите дату: ")
    match date:
        case "сегодня":
            today.append(task)
        case "завтра":
            tomorrow.append(task)
        case _:
            other.append(task)
    pass


# def printTask(list):
#     print(list)
#     pass

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
        # printTask(today)
        # print('Завтра: ')
        # printTask(tomorrow)
        # print('Другие: ')
        # printTask(other)
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date] = []
            tasks[date].append(task)
        print(f"Задача {task} добавлена по дате {date}!")
    elif command == "exit":
        run = False
    else:
        print("Данная команда неизвестна!")
        run = False

print("Спасибо за использование! До свидания!")
