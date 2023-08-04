from aiogram import executor
from dispatcher import dp
import handlers
import asyncio
from db import BotDB

name = []
address_content = []
alfavit = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, skip_updates=True)