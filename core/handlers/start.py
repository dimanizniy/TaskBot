from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Bot
import os
import json
from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard, get_reply_keyboard
from core.keyboards.inline import select_notebook

async def get_inline(message: Message, bot: Bot):
    await message.answer(f"Привет, {message.from_user.first_name}! Выбери ноутбук:",
                         reply_markup=select_notebook)

async def get_start(message: Message, bot: Bot):
    await message.answer(f'Привет, {message.from_user.first_name}, поработаем епта!',
                         reply_markup=get_reply_keyboard())


async def get_location(message: Message, bot: Bot):
    await message.answer(f"Локация отправлена!\r\a"
                         f"{message.location.latitude}\r\n{message.location.longitude}")


async def get_photo(message: Message, bot: Bot):
    await message.answer(f"Фото сохранено!")
    file = await bot.get_file(message.photo[-1].file_id)
    storage_dir = os.path.join('storage')

    # Создаем директорию, если она не существует
    os.makedirs(storage_dir, exist_ok=True)

    file_path = os.path.join(storage_dir, 'photo.jpg')
    await bot.download_file(file.file_path, file_path)
