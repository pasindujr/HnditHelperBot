from telebot import *
import os
from dotenv import load_dotenv
import pastpapers

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

shootPapers = pastpapers.PastPapers()


@bot.message_handler(commands=['start', ])
def send_start(message):
    bot.send_message(message.chat.id, "Hello " + message.chat.first_name + "! Type /help to get started.")


@bot.message_handler(commands=['about'])
def send_about(message):
    bot.send_message(message.chat.id, "Designed by @pasindujr")


@bot.message_handler(commands=['help', ])
def send_help(message):
    bot.send_message(message.chat.id,
                     'Welcome to HNDIT Helper Bot. Here you can find past papers and notes for HNDIT subjects and exams. Do you need /notes or /papers? You can type or select a option.')


@bot.message_handler(commands=['papers'])
def select_sem(message):
    shootPapers.select_sem(message)


@bot.message_handler(commands=['1st_sem_papers'])
def first_sem_papers(message):
    shootPapers.first_sem_papers(message)


@bot.message_handler(commands=['PCA_Papers'])
def pca_papers(message):
    shootPapers.pca_papers(message)


@bot.message_handler(commands=['Computer_Hardware_Papers'])
def com_hardware_papers(message):
    shootPapers.com_hardware_papers(message)


@bot.message_handler(commands=['Structured_Programming_Papers'])
def structured_programming_papers(message):
    shootPapers.structured_programming_papers(message)


@bot.message_handler(commands=['DRO_Papers'])
def dro_papers(message):
    shootPapers.dro_papers(message)


@bot.message_handler(commands=['DBMS_Papers'])
def dbms_papers(message):
    shootPapers.dbms_papers(message)


@bot.message_handler(commands=['Web_Development_Papers'])
def web_development_papers(message):
    shootPapers.web_development_papers(message)


@bot.message_handler(commands=['Maths_Papers'])
def maths_papers(message):
    shootPapers.maths_papers(message)


@bot.message_handler(commands=['English1_Papers'])
def english1_papers(message):
    shootPapers.english1_papers(message)


@bot.message_handler(commands=['2nd_sem_papers'])
def second_sem_papers(message):
    shootPapers.second_sem_papers(message)


@bot.message_handler(commands=['OOP_Papers'])
def oop_papers(message):
    shootPapers.oop_papers(message)


@bot.message_handler(commands=['Multimedia_Papers'])
def multimedia_papers(message):
    shootPapers.multimedia_papers(message)


@bot.message_handler(commands=['DSA_Papers'])
def dsa_papers(message):
    shootPapers.dsa_papers(message)


@bot.message_handler(commands=['SAD_Papers'])
def sad_papers(message):
    shootPapers.sad_papers(message)


@bot.message_handler(commands=['DCN_Papers'])
def dcn_papers(message):
    shootPapers.dcn_papers(message)


@bot.message_handler(commands=['Stats_Papers'])
def stats_papers(message):
    shootPapers.stats_papers(message)


@bot.message_handler(commands=['English2_Papers'])
def english2_papers(message):
    shootPapers.english2_papers(message)


@bot.message_handler(commands=['3rd_sem_papers'])
def third_sem_papers(message):
    shootPapers.third_sem_papers(message)


@bot.message_handler(commands=['OSCS_Papers'])
def oscs_papers(message):
    shootPapers.oscs_papers(message)


@bot.message_handler(commands=['ITPM_Papers'])
def itpm_papers(message):
    shootPapers.itpm_papers(message)


@bot.message_handler(commands=['Econ_Papers'])
def econ_papers(message):
    shootPapers.econ_papers(message)


@bot.message_handler(commands=['RAD_Papers'])
def rad_papers(message):
    shootPapers.rad_papers(message)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, 'Invalid Input! Please send me a valid command which starts with "/".')


bot.infinity_polling()
