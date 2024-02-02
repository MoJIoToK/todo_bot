import os, sys

import telebot
import random

TOKEN_FILENAME = "token.txt"
GREATING = "Ба! Знакомые все лица!"
RANDOM_TASKS = ["Учить питон", "Поесть", "Посмотреть курсы различных школ", "Посмотреть мероприятия"]

HELP = """
/help - напечатать справку по программе.
/add -  добавить задачу в список (название задачи задаёт пользователь).
/show - напечатать все добавленные задачи.
/exit - выход.
/random - добавлять случайную задачу на сегодня."""


# GetToken returns token
def getToken():
    token = ''
    if os.path.isfile(TOKEN_FILENAME):
        file = open(TOKEN_FILENAME, "r")
        token = file.read()
        file.close()
    else:
        print("Пожалуйста, создайте в папке проекта файл 'token.txt' и поместите "
              "туда токен для работы телеграм бота  и запустите скрипт заново")
        sys.exit()
    return token


token = getToken()

bot = telebot.TeleBot(token)

tasks = {
}


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print(f"Задача {task} добавлена по дате {date}!")

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Task - " + task + " - is added to " + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["random"])
def random_add(message):
    task = random.choice(RANDOM_TASKS)
    date = "today"
    add_todo("Сегодня", task)
    text = "Task - " + task + " - is added to " + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + " - " + task + "\n"
    else:
        text = "Такой даты не обнаружено!"

    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
