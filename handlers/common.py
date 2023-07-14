
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

common_router = Router()


@common_router.message(Command('start'))
async def handle_start(message: Message, waifu_api):
    waifu = await waifu_api.get_waifu('cringe')
    await message.answer_photo(waifu)