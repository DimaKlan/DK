from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '7238596187:AAHMRec0jL-IC5XyushvG3lw33SiNfhupZs'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Кнопка для открытия WebView
    keyboard = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo(url="https://your-hosted-site.com")
    keyboard.add(types.InlineKeyboardButton(text="Open iGaming Hub", web_app=web_app))

    await message.answer("Welcome to the iGaming Hub!", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp)
