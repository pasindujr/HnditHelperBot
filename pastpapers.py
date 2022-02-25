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
        itembtn7 = types.KeyboardButton('/Maths_Papers')
        itembtn8 = types.KeyboardButton('/English1_Papers')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8)
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

    def dbms_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/dbms/2016-dbms-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/dbms/2016-dbms.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/dbms/2017-dbms-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/dbms/2017-dbms.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/dbms/2018-dbms-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/dbms/2019-dbms.pdf']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def web_development_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/web_dev/2016-web-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/web_dev/2016-web.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/web_dev/2017-web-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/web_dev/2017-web.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/web_dev/2018-web-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/web_dev/2018-web.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/web_dev/2019-web.pdf']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def maths_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/maths/2016-maths-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/maths/2017-maths.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/maths/2018-maths.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/maths/2019-maths.pdf']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def english1_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/english/2016-english.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/english/2017-english.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/first_semester/english/2019-english.pdf']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def second_sem_papers(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('/OOP_Papers')
        itembtn2 = types.KeyboardButton('/Multimedia_Papers')
        itembtn3 = types.KeyboardButton('/DSA_Papers')
        itembtn4 = types.KeyboardButton('/SAD_Papers')
        itembtn5 = types.KeyboardButton('/DCN_Papers')
        itembtn6 = types.KeyboardButton('/Stats_Papers')
        itembtn7 = types.KeyboardButton('/English2_Papers')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
        bot.send_message(message.chat.id, "Choose a subject:", reply_markup=markup)

    def oop_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/oop/2016-oop-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/oop/2016-oop.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/oop/2017-oop-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/oop/2017-oop.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/oop/2018-oop-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/oop/2018-oop.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/oop/2019-oop.pdf']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def multimedia_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/multimedia/2016-multimedia-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/multimedia/2016-multimedia.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/multimedia/2017-multimedia-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/multimedia/2017-multimedia.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/multimedia/2018-multimedia-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/multimedia/2018-multimedia.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/multimedia/2019-multimedia.pdf']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def dsa_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/dsa/2016-dsa-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/dsa/2016-dsa.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/dsa/2017-dsa-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/dsa/2017-dsa.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/dsa/2018-dsa-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/dsa/2018-dsa.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/dsa/2019-dsa.pdf']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def sad_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/sad/2016-sad-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/sad/2016-sad.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/sad/2017-sad-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/sad/2017-sad.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/sad/2018-sad-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/sad/2018-sad.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/sad/2019-sad.pdf']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def dcn_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/dcn/2016-dcn-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/dcn/2016-dcn.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/dcn/2017-dcn-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/dcn/2017-dcn.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/dcn/2018-dcn-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/dcn/2018-dcn.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/dcn/2019-dcn.pdf']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def stats_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/stats/2016-stats.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/stats/2017-stats-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/stats/2017-stats.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/stats/2018-stats-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/stats/2018-stats.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/stats/2019-stats.pdf']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def english2_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/english/2016-english2.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/english/2017-english2-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/english/2017-english2.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/second_semester/english/2019-english2.pdf']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def third_sem_papers(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('/OSCS_Papers')
        itembtn2 = types.KeyboardButton('/ITPM_Papers')
        itembtn3 = types.KeyboardButton('/Econ_Papers')
        itembtn4 = types.KeyboardButton('/RAD_Papers')
        itembtn5 = types.KeyboardButton('/Principles_of_SE_Papers')
        itembtn6 = types.KeyboardButton('/OOAD_Papers')
        itembtn7 = types.KeyboardButton('/English3_Papers')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
        bot.send_message(message.chat.id, "Choose a subject:", reply_markup=markup)

    def oscs_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/oscs/2015-oscs.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/oscs/2016-oscs.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/oscs/2019-oscs.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/oscs/2020-oscs.pdf']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def itpm_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/itpm/2015-itpm.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/itpm/2016-itpm.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/itpm/2019-itpm.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/itpm/2020-itpm.pdf']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def econ_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/econ/2015-econ-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/econ/2016-econ-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/econ/2017-econ-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/econ/2018-econ-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/econ/2019-econ-scheme.pdf']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def rad_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/rad/2015-rad-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/rad/2015-rad.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/rad/2016-rad-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/rad/2016-rad.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/rad/2017-rad-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/rad/2018-rad-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/rad/2019-rad-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/rad/2019-rad.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/rad/2020-rad.pdf']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def se_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/se/2015-se-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/se/2015-se.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/se/2016-se-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/se/2016-se.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/se/2018-se-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/se/2019-se-a.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/se/2019-se-b.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/se/2019-se-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/se/2020-se.pdf']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def ooad_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/ooad/2015-ooad.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/ooad/2016-ooad-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/ooad/2017-ooad-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/ooad/2018-ooad-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/ooad/2019-ooad-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/ooad/2019-ooad.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/ooad/2020-ooad.pdf']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def english3_papers(self, message):
        files = [
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/english/2016-english3-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/english/2017-english3-scheme.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/english/2017-english3.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/english/2018-english3.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/english/2019-english3.pdf',
            'https://github.com/pasindujr/HnditHelperBot_pdfs/raw/main/papers/third-semester/english/2020-english3.pdf']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)
