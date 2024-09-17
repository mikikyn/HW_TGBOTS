from config import bot
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def question1(message: types.Message):
    murkup=InlineKeyboardMarkup()
    b1=InlineKeyboardButton(text='next', callback_data='next1')
    murkup.add(b1)
    q='backend or frontend'
    v=['backend','frontend']
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=q,
        options=v,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='Молодчина!',
        open_period=60,
        reply_markup=murkup
    )

async def question2(call:types.CallbackQuery):
    murkup=InlineKeyboardMarkup()
    b1=InlineKeyboardButton(text='next', callback_data='next2')
    murkup.add(b1)
    q = 'nike or adidas'
    v = ['nike', 'adidas']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=q,
        options=v,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='Хммм....   ',
        open_period=60,
        reply_markup=murkup
    )
async def question3(call:types.CallbackQuery):

    q = 'cola or fanta'
    v = ['cola', 'fanta']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=q,
        options=v,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation='good choise!',
        open_period=60,
    )


def register_quiz(dp: Dispatcher):
    dp.register_message_handler(question1, commands=['quiz'])
    dp.register_callback_query_handler(question2, text='next1')
    dp.register_callback_query_handler(question3, text='next2')