from config import bot, dp
from aiogram import types, Dispatcher


async def send_file(message: types.Message):
    await bot.send_document(chat_id=message.from_user.id,document=open('config.py','rb'))


def register_commands(dp: Dispatcher):
    dp.register_message_handler(send_file, commands=['file'])