from aiogram import Bot
from aiogram.types import CallbackQuery

async def select_notebook(call: CallbackQuery, bot: Bot):
    brand = call.data.split('_')[0]
    model = call.data.split('_')[1]
    year = call.data.split('_')[2]
    answer = f"{call.message.from_user.first_name}, ваш выбор пал на ноутбук {brand}, модели {model} {year} года выпуска"
    await call.message.answer(answer)
    await call.answer()
