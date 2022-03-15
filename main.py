from telebot import *
import os
from dotenv import load_dotenv
import pastpapers
import notes
import timetables

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

shootPapers = pastpapers.PastPapers()
shootNotes = notes.Notes()
shootTimetables = timetables.Timetables()


@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id,
                     "Hello " + message.chat.first_name + "! Type /help or tap the button left to typing area to get started.")


@bot.message_handler(commands=['about'])
def send_about(message):
    bot.send_message(message.chat.id,
                     "💡 Designed by @pasindujr from ATI Kegalle. The sole purpose of mine is to support the education of HNDIT students.\n💡 Do you think something is broken or have an amazing idea to improve me, please let my master know.\n💡 You can see my source code on GitHub.\nhttps://github.com/pasindujr/HnditHelperBot")

    bot.send_video(message.chat.id,
                   'https://drive.google.com/uc?export=download&id=1OLfS0BTxjy6cIIFJx6ugl5rK9SObK3zg', )


@bot.message_handler(commands=['help', ])
def send_help(message):
    bot.send_message(message.chat.id,
                     'Welcome to HNDIT Helper Bot. Here you can find past papers and notes for HNDIT subjects and exams. Do you need /notes or /papers? You can type or select an option.')


@bot.message_handler(commands=['changelog'])
def send_changelog(message):
    bot.send_message(message.chat.id,
                     "Inspect my commit history to see how I've been improved over time ⬇\nhttps://github.com/pasindujr/HnditHelperBot/commits/master")


# Below code handles past papers

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


@bot.message_handler(commands=['Principles_of_SE_Papers'])
def se_papers(message):
    shootPapers.se_papers(message)


@bot.message_handler(commands=['OOAD_Papers'])
def ooad_papers(message):
    shootPapers.ooad_papers(message)


@bot.message_handler(commands=['English3_Papers'])
def english3_papers(message):
    shootPapers.english3_papers(message)


@bot.message_handler(commands=['4th_sem_papers'])
def fourth_sem_papers(message):
    shootPapers.fourth_sem_papers(message)


@bot.message_handler(commands=['Com_Architecture_Papers'])
def com_architecture_papers(message):
    shootPapers.com_architecture_papers(message)


@bot.message_handler(commands=['Enterprise_Architecture_Papers'])
def enterprise_architecture_papers(message):
    shootPapers.enterprise_architecture_papers(message)


@bot.message_handler(commands=['FOSS_Papers'])
def foss_papers(message):
    shootPapers.foss_papers(message)


@bot.message_handler(commands=['Mobile_Papers'])
def mobile_papers(message):
    shootPapers.mobile_papers(message)


@bot.message_handler(commands=['Professional_Issues_Papers'])
def professional_issues_papers(message):
    shootPapers.professional_issues_papers(message)


@bot.message_handler(commands=['Web_Papers'])
def web_papers(message):
    shootPapers.web_papers(message)


@bot.message_handler(commands=['English4_Papers'])
def english4_papers(message):
    shootPapers.english4_papers(message)


# Below code handles notes.

@bot.message_handler(commands=['notes'])
def select_sem(message):
    shootNotes.select_sem(message)


@bot.message_handler(commands=['1st_sem_notes'])
def first_sem_notes(message):
    shootNotes.first_sem_notes(message)


@bot.message_handler(commands=['PCA_notes'])
def pca_notes(message):
    shootNotes.pca_notes(message)


@bot.message_handler(commands=['Computer_Hardware_notes'])
def com_hardware_notes(message):
    shootNotes.com_hardware_notes(message)


@bot.message_handler(commands=['Structured_Programming_notes'])
def structured_programming_notes(message):
    shootNotes.structured_programming_notes(message)


@bot.message_handler(commands=['DRO_notes'])
def dro_notes(message):
    shootNotes.dro_notes(message)


@bot.message_handler(commands=['DBMS_notes'])
def dbms_notes(message):
    shootNotes.dbms_notes(message)


@bot.message_handler(commands=['Web_Development_notes'])
def web_development_notes(message):
    shootNotes.web_development_notes(message)


@bot.message_handler(commands=['Maths_notes'])
def maths_notes(message):
    shootNotes.maths_notes(message)


@bot.message_handler(commands=['2nd_sem_notes'])
def second_sem_notes(message):
    shootNotes.second_sem_notes(message)


@bot.message_handler(commands=['OOP_notes'])
def oop_notes(message):
    shootNotes.oop_notes(message)


@bot.message_handler(commands=['Multimedia_notes'])
def multimedia_notes(message):
    shootNotes.multimedia_notes(message)


@bot.message_handler(commands=['DSA_notes'])
def dsa_notes(message):
    shootNotes.dsa_notes(message)


@bot.message_handler(commands=['SAD_notes'])
def sad_notes(message):
    shootNotes.sad_notes(message)


@bot.message_handler(commands=['DCN_notes'])
def dcn_notes(message):
    shootNotes.dcn_notes(message)


@bot.message_handler(commands=['3rd_sem_notes'])
def third_sem_notes(message):
    shootNotes.third_sem_notes(message)


@bot.message_handler(commands=['OSCS_notes'])
def oscs_notes(message):
    shootNotes.oscs_notes(message)


@bot.message_handler(commands=['ITPM_notes'])
def itpm_notes(message):
    shootNotes.itpm_notes(message)


@bot.message_handler(commands=['Econ_notes'])
def econ_notes(message):
    shootNotes.econ_notes(message)


@bot.message_handler(commands=['RAD_notes'])
def rad_notes(message):
    shootNotes.rad_notes(message)


@bot.message_handler(commands=['Principles_of_SE_notes'])
def se_notes(message):
    shootNotes.se_notes(message)


@bot.message_handler(commands=['OOAD_notes'])
def ooad_notes(message):
    shootNotes.ooad_notes(message)


@bot.message_handler(commands=['4th_sem_notes'])
def fourth_sem_notes(message):
    shootNotes.fourth_sem_notes(message)


@bot.message_handler(commands=['Com_Architecture_notes'])
def com_architecture_notes(message):
    shootNotes.com_architecture_notes(message)


@bot.message_handler(commands=['Enterprise_Architecture_notes'])
def enterprise_architecture_notes(message):
    shootNotes.enterprise_architecture_notes(message)


@bot.message_handler(commands=['FOSS_notes'])
def foss_notes(message):
    shootNotes.foss_notes(message)


@bot.message_handler(commands=['Mobile_notes'])
def mobile_notes(message):
    shootNotes.mobile_notes(message)


@bot.message_handler(commands=['Professional_Issues_notes'])
def professional_issues_notes(message):
    shootNotes.professional_issues_notes(message)


@bot.message_handler(commands=['Web_notes'])
def web_notes(message):
    shootNotes.web_notes(message)


# Below code handles exam timetables.

@bot.message_handler(commands=['timetables'])
def select_year(message):
    shootTimetables.select_year(message)


@bot.message_handler(commands=['1st_year_timetable'])
def first_year_timetable(message):
    shootTimetables.first_year_timetable(message)


@bot.message_handler(commands=['2nd_year_timetable'])
def second_year_timetable(message):
    shootTimetables.second_year_timetable(message)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id,
                     'Invalid command! Please send me a valid command which starts with "/" or try /help')


bot.infinity_polling()
