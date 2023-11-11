from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from pycoingecko import CoinGeckoAPI
from py_currency_converter import convert

cg = CoinGeckoAPI()

view = "Посмотреть курс"
usd = 'Конвертировать'
ablockchain = 'Прочитать'

# Эта кнопка для просмотра курса
def button_view_handler(update: Update, context: CallbackContext):
    price = cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd')
    update.message.reply_text(
        text=f"Bitcoin $ {price['bitcoin']['usd']:.2f}"
        + f"\nLitecoin $ {price['litecoin']['usd']:.2f}"
        + f"\nEthereum $ {price['ethereum']['usd']:.2f}"
        )

# Эта кнопка для конвертации
def button_ablockchain_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
    text='Привет!'
    )

# Эта кнопка для прочтения
def button_usd_handler(update: Update, context: CallbackContext):
    course = convert(amount=1, to=['RUB', 'EUR', 'UAH'])
    update.message.reply_text(
        text=f"1 USD to RUB {course['RUB']}"
        + f"\n1 USD to EUR {course['EUR']}"
        + f"\n1 USD to UAH {course['UAH']}"
    )
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == view:
        return button_view_handler(update=update, context=context)
    elif text == usd:
        return button_usd_handler(update=update, context=context)
    elif text == ablockchain:
        return button_ablockchain_handler(update=update, context=context)
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
            KeyboardButton(text=view),
            KeyboardButton(text=usd),
            KeyboardButton(text=ablockchain)
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text='Привет! Я готов тебя слушать!',
        reply_markup=reply_markup,
    )

def main():
    print('Start')
    updater = Updater(
    token='ВСТАВЬТЕ СВОЙ ТОКЕН',
    use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()
if __name__=='__main__':
    main()


