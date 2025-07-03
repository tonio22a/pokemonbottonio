import telebot 
from config import token
from telebot import types
from logic import Pokemon, Wizard, Fighter
from random import randint


bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['eat'])
def eate(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    btn_orange = types.InlineKeyboardButton("🍊 Апельсин", callback_data="orange")
    btn_apple = types.InlineKeyboardButton("🍎 Яблоко", callback_data='apple')
    btn_banana = types.InlineKeyboardButton("🍌 Банан", callback_data="banana")

    markup.add(btn_orange, btn_apple, btn_banana)
    bot.reply_to(message, "🤤 На выбор есть три фрукта: Апельсин, Яблоко, Банан \n\n❓ Что выберешь для кормления?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    global botnumber, bal, playernumber
    user_id = call.from_user.id

    if call.data == "orange":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"🍊 Вы покормили вашего покемона апельсином!")

    elif call.data == "apple":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"🍎 Вы покормили вашего покемона яблоком!")

    elif call.data == "banana":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"🍌 Вы покормили вашего покемона бананом!")

@bot.message_handler(commands=['go'])
def start(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")

@bot.message_handler(commands=['info'])
def infocom(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.reply_to(message, f"Информация о вашем покемоне: \n\n{pokemon.info()}")
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "У вас еще нет покемона! Используйте команду /go, чтобы получить покемона")

# Исправленный вызов infinity_polling
bot.infinity_polling()