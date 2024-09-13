from config import bot, dp
from aiogram import executor, dispatcher
from handlers import start, echo, commands, quiz, fsm_store


start.register_start(dp)
commands.register_commands(dp)
quiz.register_quiz(dp)
fsm_store.register_fsm_store(dp)
echo.register_echo(dp)






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,)