from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging
import telegram.ext.filters
from Config import BOT_TOKEN as token
from Command.Commands import start as start
from Command.Commands import help
from Command.Commands import invalid_command
from Handlers.Callback_Query import button_click
from Handlers.Languge_Query import extract_image


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
   # updater = Updater("6515139562:AAFjM1fQ-uuMVFLrwEVA7k9SV6liRujIvHo",use_context=True)
    updater = Updater(token, use_context=True)
    updater.bot.set_my_commands([("start","start the bot"),("help","Get list of commands")])
    dp=updater.dispatcher
    dp.add_handler(CommandHandler('start',start,run_async=True))
    dp.add_handler(CommandHandler('help',help,run_async=True))
    dp.add_handler(MessageHandler(Filters.photo, extract_image,run_async=True))
    dp.add_handler(MessageHandler(Filters.command,invalid_command,run_async=True))
    dp.add_handler(CallbackQueryHandler(button_click,run_async=True))

    updater.start_polling(drop_pending_updates=True)
    print("Bot is running")
    updater.idle()
if __name__ == '__main__':
    main();