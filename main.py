
HELP = """
help - напечатать справку по программе.
add -  добавить задачу в список (название задачи задаёт пользователь).
show - напечатать все добавленные задачи.
exit - выход."""

today = []
tomorrow = []
other = []

def add(task):
    date = input("Введите дату: ")
    match date:
        case "сегодня": today.append(task)
        case "завтра": tomorrow.append(task)
        case _: other.append(task)

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(today)
        print(tomorrow)
        print(other)
    elif command == "add":
        task = input("Введите задачу: ")
        add(task)
    elif command == "exit":
        run = False
    else:
        print("Данная команда неизвестна!")
        run = False


print("Спасибо за использование! До свидания!")