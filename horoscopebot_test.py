import os
import telebot
import requests
from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from .env file
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Handler for /start and /hello
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Selamcanımbenimaşkımçiçeğim") #Your Welcome Messages
    bot.send_message(message.chat.id, "Astroloji boş beleş bi iş, ama sen yinede istiyosan /horoscope yaz bi \n(bu bot sadece biricik seviglmin kullanımına açıktır)")

# Function to get daily horoscope for a zodiac sign
def get_daily_horoscope(sign: str, day: str) -> dict:
    """Get daily horoscope for a zodiac sign.
    Keyword arguments:
    sign: str - Zodiac sign
    day: str - Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY
    Return: dict - JSON data
    """
    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params = {"sign": sign, "day": day}
    response = requests.get(url, params)
    return response.json()

# Function to fetch horoscope based on the user's input
def fetch_horoscope(message, sign):
    day = message.text
    horoscope = get_daily_horoscope(sign, day)
    data = horoscope["data"]
    horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\\n*Sign:* {sign}\\n*Day:* {data["date"]}'
    bot.send_message(message.chat.id, "al bakim")
    bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")

# Function to handle zodiac sign input and ask for the day
@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    text = "Burcunu versene \n*Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)

# Function to handle day input and fetch horoscope
def day_handler(message):
    sign = message.text
    text = "Hangi günü istiyosun güzel kadın \n*TODAY*, *TOMORROW*, *YESTERDAY*, veya bu şekil YYYY-MM-DD."
    sent_msg = bot.send_message(
        message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_msg, fetch_horoscope, sign.capitalize())

# Start polling the bot
bot.infinity_polling()
