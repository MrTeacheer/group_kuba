from config import bot,dp
from aiogram import executor
from handlers import start,echo,files


start.registr_start(dp)
files.register_file(dp)
echo.registr_echo(dp)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)