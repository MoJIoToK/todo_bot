import os, sys

import telebot

TOKEN_FILENAME = "token.txt"

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


@bot.message_handler(content_types=["text"])
# EchoBot send message with text from client message
def echoBot(message):
    word = "Мария"
    greating = "Ба! Знакомые все лица!"
    if word in message.text:
        bot.send_message(message.chat.id, greating)
    else:
        bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
