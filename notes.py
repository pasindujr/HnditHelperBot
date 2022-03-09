from telebot import *
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


class Notes():
    def select_sem(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('/1st_sem_notes')
        itembtn2 = types.KeyboardButton('/2nd_sem_notes')
        itembtn3 = types.KeyboardButton('/3rd_sem_notes')
        itembtn4 = types.KeyboardButton('/4th_sem_notes')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
        bot.send_message(message.chat.id, "Choose a semester:", reply_markup=markup)

    def first_sem_notes(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('/PCA_notes')
        itembtn2 = types.KeyboardButton('/Computer_Hardware_notes')
        itembtn3 = types.KeyboardButton('/Structured_Programming_notes')
        itembtn4 = types.KeyboardButton('/DRO_notes')
        itembtn5 = types.KeyboardButton('/DBMS_notes')
        itembtn6 = types.KeyboardButton('/Web_Development_notes')
        itembtn7 = types.KeyboardButton('/Maths_notes')
        itembtn8 = types.KeyboardButton('/English1_notes')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8)
        bot.send_message(message.chat.id, "Choose a subject:", reply_markup=markup)

    def pca_notes(self, message):
        files = []
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def com_hardware_notes(self, message):
        files = []
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def structured_programming_notes(self, message):
        files = []
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def dro_notes(self, message):
        files = []
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def dbms_notes(self, message):
        files = []
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def web_development_notes(self, message):
        files = []
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def maths_notes(self, message):
        files = []
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def english1_notes(self, message):
        files = []
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def second_sem_notes(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('/OOP_notes')
        itembtn2 = types.KeyboardButton('/Multimedia_notes')
        itembtn3 = types.KeyboardButton('/DSA_notes')
        itembtn4 = types.KeyboardButton('/SAD_notes')
        itembtn5 = types.KeyboardButton('/DCN_notes')
        itembtn6 = types.KeyboardButton('/Stats_notes')
        itembtn7 = types.KeyboardButton('/English2_notes')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
        bot.send_message(message.chat.id, "Choose a subject:", reply_markup=markup)

    def oop_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def multimedia_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def dsa_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def sad_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def dcn_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def stats_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def english2_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def third_sem_notes(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('/OSCS_notes')
        itembtn2 = types.KeyboardButton('/ITPM_notes')
        itembtn3 = types.KeyboardButton('/Econ_notes')
        itembtn4 = types.KeyboardButton('/RAD_notes')
        itembtn5 = types.KeyboardButton('/Principles_of_SE_notes')
        itembtn6 = types.KeyboardButton('/OOAD_notes')
        itembtn7 = types.KeyboardButton('/English3_notes')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
        bot.send_message(message.chat.id, "Choose a subject:", reply_markup=markup)

    def oscs_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def itpm_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def econ_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def rad_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def se_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def ooad_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def english3_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def fourth_sem_notes(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('/Com_Architecture_notes')
        itembtn2 = types.KeyboardButton('/Enterprise_Architecture_notes')
        itembtn3 = types.KeyboardButton('/FOSS_notes')
        itembtn4 = types.KeyboardButton('/Mobile_notes')
        itembtn5 = types.KeyboardButton('/Professional_Issues_notes')
        itembtn6 = types.KeyboardButton('/Web_notes')
        itembtn7 = types.KeyboardButton('/English4_notes')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
        bot.send_message(message.chat.id, "Choose a subject:", reply_markup=markup)

    def com_architecture_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def enterprise_architecture_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def foss_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def mobile_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def professional_issues_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def web_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def english4_notes(self, message):
        files = []

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)
