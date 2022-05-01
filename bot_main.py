import telebot
from telebot import types
import random
from random import *
import urllib
import datetime
import re
import time

bot = telebot.TeleBot("1512895977:AAFkP5guDgDuSnP8XdG4JTTo8BT3qEPNfj4")

i = -1
j = -1
list_of_messages_to_remind = []
dict_of_messages_to_remind = {}
#remind_message_format = re.compile()

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup()
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1= types.KeyboardButton("Thought of Bushido")
    item2= types.KeyboardButton("Thought of Nindo")
    item3= types.KeyboardButton("Make a prediction")
    item4 = types.KeyboardButton('Сделать напоминание')
    keyboard1.add(item1,item3, item2)

    bot.send_message(message.chat.id, 'Hello, young warrior. Which way will you choose? \nWay of honor or Way of shadows? \nI will teach you the way you have chosen.  ', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_message(message):
    class reply():
     def __init__(self, picture, text):
        self.picture = picture
        self.text = text
     def send_letter(self):
        bot.send_photo(message.chat.id, open("{}".format(self.picture), "rb"))
        bot.send_message(message.chat.id, "{}".format(self.text))

    message_number_busido = 0
    message_number_nindo = 0
    Mysl_1 = reply("AVE SAMURAI meme.png", "Remember, Samurai. Fight with honor.")
    Mysl_2 = reply("Samurai.jpg", "Path of Warrior is a path of honor.")
    Mysl_3 = reply("Samurai 2.jpg", "Reading Bushido and stabbing in the back is nonsense.")
    Mysl_4 = reply("ninja in adidas.jpg","Enhance your skills every day, as a true Samurai would do.")
    Mysl_5 = reply("ninja.jpg","Once chosen Nindo path, there is no way back to the Samurai path. ")
    Mysl_6 = reply("AVE KOKOREV RASENGAN meme.png", "Way of Shinobi is a way of being unseen...")
    Mysl_8 = reply("ninja irl.jpg", "Enough thoughts for today, shinobi.")
    Mysl_7 = reply("ninja in adidas.jpg","Remember, shinobi, you hesitate - you lose! (Isshin Ashina)")
    global Sovety_Busido
    Sovety_Busido = [Mysl_1, Mysl_2, Mysl_3, Mysl_4]
    global Sovety_Nindo
    Sovety_Nindo = [Mysl_5, Mysl_6, Mysl_7, Mysl_8]

    r = re.compile(r"[\d][\d]/[\d][\d]/[\d][\d] [\d][\d]:[\d][\d]+")

    if message.text == "Thought of Bushido" :
        global i
        if i == 3:
            bot.send_message(message.chat.id, "Enough Bushido thoughts for today")
        else:
         Sovety_Busido[i+1].send_letter()
         i += 1


    elif message.text == "Thought of Nindo":
        global j
        if j == 3:
            bot.send_message(message.chat.id, "Enough Nindo thoughts for today")
        else:
         Sovety_Nindo[j+1].send_letter()
         j += 1

    elif message.text == "Make a prediction":
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1= types.InlineKeyboardButton("Understand", callback_data='ясно')
        markup.add(item1)
        bot.send_message(message.chat.id, 'You are breathtaking!.', reply_markup=markup)

    elif message.text == "Сделать напоминание":

        markup = types.InlineKeyboardMarkup(row_width=3)
        item2 = types.InlineKeyboardButton("Сегодня", callback_data= "Сегодня")
        item3 = types.InlineKeyboardButton("Завтра", callback_data = "Завтра" )
        markup.add(item2, item3)
        bot.send_message(message.chat.id, 'На какую дату сделать напоминание, господин?\nПрошу удостоверьтесь что время и дата на вашем девайсе верны.',
                         reply_markup=markup)

    elif message.text.split()[0] == "Remind":
            #bot.send_message(message.chat.id, "izi")
            str1 = " "
            time_1 = int(message.text.split()[len(message.text.split())-1])
            last = len(message.text.split())-1
            text = str1.join(message.text.split()[1: last])
            time.sleep(time_1)
            bot.send_message(message.chat.id, text)

    elif bool(r.match(message.text)) == True:
        napominanie = re.split(" ", message.text)
        print(message.text)
        list_of_messages_to_remind.append(napominanie)
        print(list_of_messages_to_remind)
        bot.send_message(message.chat.id, "Хорош!")

    else:
          bot.send_message(message.chat.id, "I do not understand you.")



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'ясно':
                bot.send_message(call.message.chat.id, ')')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="You are breathtaking!.", reply_markup=None)
                bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text="Ну а хули)")

            elif call.data == "Сегодня":
                print("call data /Remind today")
                today_date = datetime.date.today()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Напишите сообщение которое нужно напомнить", reply_markup=None)





    except Exception as e:
        print(repr(e))

#for k in dict_of_messages_to_remind:
  #  if datetime.datetime.now().time() == dict_of_messages_to_remind[k]:
 #      bot.send_message(message.chat.id, "{}".format(dict_of_messages_to_remind.get(k, [default])))
for element in list_of_messages_to_remind:
    if element[0] == datetime.datetime.now().date():
        if element[1] == datetime.datetime.now().time():
            bot.send_message(message.chat.id, element[2])

bot.polling(none_stop=True)
