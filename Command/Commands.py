from telegram.ext import CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from Help.Decorators import send_typing_action

#command /help
@send_typing_action
def help(update:Update,context:CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "List of commands available:\
        \n/start - To start the bot\
        \n/help - To show this message",quote=True
    )

#command is not found
@send_typing_action
def invalid_command(update:Update, context:CallbackContext):
    """
    This function is called when the user enters an invalid command.
    """
    update.message.reply_text("Invalid command. Type /help for a list of commands.",quote=True)

#command /start
@send_typing_action
def start(update:Update,context:CallbackContext):
    """Send a message when the command /start is issued."""
    first=update.effective_user.first_name
    update.message.reply_text('Hi! '+str(first)+' \n\nI am an Optical Character Recognizer Bot (OCR). \n\nJust send a clear image to me and i will recognize the text in the image and send it as a message!',quote=True)

#command /about
@send_typing_action
def about(update:Update,context:CallbackContext):
    """Send a message when the command /about is issued."""
    first=update.effective_user.first_name
    update.message.reply_text('Hi! '+str(first)+' \n\nI am Developer. Apu Riah  . \n\n if you want help @EngApuReah93BOT \n or Learn https://t.me/Info_Eng_Society !',quote=True)

#command /languge
@send_typing_action
def languge(update:Update,context:CallbackContext):
    """Send a message when the command /start is issued."""
    keyboard = [
        [InlineKeyboardButton("English ", callback_data='eng'), InlineKeyboardButton("Russian", callback_data='rus'),
         InlineKeyboardButton("Arabic", callback_data='ara')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    m = update.message.reply_text('Select Language : ', reply_markup=reply_markup, quote=True)
    chat_id=m.chat_id
    message_id=m.message_id
