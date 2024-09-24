from aiogram.types import document
from config import bot, dp
from aiogram import types, Dispatcher



async def pin(message: types.Message):
    if message.chat.type != 'private':
        if message.reply_to_message:
            pinmessage = message.reply_to_message
            await bot.pin_chat_message(message.chat.id, pinmessage.message_id)
        else:
            await message.answer('Не получилось закрепить!')
    else:
        await message.answer('Работает только в группе!')

def register_group(dp: Dispatcher):
    dp.register_message_handler(pin, text='!pin')