from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build(buttons):
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 1

    for button in buttons:
        keyboard.add(InlineKeyboardButton(text=button, callback_data=button))

    return keyboard

def buildGamesMenu():
    keyboard = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton('Gay 🎲', callback_data='Gay random')
    button2 = InlineKeyboardButton('Mary 🎲', callback_data='Mariia random')
    button3 = InlineKeyboardButton('Yuri 🎲', callback_data='Yurii random')
    button4 = InlineKeyboardButton('Ivan 🎲', callback_data='Ivan random')
    keyboard.row(button1, button2)
    keyboard.row(button3, button4)
    return keyboard


def buildMenu():
    keyboard = InlineKeyboardMarkup()

    button1 = InlineKeyboardButton(text=' How Gay ', callback_data='How gay are you?')
    button2 = InlineKeyboardButton(text='Basic', callback_data='Basic')
    button3 = InlineKeyboardButton(text='Basic', callback_data='Basic')
    button4 = InlineKeyboardButton(text='Basic', callback_data='Basic')
    button5 = InlineKeyboardButton(text='Basic', callback_data='Basic')
    button6 = InlineKeyboardButton(text='Basic', callback_data='Basic')

    keyboard.add(button1, button2) \
        .add(button3, button4) \
        .add(button5, button6)

    return keyboard
