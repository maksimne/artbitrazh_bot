import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder

API_TOKEN = "7611179707:AAE7HDYSC_CMywyAYF9YYS8Vk0AIrqkoARI"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Главное меню
isAuthorizated = False
auth_data = {
    "Andrey" : "aaa228bbb"
}


@dp.message(Command("start"))
async def login_handler(message: types.Message):
    await message.reply("Добро пожаловать. Для начала работы с ботом - авторизируйся при помощи команды /auth логин пароль!")

@dp.message(Command("auth"))
async def auth_handler(message: types.Message):
    # Получаем текст команды после /auth
    command = message.text.strip().split()
    if len(command) != 3:
        await message.reply("Неверный формат команды. Используйте: /auth login password")
        return

    # Извлекаем логин и пароль
    _, login, password = command

    # Проверяем, есть ли логин в словаре и совпадает ли пароль
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
        # send_welcome(message);

    else:
        await message.reply("Неверный логин или пароль.")


# Под меню Аккаунты
@dp.message(F)
async def under_menu(message: types.Message):

    if message.text == "Выйти":
        builder = ReplyKeyboardBuilder()
        builder.row(types.KeyboardButton(text="📱 Аккаунты"))
        builder.row(types.KeyboardButton(text="🎥 Контент"))
        builder.row(types.KeyboardButton(text="📊 Статистика"))
        builder.row(types.KeyboardButton(text="📈 Анализ рынка"))
        builder.row(types.KeyboardButton(text="✅ Чекер"))
        builder.row(types.KeyboardButton(text="Выйти"))
    if message.text == "📱 Аккаунты":
        builder = ReplyKeyboardBuilder()
        builder.row(types.KeyboardButton(text="Добавить аккаунт"))
        builder.row(types.KeyboardButton(text="Просмотреть аккаунты"))
        builder.row(types.KeyboardButton(text="Удалить аккаунт"))
        builder.row(types.KeyboardButton(text="Подключить бизнес-аккаунт"))
        builder.row(types.KeyboardButton(text="Выйти"))

    elif message.text == "🎥 Контент":
        builder = ReplyKeyboardBuilder()
        builder.row(types.KeyboardButton(text="Загрузить ролики для обработки"))
        builder.row(types.KeyboardButton(text="Уникализировать ролики"))
        builder.row(types.KeyboardButton(text="Настроить расписание автозалива"))
        builder.row(types.KeyboardButton(text="Выйти"))

    elif message.text == "📊 Статистика":
        builder = ReplyKeyboardBuilder()
        builder.row(types.KeyboardButton(text="Выбрать платформу для анализа"))
        builder.row(types.KeyboardButton(text="Выбрать нишу (офферы, вертикали)"))
        builder.row(types.KeyboardButton(text="Просмотреть тренды и примеры"))
        builder.row(types.KeyboardButton(text="Выйти"))

    elif message.text == "📈 Анализ рынка":
        builder = ReplyKeyboardBuilder()
        builder.row(types.KeyboardButton(text="Проверить аккаунт"))
        builder.row(types.KeyboardButton(text="Проверить несколько аккаунтов одновременно"))
        builder.row(types.KeyboardButton(text="Выйти"))

    elif message.text == "✅ Чекер":
        builder = ReplyKeyboardBuilder()
        builder.row(types.KeyboardButton(text="Индивидуальная статистика по аккаунту"))
        builder.row(types.KeyboardButton(text="Общая статистика"))
        builder.row(types.KeyboardButton(text="Выйти"))

    await message.answer(
        "Выберите действие:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())