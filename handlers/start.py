from config import bot,dp
from aiogram import types, Dispatcher


async def start(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'hello {message.from_user.first_name}'
    )


def registr_start(dp: Dispatcher):
    dp.register_message_handler(start,commands=['start'])