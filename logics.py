import random
import main

from aiogram import types
from random import randint
import keyboards
import json

num : int

async def echo(input):

    list = json.loads(str(input.chat))
    print(list['type'] == 'private')

    if list['type'] != 'private':

        if input.from_id == 332832026:  # Yurii
            await main.bots[1].send_message(chat_id='-1001928344452', text=input.text)
        if input.from_id == 395578806:  # Ivan
            await main.bots[2].send_message(chat_id='-1001928344452', text=input.text)
        if input.from_id == 341143604:  # Mariia
            await main.bots[3].send_message(chat_id='-1001928344452', text=input.text)
        if input.from_id == 485300860:  # Matvii
            await main.bots[4].send_message(chat_id='-1001928344452', text=input.text)
        if input.from_id == 642501963:  # Oles'
            await main.bots[5].send_message(chat_id='-1001928344452', text=input.text)
        if input.from_id == 264643446:  # Irina
            await main.bots[6].send_message(chat_id='-1001928344452', text=input.text)
        if input.from_id == 407790244:  # Mykita
            await main.bots[7].send_message(chat_id='-1001928344452', text=input.text)

async def show_menu(input):
    await input.answer(text='Choose from options below:', reply_markup=keyboards.buildMenu())
    await echo(input)

async def alarm(input):
    print(input.get_args)
    await input.answer(text='@zaberura @vidm0chka @shyrokyi_shershen '
                            '@m0tanka @kiselboroda @moxito_s_rahitom @oleskuchyn ')
    await echo(input)

async def gay_random(input):

    user_id = input.from_user.id
    first_name = get_custom_name(user_id)
    global num
    num = randint(1, 100)
    if num < 50:
        num += randint(0, 15)
    elif num < 90:
        num += randint(0, 9)
    elif num < 98:
        num += randint(0,3)

    text = '🫀: ' + first_name + ' на ' + str(num) + '% гей 🏳️‍🌈' \
           + '\n ' + get_gay_command_response(num, user_id)

    if type(input) is types.Message:
        await input.answer(text=text, reply_markup=keyboards.buildGamesMenu(), parse_mode='HTML')
        await echo(input)

    elif type(input) is types.CallbackQuery:
        await input.message.answer(text=text, reply_markup=keyboards.buildGamesMenu(), parse_mode='HTML')

async def mariia_random(input):

    list = ['Миті та Життя 😇', 'Бази й Каламбуру 🍉', 'Космосу та Хаосу 👾',
            'Справедливості та Спалаху 🔥', 'Блискавки й Наслідку 🌩', 'Посіпак й Володарів ⚜️',
            'Спокою та Гармонії ☮️', 'Ночі та Пітьми 🥷', 'всіх Марій 👑', ', просто Марія... 🙃']

    user_id = input.from_user.id
    first_name = get_custom_name(user_id)
    num = randint(0, len(list)-1)
    text = '🫀: ' + first_name + ', сьогодні ви \n<i> Марія ' + list[num] + '</i>'
    text.strip()

    if type(input) is types.Message:
        await input.answer(text=text, reply_markup=keyboards.buildGamesMenu(), parse_mode='HTML')
        await echo(input)

    elif type(input) is types.CallbackQuery:
        await input.message.answer(text=text, reply_markup=keyboards.buildGamesMenu(), parse_mode='HTML')


async def yurii_random(input):

    list = ['романтично', 'помірно', 'занадто', 'маніакально', 'лагідно', 'бурхливо', 'примарно', 'обурливо',
            'абсурдно', 'ніжно', 'ніхуя не']

    user_id = input.from_user.id
    first_name = get_custom_name(user_id)
    num = randint(0, len(list)-1)
    text = '🫀: ' + first_name + ', сьогодні ви\n<i> ' + list[num] + '-депресивний Юрій</i>'
    text.strip()

    if type(input) is types.Message:
        await input.answer(text=text, reply_markup=keyboards.buildGamesMenu(), parse_mode='HTML')
        await echo(input)

    elif type(input) is types.CallbackQuery:
        await input.message.answer(text=text, reply_markup=keyboards.buildGamesMenu(), parse_mode='HTML')


async def ivan_random(input):

    quotes = ['Один крок не туди і ти вже учениця найвеличнішої людини у цьому всесвіті',
            'Особисто мені здається, що треба більше дивитись аніме',
            'Тут або мозок занадто завантажений чимось (цікаво чим), або треба щось змінювати',
            'Асамадумадумадума пліз стенд ап пліз стенд ап',
            'Починати роботу, не проживши належним чином хоча б частину ранку - недопустима '
            'помилка, яка призводить до деградації тіла, підточує силу волі та розхитує тебе на шляху до мети',
            'Прогрес визначається в порівнянні з собою в минулому']
    quote = '💅: Цитата о Великого:\n' + random.choice(quotes) + ' 💎'

    if type(input) is types.Message:
        await input.answer(text=quote, reply_markup=keyboards.buildGamesMenu(), parse_mode='HTML')
        await echo(input)

    elif type(input) is types.CallbackQuery:
        await input.message.answer(text=quote, reply_markup=keyboards.buildGamesMenu(), parse_mode='HTML')

def get_custom_name(input):
    if input == 332832026:
        return 'Юрчик'
    if input == 341143604:
        return 'Марічка'
    if input == 395578806:
        return 'Іванко'
    if input == 485300860:
        return 'Матвійчик'
    if input == 642501963:
        return 'Лесик'
    if input == 264643446:
        return 'Іринка'
    if input == 407790244:
        return 'Микитка'

def get_gay_command_response(num, id):

    if num <= 10:
        text = '<i> - Сором родини... </i>'
    if 10 < num <= 50:
        text = '<i> - Тобі ще далеко до ідеалу </i>'
    if 50 < num <= 90:
        text = '<i> - Дай сраці сіна!</i>'
        if id == 395578806:
            text = '<i> - Дай по сраці Юрі!</i>'
    if 90 < num <= 99:
        text = '<i> - Поклін Отаману! </i>'
    if num == 100:
        text = '<i> -Справжнісінький гей-бог </i>\n🏳️‍🌈🏳️‍🌈🏳️‍🌈🏳️‍🌈🏳️‍🌈🏳️‍🌈'

    return text
