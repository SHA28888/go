import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = "https://your-vercel-app.vercel.app/webhook"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hei! Jeg er en Telegram-bot.")

def bot_link(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Bot-lenke: http://t.me/Plugtaalkbot")

def group_link(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Gruppelenke: https://t.me/+FAIgPPXFkj04MmE0")

def bot_something(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("This is the response for /bot_something command.")

def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("botlink", bot_link))
    dispatcher.add_handler(CommandHandler("grouplink", group_link))
    dispatcher.add_handler(CommandHandler("bot_something", bot_something))

    # Sett opp webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(os.getenv("PORT", "5000")),
                          url_path=BOT_TOKEN)
    updater.bot.set_webhook(WEBHOOK_URL + BOT_TOKEN)

if __name__ == "__main__":
    main()
