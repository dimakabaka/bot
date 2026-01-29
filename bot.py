import os
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

HOST = os.getenv("ROUTER_HOST")

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    r = subprocess.run(["ping", "-c", "2", HOST], stdout=subprocess.DEVNULL)
    if r.returncode == 0:
        await update.message.reply_text("✅ Світло є, роутер онлайн")
    else:
        await update.message.reply_text("❌ Світла немає або інтернет відсутній")

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("check", check))
app.run_polling()
