import os, sys

import telebot
from random import choice

TOKEN_FILENAME = "token.txt"
GREATING = "Ба! Знакомые все лица!"
RANDOM_TASKS = ["Учить питон", "Поесть", "Посмотреть курсы различных школ", "Посмотреть мероприятия"]

HELP = """
/help - напечатать справку по программе.
/add -  добавить задачу в список (название задачи задаёт пользователь).
/show - напечатать все добавленные задачи.
/exit - выход.
/random - добавлять случайную задачу на сегодня."""

tasks = dict()

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

def add_todo(date, task):
    date = date.lower()
    if tasks.get(date) is not None:
        tasks[date].append(task)
    else:
        tasks[date] = [task]

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    _, date, tail = message.text.split(maxsplit=2)
    task = ' '.join([tail])
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')

@bot.message_handler(commands=["random"])
def random(message):
    task = choice(RANDOM_TASKS)
    add_todo('сегодня', task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на сегодня')

@bot.message_handler(commands=["show", "print"])
def show(message):
    date = message.text.split()[1].lower()
    if date in tasks:
        text = ''
        for task in tasks[date]:
            text += f'[ ] {task}\n'
    else:
        text = 'Такой даты нет'
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
