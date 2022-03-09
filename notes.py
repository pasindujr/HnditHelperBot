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
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
        bot.send_message(message.chat.id, "Choose a subject:", reply_markup=markup)

    def pca_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1XtbU22s01G6UlQYMvjfFKCFFifL0Y6tK']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def com_hardware_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1ovahFEv7YemFWIHVdy6XtdS0UZEw4YIS',
                 'https://drive.google.com/uc?export=download&id=1w0LfmkYXCKD3-XeKFAn-F4AfPGwnyzlR']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def structured_programming_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1n65ncZ-wr-UzWhsgJQB_LR9yPVTCngcV']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def dro_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1jMbhwRef31t4KQjQuZW2rSVstjOKVFR-']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def dbms_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1-xT499d_VxrJ2NPOiPTOlyFuwxp7sqEG']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def web_development_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=19qF5eNHvT1u4B9RmOWUMiRPSTb7azbZS',
                 'https://drive.google.com/uc?export=download&id=1eepJZh6Vt891lM5QU0FdH84rkoLGf86s',
                 'https://drive.google.com/uc?export=download&id=1PYaFxRWgjSNRQJNwN9T-0NDTIogA2Adz']
        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def maths_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=13cndwTPbvbXlHSq7pEaHvRsHPm9fh3Hs']
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
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
        bot.send_message(message.chat.id, "Choose a subject:", reply_markup=markup)

    def oop_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1yNndva_1GpEixCXNND7EFrkb5Abnc-Th']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def multimedia_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1izzp1Snu9NtvXRX4IrfAcAB2ZSJFDJND',
                 'https://drive.google.com/uc?export=download&id=1q6CqX3pQ-ig_EtkcjJ6K1ngHnOAHo7KH',
                 'https://drive.google.com/uc?export=download&id=1Bcid2eqLp93NlJNj14rUX_Hpa3CZj-Th']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def dsa_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1dPmRPrIrdSprFXcOhw98gyKFwpWDAXAh']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def sad_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=15OKL0N5TdRRZJ7i7aSHFwG2W_MCV6zUT']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def dcn_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1Ulmzrhv5mo1YfVwA-h44rJHfvrXV7wXo',
                 'https://drive.google.com/uc?export=download&id=1tFgO_rrlYiz-aAcwAW_vyoMV1qOSdtnG']

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
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
        bot.send_message(message.chat.id, "Choose a subject:", reply_markup=markup)

    def oscs_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1rVW3iKtuqjvK3MpQBkYa-csIyWimnrnT',
                 'https://drive.google.com/uc?export=download&id=1lxemRO1tGVgzHNtRuscDSJaaeKQUIijl',
                 'https://drive.google.com/uc?export=download&id=1dEsAhZ-BWghAO5nRiNo_uc6t-AK-WiIM']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def itpm_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1cH-idR9FqO1QHx8KjbrEdcnE9qrK342e',
                 'https://drive.google.com/uc?export=download&id=1lW4l_w3DSSsbSvCNi977XcGB5_pBNn1g']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def econ_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1F_GVrVeDZ9AK2fCgyAvsKUZytbDQZMOv',
                 'https://drive.google.com/uc?export=download&id=1u7qKRFL8wKkQHyr0Qhua1e8eDjTIF7Sx']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def rad_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1r2btKpQd5oFMwZrqCpYNZ-0DtWLYKJA5',
                 'https://drive.google.com/uc?export=download&id=1wIF6la1zdSGMyJ6CRSuruVXCqGCLP3Z6']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def se_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1J6h6Us_02j2otFhQYhXYN3grr1sJ_kl1']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def ooad_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1E3l7NFlTl0-6FeKXydsVzNhStXF7Lzd0',
                 'https://drive.google.com/uc?export=download&id=1a6wt-LwvLi9avjH-ws4PkKAK5QlJ06K0']

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
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
        bot.send_message(message.chat.id, "Choose a subject:", reply_markup=markup)

    def com_architecture_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1VBh6_ZzruRZMXtYJdDHtt8HUsOpJicD8']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def enterprise_architecture_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1uWPPSWAE-7fv0CUjsLnA1-tZXiLWhG8X']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def foss_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1rY77kU2iJcgJ_Me5va7iYD63u0BHDecn']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def mobile_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1yFPXXYUFGkcjO5JNJTJogbORLIR3G9Tt']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def professional_issues_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1StlLaoE1864Jlo8xCSx6XndnloWW2GeB']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)

    def web_notes(self, message):
        files = ['https://drive.google.com/uc?export=download&id=1Ch22aqMwtKgv6xzYNtYr4sYkoqa4ckHS']

        bot.send_message(message.chat.id, str(len(files)) + " File/s Incoming...")

        for file in files:
            bot.send_document(message.chat.id, file)
