import telebot


token = "7398726008:AAGD8gMSDaDnHgKrwmcUXfH51zrYFG_2OgI"
bot = telebot.TeleBot(token)


chat_id = 695078526

@bot.message_handler(content_types=['text'])
def get_all_accounts(message):
    bot.send_message(message.chat.id, text=f"{message.chat.id}")


def send_notify_level_up(udid, level, monster_id):
    bot.send_message(chat_id, text=f"{udid} ({monster_id}) has reached {level} level")


def send_notify_new_account(udid, monster_id):
    bot.send_message(chat_id, text=f"new account {udid} ({monster_id})")


def send_notify_udid_found(udid):
    bot.send_message(chat_id, text=f"UDID found {udid}")

