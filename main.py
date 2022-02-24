from telebot import *
import os
from dotenv import load_dotenv
import pastpapers

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

papersObj = pastpapers.PastPapers()


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
    papersObj.select_sem(message)


@bot.message_handler(commands=['1st_sem_papers'])
def first_sem_papers(message):
    papersObj.first_sem_papers(message)


@bot.message_handler(commands=['PCA_Papers'])
def pca_papers(message):
    papersObj.pca_papers(message)


@bot.message_handler(commands=['Computer_Hardware_Papers'])
def com_hardware_papers(message):
    papersObj.com_hardware_papers(message)


@bot.message_handler(commands=['Structured_Programming_Papers'])
def structured_programming_papers(message):
    papersObj.structured_programming_papers(message)


@bot.message_handler(commands=['DRO_Papers'])
def dro_papers(message):
    papersObj.dro_papers(message)


@bot.message_handler(commands=['DBMS_Papers'])
def dbms_papers(message):
    papersObj.dbms_papers(message)


@bot.message_handler(commands=['Web_Development_Papers'])
def web_development_papers(message):
    papersObj.web_development_papers(message)


@bot.message_handler(commands=['Maths_Papers'])
def maths_papers(message):
    papersObj.maths_papers(message)


@bot.message_handler(commands=['English1_Papers'])
def english1_papers(message):
    papersObj.english1_papers(message)


@bot.message_handler(commands=['2nd_sem_papers'])
def second_sem_papers(message):
    papersObj.second_sem_papers(message)


@bot.message_handler(commands=['OOP_Papers'])
def oop_papers(message):
    papersObj.oop_papers(message)


@bot.message_handler(commands=['Multimedia_Papers'])
def multimedia_papers(message):
    papersObj.multimedia_papers(message)


@bot.message_handler(commands=['DSA_Papers'])
def dsa_papers(message):
    papersObj.dsa_papers(message)


@bot.message_handler(commands=['SAD_Papers'])
def sad_papers(message):
    papersObj.sad_papers(message)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, 'Invalid Input! Please send me a valid command which starts with "/".')


bot.infinity_polling()
