from aiogram import Bot, Dispatcher, executor
from get_lyrics import Genius
import logging
import config

from keyboard import Keyboard

logging.basicConfig(level=logging.INFO)
bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)
genius = Genius()

keyboard = Keyboard()


@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, 'Welcome')


@dp.message_handler(content_types=['text'])
async def msg(message):
    text = message.text.split(",")
    artist, song = text[0], text[1]
    try:
        lyrics = genius.get_lyrics(artist, song)
        if len(lyrics) > 4096:
            for x in range(0, len(lyrics), 4096):
                await bot.send_message(message.chat.id, lyrics[x:x + 4096])
        else:
            await bot.send_message(message.chat.id, lyrics)
    except Exception as e:
        await bot.send_message(message.chat.id,
                               "Sorry, We could not find any results, please make sure you wrote everything correct")


if __name__ == '__main__':
    print('program starting')
    executor.start_polling(dp, skip_updates=True)
