import asyncio
import os

import threading
from asyncio import tasks
from concurrent.futures import thread

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import logics

#Bot Defined
load_dotenv()
tokens = [
    os.getenv('API_KEY_MAIN_BOT'),
    os.getenv('API_KEY_1'),
    os.getenv('API_KEY_2'),
    os.getenv('API_KEY_3'),
    os.getenv('API_KEY_4'),
    os.getenv('API_KEY_5'),
    os.getenv('API_KEY_6'),
    os.getenv('API_KEY_7'),
]
bots = []
dispatchers = []
for t in tokens:
    bots.append(Bot(t))
    dispatchers.append(Dispatcher(Bot(t)))








@dispatchers[0].message_handler(commands='menu')
async def menu(message: types.Message):
    await logics.show_menu(message)

@dispatchers[0].message_handler(commands='gay')
async def gay(message: types.Message):
    await logics.gay_random(message)
@dispatchers[0].callback_query_handler(text='Gay random')
async def gay(call: types.CallbackQuery):
    await logics.gay_random(call)

@dispatchers[0].message_handler(commands='mariiaR')
async def mariiaR(message: types.Message):
    await logics.mariia_random(message)
@dispatchers[0].callback_query_handler(text='Mariia random')
async def mariiaR(message: types.CallbackQuery):
    await logics.mariia_random(message)

@dispatchers[0].message_handler(commands='yuriiR')
async def mariiaR(message: types.Message):
    await logics.yurii_random(message)
@dispatchers[0].callback_query_handler(text='Yurii random')
async def mariiaR(message: types.CallbackQuery):
    await logics.yurii_random(message)

@dispatchers[0].message_handler(commands='ivanR')
async def mariiaR(message: types.Message):
    await logics.ivan_random(message)

@dispatchers[0].callback_query_handler(text='Ivan random')
async def mariiaR(message: types.CallbackQuery):
    await logics.ivan_random(message)

@dispatchers[0].message_handler(commands='alarm')
async def alarm(message: types.Message):
    await logics.alarm(message)

@dispatchers[0].message_handler(commands='secret_quote')
async def alarm(message: types.Message):
    photo = open('media/ivan_quote.jpg', 'rb')
    await bots[0].send_photo(message.from_user.id, photo)

#ECHO
@dispatchers[0].message_handler()
async def echo(message: types.Message):
    await logics.echo(message)

#BOT 2
@dispatchers[1].message_handler(commands='alarm')
async def alarm(message: types.Message):
    await logics.alarm(message)

@dispatchers[2].message_handler(commands='alarm')
async def alarm(message: types.Message):
    await logics.alarm(message)

@dispatchers[3].message_handler(commands='alarm')
async def alarm(message: types.Message):
    await logics.alarm(message)



async def run_bot_main(dp: Dispatcher):
    await dp.start_polling()
    print("Stopped")

async def main():
    await asyncio.gather(run_bot_main(dispatchers[0]),
                         run_bot_main(dispatchers[1]),
                         run_bot_main(dispatchers[2]),
                         run_bot_main(dispatchers[3]), )

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
