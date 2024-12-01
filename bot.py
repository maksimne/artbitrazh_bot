from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

API_TOKEN = "7715310992:AAEVhK0oo7EOpuKQqGoGzwz6z6l-65tJRXE"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Главное меню
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("📱 Аккаунты"))
main_menu.add(KeyboardButton("🎥 Контент"))
main_menu.add(KeyboardButton("📊 Статистика"))
main_menu.add(KeyboardButton("📈 Анализ рынка"))
main_menu.add(KeyboardButton("✅ Чекер"))

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать! Выберите действие:", reply_markup=main_menu)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
