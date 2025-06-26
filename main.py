import telebot 
from config import token
from telebot import types
from logic import Pokemon


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
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.reply_to(message, pokemon.info())
        # Отправляем фото по URL
        bot.send_photo(message.chat.id, pokemon.img)
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


# Исправленный вызов infinity_polling
bot.infinity_polling()