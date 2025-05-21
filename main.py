import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    CallbackContext
)
import asyncio

# Настраиваем логирование
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
        query.edit_message_text(text="MediGuard CareAlert — умная таблетница, которая помогает принимать лекарства вовремя.")
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
            "- Адрес доставки (если нужно)"
        )
        query.edit_message_text(text=text)

async def main():
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise ValueError("Переменная окружения TELEGRAM_TOKEN не установлена.")

    # Создаём приложение
    application = ApplicationBuilder().token(token).build()

    # Инициализация
    await application.initialize()

    # Добавляем обработчики команд и кнопок
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Запуск
    await application.start()
    await application.updater.start_polling()

    # Остановка
    # await application.stop()

if __name__ == "__main__":
    asyncio.run(main())
