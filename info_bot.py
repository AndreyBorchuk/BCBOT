import telebot


token = "7398726008:AAGD8gMSDaDnHgKrwmcUXfH51zrYFG_2OgI"
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def get_all_accounts(message):
    bot.send_message(message.chat.id, text=f"{message.chat.id}")


def send_notify_level_up(udid, level, monster_id):
    bot.send_message(695078526, text=f"{udid} ({monster_id}) has reached {level} level")


def send_notify_new_account(udid, monster_id):
    bot.send_message(695078526, text=f"new account {udid} ({monster_id})")


bot.polling(none_stop=True)