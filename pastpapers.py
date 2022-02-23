from telebot import *
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


class PastPapers():
    def select_sem(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('/1st_sem_papers')
        itembtn2 = types.KeyboardButton('/2nd_sem_papers')
        itembtn3 = types.KeyboardButton('/3rd_sem_papers')
        itembtn4 = types.KeyboardButton('/4th_sem_papers')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
        bot.send_message(message.chat.id, "Choose a semester:", reply_markup=markup)

    def first_sem_papers(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('/PCA_Papers')
        itembtn2 = types.KeyboardButton('/Computer_Hardware_Papers')
        itembtn3 = types.KeyboardButton('/Structured_Programming_Papers')
        itembtn4 = types.KeyboardButton('/DRO_Papers')
        itembtn5 = types.KeyboardButton('/DBMS_Papers')
        itembtn6 = types.KeyboardButton('/Web_Development_Papers')
        itembtn7 = types.KeyboardButton('/Mathematics_Papers')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
        bot.send_message(message.chat.id, "Choose a subject:", reply_markup=markup)

    def pca_papers(self, message):
        files = ['https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/pca/2016-pca.pdf',
                 'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/pca/2017-pca.pdf',
                 'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/pca/2018-pca%20marking%20scheme.pdf',
                 'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/pca/2018-pca.pdf',
                 'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/pca/2019-pca.pdf']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def com_hardware_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/com_hardware/2016-hardware-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/com_hardware/2016-hardware.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/com_hardware/2017-hardware-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/com_hardware/2017-hardware.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/com_hardware/2018-hardware-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/com_hardware/2018-hardware.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/com_hardware/2019-hardware.pdf']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def structured_programming_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/structured-programming/2016-structured-programming.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/structured-programming/2017-structured-programming-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/structured-programming/2017-structured-programming.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/structured-programming/2018-structured-programming-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/structured-programming/2018-structured-programming.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/structured-programming/2019-structured-programming.pdf']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def dro_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/dro/2016-dro-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/dro/2016-dro.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/dro/2017-dro-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/dro/2017-dro.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/dro/2018-dro-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/dro/2018-dro.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/dro/2019-dro.pdf']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)
