from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Bot
import os

start_router = Router()

async def get_start(message: Message, bot: Bot):
    await message.answer(f'Hello, {message.from_user.first_name}, glad to see you!')

async def get_photo(message: Message, bot: Bot):
    await message.answer(f"Picture's saved")
    file = await bot.get_file(message.photo[-1].file_id)
    storage_dir = os.path.join('storage')

    # Создаем директорию, если она не существует
    os.makedirs(storage_dir, exist_ok=True)

    file_path = os.path.join(storage_dir, 'photo.jpg')
    await bot.download_file(file.file_path, file_path)
