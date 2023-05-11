import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '5989538305:AAH907pTMy25q89Mn584KLXrjHlHA4IKs0k'
openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)

def update(messages,role,content):
    messages.append({"role":role, "content":content})
    return messages

@dp.message_handler()
async def send(message: types.Message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message.text}
        ]
    )
    await message.answer(response['choices'][0]['message']['content'])

executor.start_polling(dp, skip_updates=True)