from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot


async def quiz_1(message: types.Message):
    quiz_button = InlineKeyboardMarkup()
    button_qyuz_1 = InlineKeyboardButton('Дальше...',
                                         callback_data='button_1')
    quiz_button.add(button_qyuz_1)

    question = 'BMW or Mercedes?'
    answer = ['BMW', 'Mercedes', 'Lada']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Русскиц автопром!',
        open_period=60,
        reply_markup=quiz_button
    )


async def quiz_2(call: types.CallbackQuery):

    question = "Frontend or Backend"
    answer = ['Frontend', 'Backend', 'IOS']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation='Импостер -_-',
        open_period=60
    )


def register_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='button_1')