from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def quiz(message: types.Message):

    button_quiz = InlineKeyboardMarkup()
    button_quiz.add(InlineKeyboardButton("Дальше!",
                                         callback_data="button_1"))

    question = 'Месси или Роналду'

    answer = ['Месси', 'Роналду', 'Никто']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation='Ну ты даешь :)',
        open_period=60,
        reply_markup=button_quiz
    )

async def quiz_2(call: types.CallbackQuery):
    button_quiz = InlineKeyboardMarkup()
    button_quiz.add(InlineKeyboardButton("Дальше!",
                                         callback_data="button_2"))

    question = 'Фортнайт или пабг'

    answer = ['Fortnite', 'Pubg', 'CS-2', "Free fire",
              "Call of Duty", "Mobile legends"]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='Ты че не шаришь, позер',
        open_period=60,
        reply_markup=button_quiz
    )


async def quiz_3(call: types.CallbackQuery):
    button=InlineKeyboardMarkup()
    button.add(InlineKeyboardButton(text='next',callback_data='button_3'))

    question = 'Backend, Frontend or IOS developer'

    answer = ["Backend", "Frontend", "IOS"]

    await bot.send_photo(chat_id=call.from_user.id,
                         photo=open('media/good.jpg', 'rb'))

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='regular',
        allows_multiple_answers=True,
        explanation='Ты че не шаришь, позер',
        reply_markup=button
    )


async def quiz4(call:types.CallbackQuery):
    question='ps5 or nintendo'
    options=['ps5','nintendo']
    await bot.send_photo(chat_id=call.from_user.id,
                         photo=open('media/ho.jpeg','rb'))
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=options,
        is_anonymous=True,
        correct_option_id=1,
        type='regular',
        allows_multiple_answers=True
    )

def register_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='button_1')
    dp.register_callback_query_handler(quiz_3, text='button_2')
    dp.register_callback_query_handler(quiz4,text='button_3')