from telebot import *
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


class Timetables():
    def select_year(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('/1st_year_timetable')
        itembtn2 = types.KeyboardButton('/2nd_year_timetable')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id, "Choose a year:", reply_markup=markup)

    def first_year_timetable(self, message):
        files = ['https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/timetables/2020-1st-year.png']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_photo(message.chat.id, file, caption='2020 batch 1st year exam timetable')

    def second_year_timetable(self, message):
        files = ['https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/timetables/2020-2nd-year.png']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_photo(message.chat.id, file, caption='2019 batch 2nd year exam timetable')
