from aiogram import executor
from config import bot, dp
from handlers import start, commands, echo, quiz


start.register_start(dp)
commands.register_commands(dp)
quiz.register_quiz(dp)
echo.register_echo(dp)






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)