from aiogram import executor
from config import bot, dp
from handlers import (start,
                      echo,
                      commands)


start.register_start(dp=dp)
commands.register_commands(dp=dp)
echo.register_echo(dp=dp)






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)