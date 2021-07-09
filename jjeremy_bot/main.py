import telebot


bot = telebot.TeleBot('1650295407:AAHKcYX4an6CrGKKyNCSjZgaDbYHo_6WvA0')
way_saved = 'C:/Users/User/Desktop/New_Doc/wb/tg_bots/jjeremy_bot/'


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Hello, this is testing bot!\n'
                                      'What can this bot do?\n'
                                      '-Translate a photo into a drawing!')


@bot.message_handler(commands=['drawing'])
def drawing_start(message):
    try:
        send = bot.send_message(message.chat.id, 'Good! Send your photo...')
        bot.register_next_step_handler(send, drawing_saved)
    except TypeError:
        bot.send_message(message.chat.id, 'You did not send a photo!')
        drawing_start()


def drawing_saved(message):
    try:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = way_saved + file_info.file_path
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, 'Photo saved!\n'
                              'Waiting for...')
        way_photo = way_saved + file_info.file_path
        photo = open(way_photo, 'rb')
        bot.send_photo(message.chat.id, photo)

    except Exception as Ex:
        bot.reply_to(message, Ex)


# if __name__ == '__main__':
bot.polling()
