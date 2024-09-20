from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


async def reply_webapp(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)

    geeks_online = KeyboardButton('Geeks Online',
                                  web_app=types.WebAppInfo(url='https://online.geeks.kg/'))

    youtube = KeyboardButton('YouTube',
                             web_app=types.WebAppInfo(url='https://www.youtube.com/'))

    spotify = KeyboardButton('Spotify', web_app=types.WebAppInfo(url='https://open.spotify.com/'))

    jutsu = KeyboardButton('Jut.Su', web_app=types.WebAppInfo(url='https://jut.su/'))

    netflix = KeyboardButton('Netflix', web_app=types.WebAppInfo(url='https://www.netflix.com/kg/'))

    kinokrad = KeyboardButton('Kinokrad', web_app=types.WebAppInfo(url='https://kinokrad.ac/'))

    os_kg = KeyboardButton('OK KG', web_app=types.WebAppInfo(url='https://oc.kg/'))

    keyboard.add(geeks_online, youtube, spotify, jutsu, netflix, kinokrad, os_kg)

    await message.answer(text='WebApp кнопки: ', reply_markup=keyboard)


async def inline_webapp(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2, resize_keyboard=True)

    gitignore_io = InlineKeyboardButton('gitignore.io', web_app=types.WebAppInfo(
        url='https://www.toptal.com/developers/gitignore/'))

    translate = InlineKeyboardButton('Переводчик', web_app=types.WebAppInfo(url='https://translate.google.com/?sl=en&tl=ru&op=translate'))

    chat_gpt = InlineKeyboardButton('chat.gpt', web_app=types.WebAppInfo(url='https://chatgpt.com/'))

    kaktus_media = InlineKeyboardButton('kaktus.media', web_app=types.WebAppInfo(url='https://kaktus.media/'))

    keyboard.add(gitignore_io, translate, chat_gpt, kaktus_media)

    await message.answer(text='WebApp кнопки: ', reply_markup=keyboard)


def register_handlers_webapp(dp: Dispatcher):
    dp.register_message_handler(reply_webapp, commands=['reply_webapp'])
    dp.register_message_handler(inline_webapp, commands=['inline_webapp'])