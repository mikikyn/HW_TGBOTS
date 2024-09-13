from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage



token = config('TOKEN')
bot=Bot(token=token)
dp = Dispatcher(bot=bot, storage=MemoryStorage())