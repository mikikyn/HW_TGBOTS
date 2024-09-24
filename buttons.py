from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
# ===============================================================

start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)

start_buttons = KeyboardButton('/start')
mem_buttons = KeyboardButton('/mem')
mem_all_buttons = KeyboardButton('/mem_all')
music_buttons = KeyboardButton('/music')


start.add(start_buttons, mem_buttons, mem_all_buttons,
          music_buttons)

# ===============================================================

start_test = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
    ).add(
KeyboardButton('/start')
)

# ===============================================================

start_test_1 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
    )

start_test_1.add(
    KeyboardButton('/start'),
    KeyboardButton('/mem'),
    KeyboardButton('/mem_all'),
    KeyboardButton('/music')

)

# ===============----HOMEWORK-6-----========================

link='https://github.com/'
web=types.WebAppInfo(url=link)
urls=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text='github', web_app=types.WebAppInfo(url='https://github.com/')),
                                      types.InlineKeyboardButton(text='twitter', web_app=types.WebAppInfo(url='https://twitter.com/')),
                                      types.InlineKeyboardButton(text='linkedin', web_app=types.WebAppInfo(url='https://www.linkedin.com/')),
                                      types.InlineKeyboardButton(text='youtube', web_app=types.WebAppInfo(url='https://www.youtube.com/')),
                                      types.InlineKeyboardButton(text='amazon', web_app=types.WebAppInfo(url='https://www.amazon.com/')))




# ================================================================

cancel_button = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отмена'))

submit_button = ReplyKeyboardMarkup(resize_keyboard=True,
                                    row_width=2).add(KeyboardButton('Да'), KeyboardButton('Нет'))