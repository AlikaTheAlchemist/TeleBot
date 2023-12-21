from aiogram import Bot, Dispatcher, executor, types
import requests
import random

f = open("/home/alika/telegram_bot/nick.txt", "r", encoding="UTF-8")
nick = f.read().split('\n')
f.close()

f = open("/home/alika/telegram_bot/smiles.txt", "r", encoding="UTF-8")
emoji = f.read().split('\n')
f.close()

f = open("/home/alika/telegram_bot/guilds.txt", "r", encoding="UTF-8")
guild = f.read().split('\n')
f.close()

f = open("/home/alika/telegram_bot/games2.txt", "r", encoding="UTF-8")
game = f.read().split('\n\n')
f.close()

API_TOKEN = '6774319760:AAEPzFzMEmna65rTdl6EMNLF-O29KzAlxVw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['generate'])
async def echo(message: types.Message):
	await message.answer(random.choice(nick))

@dp.message_handler(commands=['emoji'])
async def echo(message: types.Message):
        await message.answer(random.choice(emoji))

@dp.message_handler(commands=['guild'])
async def echo(message: types.Message):
        await message.answer(random.choice(guild))

@dp.message_handler(commands=['game_recomend'])
async def echo(message: types.Message):
        await message.answer(random.choice(game))



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.answer("Привет!\nЯ помогу тебе с созданием идеального никнейма для видеоигр!\nЕсли тебе нужно сгенерировать никнейм напиши /generate.\nЕсли тебе нужна идея для названия гильдии напиши /guild.\nЕсли у тебя уже есть идея для никнейма или гильдии напиши её и я помогу сделать её лучше и оригинальнее!\nДля просмотра всех команд напиши /help")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
   await message.answer("Список команд\n\n/generate - Сгенерировать никнейи \n/guild - Сгенерировать название гильдии \n/emoji - Прислать случайный эмодзи\n/game_recomend - Рекомендовать игру")




@dp.message_handler()
async def echo(message: types.Message):
	r = random.randint(1,6)
	emo = random.choice(emoji)
	match r:
		case 1:
			await message.answer(f'Идеи для улучшения твоего никнейма: \n\n\n>{message.text}<\n\n{message.text}{emo}\n\nx{message.text}x\n\n{emo}{message.text}\n\nX{message.text}X\n\n{emo}{message.text}{emo}')

		case 2:
			await message.answer(f'Идеи для улучшения твоего никнейма: \n\n\n+{message.text}+\n\n{message.text}{emo}\n\n={message.text}=\n\n{emo}{message.text}\n\n_{message.text}_\n\n{emo}{message.text}{emo}')

		case 3:
			await message.answer(f'Идеи для улучшения твоего никнейма: \n\n\n-{message.text}-\n\n{message.text}{emo}\n\n~{message.text}~\n\n{emo}{message.text}\n\n†{message.text}†\n\n{emo}{message.text}{emo}')

		case 4:
			await message.answer(f'Идеи для улучшения твоего никнейма: \n\n\n↑{message.text}↑\n\n{message.text}{emo}\n\n》{message.text}《\n\n{emo}{message.text}\n\n☆{message.text}☆\n\n{emo}{message.text}{emo}')

		case 5:
			await message.answer(f'Идеи для улучшения твоего никнейма: \n\n\n◇{message.text}◇\n\n{message.text}{emo}\n\n♤{message.text}♤\n\n{emo}{message.text}\n\n♧{message.text}♧\n\n{emo}{message.text}{emo}')

		case 6:
			await message.answer(f'Идеи для улучшения твоего никнейма: \n\n\n♡{message.text}♡\n\n{message.text}{emo}\n\n|{message.text}|\n\n{emo}{message.text}\n\n☞{message.text}☜\n\n{emo}{message.text}{emo}')
		case _:
			await message.answer(f'prolema')

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
