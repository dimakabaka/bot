import os
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from threading import Thread
from flask import Flask

HOST = os.getenv("ROUTER_HOST")
TOKEN = os.getenv("BOT_TOKEN")

# Telegram bot
async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    r = subprocess.run(["ping", "-c", "2", HOST], stdout=subprocess.DEVNULL)
    if r.returncode == 0:
        await update.message.reply_text("✅ Світло є, роутер онлайн")
    else:
        await update.message.reply_text("❌ Світла немає або інтернет відсутній")

app_bot = ApplicationBuilder().token(TOKEN).build()
app_bot.add_handler(CommandHandler("check", check))

def run_bot():
    app_bot.run_polling()

# Мінімальний веб-сервер для Render
web_app = Flask("web")
@web_app.route("/")
def home():
    return "Bot is running!"

# Запуск веб-сервера в окремому потоці
Thread(target=lambda: web_app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))).start()

# Запуск Telegram бота
run_bot()
