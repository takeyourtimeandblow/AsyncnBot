import random
from time import sleep

import telebot
import datetime
from typing import Final
from telebot import types

token: Final [str] = open("bot_token.txt").read()

try:
    bot = telebot.TeleBot(token)
    msg_ids = []

    def buttons(menu_id: str = ''):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        match menu_id:
            case 'dice': #dice throwing
                dice_list = ['/Throw_dice_1_times', '/Throw_dice_2_times', '/Throw_dice_20', '/back']
                markup.add(*[types.KeyboardButton(i) for i in dice_list])

                return markup

            case 'timer': #timer
                timer_list = ['/30_secs', '/1_min', '/5_mins', '/back']
                markup.add(*[types.KeyboardButton(i) for i in timer_list])

                return markup

            case _:
                main_menu_list = ['/time', "/clear", "/date", "/dice", "/timer"]
                markup.add(*[types.KeyboardButton(i) for i in main_menu_list])

                return markup


    @bot.message_handler(commands=['start'])
    def start_message(message):
        msg_ids.append(
            bot.send_message(
                message.chat.id, "Привет ✌️", reply_markup=buttons()
            ).message_id
        )


    @bot.message_handler(commands= ['time'])
    def time(message):
        current_time = datetime.datetime.now()

        msg_ids.append(
            bot.send_message(
                message.chat.id,f"🕧The time is {current_time.strftime('%X')}", reply_markup=buttons()
            ).message_id
        )


    @bot.message_handler(commands=['date'])
    def time(message):
        current_date = datetime.date.today()

        msg_ids.append(
            bot.send_message(
                message.chat.id, f"⌚The date is {current_date}", reply_markup=buttons()
            ).message_id
        )


    @bot.message_handler(commands=['clear'])
    def clear(message):
        bot.delete_messages(message.chat.id, msg_ids)
        msg_ids.clear()


    @bot.message_handler(commands=['dice'])
    def dice(message):
        msg_ids.append(
            bot.send_message(
                message.chat.id, f"Select what dice to Throw 🎲", reply_markup=buttons('dice')
            ).message_id
        )


    @bot.message_handler(commands=['Throw_dice_1_times', 'Throw_dice_2_times', 'Throw_dice_20'])
    def throw(message):
        num = []
        match message.text:
            case '/Throw_dice_1_times':
                num.append(str(random.randint(1, 6)))
            case '/Throw_dice_2_times':
                num.append(str(random.randint(1, 6)))
                num.append(str(random.randint(1, 6)))
            case '/Throw_dice_20':
                num.append(str(random.randint(1, 20)))

        msg_ids.append(
            bot.send_message(
                message.chat.id, "The number(s) dropped: " + ' '.join(num), reply_markup=buttons('dice')
            ).message_id
        )


    @bot.message_handler(commands=['timer'])
    def timer(message):
        msg_ids.append(
            bot.send_message(
                message.chat.id, f"⏲️I will count...", reply_markup=buttons('timer')
            ).message_id
        )


    @bot.message_handler(commands=['30_secs', '1_min', '5_mins'])
    def count(message):
        msg_ids.append(
            bot.send_message(
                message.chat.id, f"⏲️counting {' '.join(message.text[1:].split('_'))}"
            ).message_id
        )
        match message.text:
            case '/30_secs':
                sleep(30)
            case '/1_min':
                sleep(60)
            case '/5_mins':
                sleep(300)

        msg_ids.append(
            bot.send_message(
                message.chat.id, f"{' '.join(message.text[1:].split('_'))} passed⏲️", reply_markup=buttons('timer')
            ).message_id
        )


    @bot.message_handler(commands=['back'])
    def back(message):
        msg_ids.append(
            bot.send_message(
                message.chat.id, "back to main menu! 😊", reply_markup=buttons()
            ).message_id
        )


    @bot.message_handler(func=lambda message: True)
    def echo(message):
        msg_ids.append(
            bot.reply_to(
                message, message.text, reply_markup=buttons(0)
            ).message_id
        )


    bot.polling()

finally:
    print("done")
