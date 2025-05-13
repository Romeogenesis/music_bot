import asyncio
import logging
import sys
import config

from aiogram import Bot, Dispatcher, Router
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

from handlers import router

TOKEN = config.BOT_TOKEN
dp = Dispatcher()


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(router)

        
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())