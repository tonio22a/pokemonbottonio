import telebot 
from config import token
from logic import Pokemon

bot = telebot.TeleBot(token) 

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