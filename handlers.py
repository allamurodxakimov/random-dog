from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from dog import get_dog_image
from cat import get_cat_image

def start(update: Update, context: CallbackContext):
    user = update.message.from_user

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='🐶'), KeyboardButton(text='🐈')]
        ],
        resize_keyboard=True
    )
    update.message.reply_html(
        text=f'Hello, {user.full_name}! Press one of the buttons.',
        reply_markup=keyboard
    )

def echo_dog(update: Update, context: CallbackContext):

    # bot = context.bot
    # bot.send_photo(chat_id = user.id, photo = get_dog_image, caption = '<b><i>Tasodifiy kuchukcha :(</i></b>',parse_mode='HTML')
    update.message.reply_photo(
        photo=get_dog_image(),
        caption= '<b><i>Tasodifiy kuchukcha :(</i></b>',
        parse_mode='HTML'
    )
def echo_cat(update: Update, context: CallbackContext):
    update.message.reply_photo(
        photo=get_cat_image(),
        caption = '<b><i>Tasodifiy mushukcha :(</i></b>',
        parse_mode="HTML"
    )
def echo_text(update: Update,context: CallbackContext):
    update.message.reply_html(
        text=update.message.text
    )
