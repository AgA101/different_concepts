import telebot
import credentials
from telebot import types
name = {}
surname = {}
age = {}
mail = {}
bot = telebot.TeleBot(credentials.TOKEN)
@bot.message_handler(commands=["start","help"])
def send(message):
    bot.reply_to(message, "/reg - команда для регистрации")

@bot.message_handler(commands=["reg"])
def exo(message):
    bot.send_message(message.from_user.id, "Привет! Давай познакомимся! Как тебя зовут?")
    bot.register_next_step_handler(message, reg_name)

def reg_name(message):
    global name
    name[message.from_user.id] = message.text
    bot.send_message(message.from_user.id, "Какая у вас фамилия?")
    bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
    global surname
    surname[message.from_user.id] = message.text
    bot.send_message(message.from_user.id, "Какая у вас электронная почта?")
    bot.register_next_step_handler(message, reg_mail)

def reg_mail(message):
    global mail
    mail[message.from_user.id] = message.text
    bot.send_message(message.from_user.id, "Сколько вам лет?")
    bot.register_next_step_handler(message, reg_age)

def reg_age(message):
    global age
    global name
    global surname
    global mail
    age[message.from_user.id] = message.text
    try:
        age[message.from_user.id] = int(message.text)
        statement = "Вам " + str(age[message.from_user.id]) + ", вас зовут " + str(
            name[message.from_user.id]) + " " + str(surname[message.from_user.id]) + " и ваша почта " + str(
            mail[message.from_user.id]) + " Все верно?"
        keyboard = types.InlineKeyboardMarkup()
        key_y = types.InlineKeyboardButton(text="Да", callback_data="yes")
        keyboard.add(key_y)
        key_n = types.InlineKeyboardButton(text="Нет", callback_data="no")
        keyboard.add(key_n)
        bot.send_message(message.from_user.id, text=statement, reply_markup=keyboard)

    except Exception:
        bot.send_message(message.from_user.id, "Вводите цифры!")
        bot.register_next_step_handler(message, reg_age)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Данные записаны")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Давай познакомимся заново! Как тебя зовут?")
        bot.register_next_step_handler(call.message, reg_name)
bot.polling()