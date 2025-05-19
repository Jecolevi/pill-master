import os
from telegram.ext import Updater, CommandHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import logging

# Вставь свой токен от BotFather
TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError("Не установлен TELEGRAM_TOKEN!")

updater = Updater(TOKEN)
# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Что такое MediGuard CareAlert?", callback_data='info')],
        [InlineKeyboardButton("Как работает?", callback_data='how_it_works')],
        [InlineKeyboardButton("Преимущества", callback_data='benefits')],
        [InlineKeyboardButton("Заказать / Тестировать", callback_data='order')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Добро пожаловать!', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == 'info':
        query.edit_message_text(text="MediGuard CareAlert — умная таблетница, которая помогает принимать лекарства вовремя. Устройство подсвечивает ячейку, подает звуковые и световые сигналы, а при пропуске — отправляет SMS на заранее заданный номер.")
    elif query.data == 'how_it_works':
        text = (
            "1. Вы программируете время приема с помощью сенсорного дисплея.\n"
            "2. В назначенное время:\n"
            "   - Подсветка нужной ячейки\n"
            "   - Звуковой и световой сигнал\n"
            "   - Голосовое сообщение: 'Пора принять лекарство'\n"
            "3. Если лекарство не принято — отправляется SMS на заранее указанный номер."
        )
        query.edit_message_text(text=text)
    elif query.data == 'benefits':
        text = (
            "✅ Простое управление с сенсорным экраном\n"
            "✅ Подсветка ячеек\n"
            "✅ Звуковые и световые сигналы\n"
            "✅ Голосовое напоминание\n"
            "✅ SMS-оповещение при пропуске\n"
            "✅ Компактный размер (25x15x10 см)\n"
            "✅ Защищен патентом РФ RU 2 301 84 U1"
        )
        query.edit_message_text(text=text)
    elif query.data == 'order':
        text = (
            "Чтобы заказать или запросить тестирование, пожалуйста, отправьте нам:\n"
            "- Имя\n"
            "- Телефон\n"
            "- Email (по желанию)\n"
            "- Адрес доставки (если нужно)\n"
            "- Сообщение: 'Хочу протестировать', 'Хочу купить'"
        )
        query.edit_message_text(text=text)

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
