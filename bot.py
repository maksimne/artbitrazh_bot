import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from func_bot import accounts

# 0 - TikTok
# 1 - Instagram
# 2 - YouTube

AUTHOR = ""
API_TOKEN = "7611179707:AAE7HDYSC_CMywyAYF9YYS8Vk0AIrqkoARI"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Главное меню
isAuthorizated = False
auth_data = {
    "admin" : "admin001"
}


@dp.message(Command("start"))
async def login_handler(message: types.Message):
    await message.reply("Добро пожаловать. Для начала работы с ботом - авторизируйся при помощи команды /auth логин пароль!")

@dp.message(Command("auth"))
async def auth_handler(message: types.Message):
    global AUTHOR
    command = message.text.strip().split()
    if len(command) != 3:
        await message.reply("Неверный формат команды. Используйте: /auth login password")
        return
    _, login, password = command
    AUTHOR = login


    if login in auth_data and auth_data[login] == password:
        builder = ReplyKeyboardBuilder()
        builder.row(types.KeyboardButton(text="📱 Аккаунты"))
        builder.row(types.KeyboardButton(text="🎥 Контент"))
        builder.row(types.KeyboardButton(text="📊 Статистика"))
        builder.row(types.KeyboardButton(text="📈 Анализ рынка"))
        builder.row(types.KeyboardButton(text="✅ Чекер"))
        await message.answer(
            "Выберите действие:",
            reply_markup=builder.as_markup(resize_keyboard=True),
        )

    else:
        await message.reply("Неверный логин или пароль.")


@dp.message(Command("cr_acc"))
async def login_handler(message: types.Message):
    global AUTHOR
    t = message.text.strip().split()
    _, kol = t

    accounts.creating_account(author=AUTHOR, platform=0)

    await message.reply(f"kol - {kol}")



@dp.message(F)
async def under_menu(message: types.Message):
    flag = 0
    builder = ReplyKeyboardBuilder()
    if message.text == "Добавить аккаунты":
        await message.reply("Введите /cr_acc количество\nНапример /cr_acc 10")

    if message.text == "Выйти":
        flag = 1
        builder = ReplyKeyboardBuilder()
        builder.row(types.KeyboardButton(text="📱 Аккаунты"))
        builder.row(types.KeyboardButton(text="🎥 Контент"))
        builder.row(types.KeyboardButton(text="📊 Статистика"))
        builder.row(types.KeyboardButton(text="📈 Анализ рынка"))
        builder.row(types.KeyboardButton(text="✅ Чекер"))
        builder.row(types.KeyboardButton(text="Выйти"))
    if message.text == "📱 Аккаунты":
        flag = 1
        builder = ReplyKeyboardBuilder()
        builder.row(types.KeyboardButton(text="Добавить аккаунты"))
        builder.row(types.KeyboardButton(text="Просмотреть аккаунт"))
        builder.row(types.KeyboardButton(text="Удалить аккаунт"))
        builder.row(types.KeyboardButton(text="Подключить бизнес-аккаунт"))
        builder.row(types.KeyboardButton(text="Выйти"))

    elif message.text == "🎥 Контент":
        flag = 1
        builder = ReplyKeyboardBuilder()
        builder.row(types.KeyboardButton(text="Загрузить ролики для обработки"))
        builder.row(types.KeyboardButton(text="Уникализировать ролики"))
        builder.row(types.KeyboardButton(text="Настроить расписание автозалива"))
        builder.row(types.KeyboardButton(text="Выйти"))

    elif message.text == "📊 Статистика":
        flag = 1
        builder = ReplyKeyboardBuilder()
        builder.row(types.KeyboardButton(text="Выбрать платформу для анализа"))
        builder.row(types.KeyboardButton(text="Выбрать нишу (офферы, вертикали)"))
        builder.row(types.KeyboardButton(text="Просмотреть тренды и примеры"))
        builder.row(types.KeyboardButton(text="Выйти"))

    elif message.text == "📈 Анализ рынка":
        flag = 1
        builder = ReplyKeyboardBuilder()
        builder.row(types.KeyboardButton(text="Проверить аккаунт"))
        builder.row(types.KeyboardButton(text="Проверить несколько аккаунтов одновременно"))
        builder.row(types.KeyboardButton(text="Выйти"))

    elif message.text == "✅ Чекер":
        flag = 1
        builder = ReplyKeyboardBuilder()
        builder.row(types.KeyboardButton(text="Индивидуальная статистика по аккаунту"))
        builder.row(types.KeyboardButton(text="Общая статистика"))
        builder.row(types.KeyboardButton(text="Выйти"))
    if flag == 1:
        await message.answer(
            "Выберите действие:",
            reply_markup=builder.as_markup(resize_keyboard=True),
        )


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())