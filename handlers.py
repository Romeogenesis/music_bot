from aiogram import Router, F, types, Bot
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN, CHAT_ID
from keyboards import webAppKeyboard

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет! Это музыкальный бот.",
        reply_markup=webAppKeyboard()
    )