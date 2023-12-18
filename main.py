from aiogram import Bot, Dispatcher, executor, types

import subprocess
import os
from dotenv import load_dotenv

load_dotenv()
 
API_TOKEN = os.getenv('API_TOKEN')

chat_id = 545120434
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
 
async def on_startup(dp):
    await bot.send_message(chat_id=chat_id, text="Бот был запущен.")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ Эхо-бот от Olderestin!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")

@dp.message_handler(commands=['dota'])
async def open_dota(message: types.Message):
    try:
        subprocess.run(os.getenv('DOTA_PATH'), check=True)

        await message.reply("Dota 2 has been opened!")
    except subprocess.CalledProcessError as e:
        await message.reply(f"Error: {e}")
    except FileNotFoundError:
        await message.reply("Dota 2 application not found")
 
@dp.message_handler(commands=['shutdown'])
async def shutdown_computer(message: types.Message):
    try:
        os.system('shutdown /s /f /t 1')  # Выключение компьютера через 1 секунду
        await message.reply("Computer is shutting down...")

        await bot.send_message(chat_id=chat_id, text="Бот был выключен.")
    except Exception as e:
        await message.reply(f"Error: {e}")

        
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)