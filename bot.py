from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

API_TOKEN = "7340700679:AAEGFOcBangQUY3_NPkn9tKdamE7GWBjyMg"

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

isAuthorizated = False
auth_data = {
    "Andrey" : "aaa228bbb"
}


@dp.message_handler(commands=["start"])
async def login_handler(message: types.Message):
    await message.reply("Добро пожаловать. Для начала работы с ботом - авторизируйся при помощи команды /auth логин пароль!")

@dp.message_handler(commands=["auth"])
async def auth_handler(message: types.Message):
    # Получаем текст команды после /auth
    command = message.text.strip().split()

    # Проверяем правильность формата команды
    if len(command) != 3:
        await message.reply("Неверный формат команды. Используйте: /auth login password")
        return

    # Извлекаем логин и пароль
    _, login, password = command

    # Проверяем, есть ли логин в словаре и совпадает ли пароль
    if login in auth_data and auth_data[login] == password:
        await message.reply(f"Привет, {login}! Ты успешно авторизовался. Выбери действие:",reply_markup=main_menu)
        send_welcome(message);

    else:
        await message.reply("Неверный логин или пароль.")


# Под меню Аккаунты
@dp.message_handler(content_types=["text"])
async def under_menu(message: types.Message):
    if message.text == "Выйти":
        u_menu = main_menu
    if message.text == "📱 Аккаунты":
        u_menu = ReplyKeyboardMarkup(resize_keyboard=True)
        u_menu.add(KeyboardButton("Добавить аккаунт"))
        u_menu.add(KeyboardButton("Просмотреть аккаунты"))
        u_menu.add(KeyboardButton("Удалить аккаунт"))
        u_menu.add(KeyboardButton("Подключить бизнес-аккаунт"))

    elif message.text == "🎥 Контент":
        u_menu = ReplyKeyboardMarkup(resize_keyboard=True)
        u_menu.add(KeyboardButton("Загрузить ролики для обработки"))
        u_menu.add(KeyboardButton("Уникализировать ролики"))
        u_menu.add(KeyboardButton("Настроить расписание автозалива"))

    elif message.text == "📊 Статистика":
        u_menu = ReplyKeyboardMarkup(resize_keyboard=True)
        u_menu.add(KeyboardButton("Выбрать платформу для анализа"))
        u_menu.add(KeyboardButton("Выбрать нишу (офферы, вертикали)"))
        u_menu.add(KeyboardButton("Просмотреть тренды и примеры"))

    elif message.text == "📈 Анализ рынка":
        u_menu = ReplyKeyboardMarkup(resize_keyboard=True)
        u_menu.add(KeyboardButton("Проверить аккаунт"))
        u_menu.add(KeyboardButton("Проверить несколько аккаунтов одновременно"))

    elif message.text == "✅ Чекер":
        u_menu = ReplyKeyboardMarkup(resize_keyboard=True)
        u_menu.add(KeyboardButton("Индивидуальная статистика по аккаунту"))
        u_menu.add(KeyboardButton("Общая статистика"))

    u_menu.add(KeyboardButton("Выйти"))
    await message.reply("📱 Аккаунты", reply_markup=u_menu)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)