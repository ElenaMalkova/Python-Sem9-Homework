from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv("tg_token")
app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("add", add_command))
app.add_handler(CommandHandler("mul", mul_command))
app.add_handler(CommandHandler("sub", sub_command))
app.add_handler(CommandHandler("div", div_command))

print('server start')

app.run_polling()