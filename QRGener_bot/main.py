# -*- coding: utf-8 -*-
# By Jamadog QR Generation
import telebot
import os
import qrcode

bot = telebot.TeleBot('') # ваш токе

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'What can this bot do?\n'
                                      '-Creating a QR by link /qr')


@bot.message_handler(commands=['qr'])
def qr_start(message):
    send = bot.send_message(message.chat.id, 'Ok! Send your URL...\n'
                                             'Or write cancel')
    bot.register_next_step_handler(send, qr_create)


def qr_create(message):
    if message.text.lower() == 'cancel':
        bot.send_message(message.chat.id, 'Ok, the cancellation was successful!')
        start_command(message)
    else:
        try:
            image = qrcode.make(message.text.lower())
            name = 'qr.png'
            image.save(name)
            qr = open(name, 'rb')
            bot.send_photo(message.chat.id, qr)
            qr.close()
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), name)
            os.remove(path)
        except FileNotFoundError:
            pass

bot.polling(True)
