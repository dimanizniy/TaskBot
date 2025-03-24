from core.settings import settings
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from core.handlers.start import get_start, get_photo
from core.filters.is_contact import IsTrueContact
from core.handlers.contact import get_fake_contact, get_true_contact
from aiogram.filters import Command, CommandStart, Filter
from core.utils.commands import set_commands
from core.handlers.start import get_location
from core.handlers.start import get_inline
from core.handlers.callback import select_notebook

import asyncio
import logging

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text="Bot is started!")

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Bot is stoped!")

async def start():
    logging.basicConfig(level = logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_inline, Command(commands = 'inline'))
    dp.callback_query.register(select_notebook, F.data.startswith('msi'))
    dp.message.register(get_location, F.location)
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_fake_contact, F.contact)

    dp.message.register(get_photo, F.photo)
    dp.message.register(get_start, CommandStart)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())