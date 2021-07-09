import telebot
import draw_image
import os

bot = telebot.TeleBot('1650295407:AAHKcYX4an6CrGKKyNCSjZgaDbYHo_6WvA0')
way_saved = 'C:/Users/Jamadog/Desktop/Projects/tg_bots/jjeremy_bot/'


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
        img_input = way_saved + file_info.file_path

        with open(img_input, 'wb') as new_file:
            new_file.write(downloaded_file)
            new_file.close()
        bot.reply_to(message, 'Photo saved!\n'
                              'Waiting for...')

        img_output = draw_image.draw_img(img_input)
        img_output.save(way_saved+file_info.file_path)
        way_img_output = way_saved+file_info.file_path
        photo = open(way_img_output, 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), way_img_output)
        os.remove(path)

    except Exception as Ex:

        print(Ex)


# if __name__ == '__main__':
bot.polling()
