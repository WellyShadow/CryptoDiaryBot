from distutils.log import error
from aiogram import types
from dispatcher import dp
import config
import re
from bot import BotDB
import bot
import api
import parse
import string



BotDB = BotDB('db.db')


@dp.message_handler(commands = "start")
async def start(message: types.Message):    
    await message.bot.send_message(message.from_user.id, "Добро пожаловать! Для начала работы нужно добавить Ваш адрес в базу даних в формате: /address *ваш адрес*")
#-------------------------------------------------------------------------------------------------------------------------#
@dp.message_handler(commands = ("address"))
async def start(message: types.Message):
    
    cmd_variants = (('/address'))
    address = message.text
    address = address.replace(cmd_variants, '').strip()
    
    
    
    for i in address: 
        x = bot.alfavit.find(i)
    if x ==-1: 
        await message.bot.send_message(message.from_user.id, "Не вірний формат адреси!") 
    else:   
        api.api(address)
         
        if api.api.statuscode == 200: 
            BotDB.add_record(message.from_user.id,address)
            await message.reply("✅ Адрес успешно добавлен")
        else: 
            await message.reply("❗Адреса не существует, попробуйте ввести еще раз")  
            
           
#-------------------------------------------------------------------------------------------------------------------------#           
@dp.message_handler(commands = ("get"), commands_prefix = "/!")
async def start(message: types.Message):
    
    records = BotDB.get_user_address(message.from_user.id)
    await message.reply(records)
#-------------------------------------------------------------------------------------------------------------------------#
@dp.message_handler(commands="balance")
async def start(message:types.Message):
    await message.reply('Назва монети|Кількість|(Ціна за одну)|Загальна собівартість')
    for coin in bot.address_content: 
        contract_ticker_symbol=coin.get('contract_ticker_symbol')
        balance=coin.get('balance')
        contract_decimals=coin.get('contract_decimals')
        quote_rate = coin.get('quote_rate')
        quote = coin.get('quote')
        #strquote_rate = str(quote_rate)
        intbalance = int(balance)
        intbalance = intbalance/10**(contract_decimals)
        
        bot.name.append( contract_ticker_symbol +'|'+ '%.3f'%intbalance +'|( '+'%.3f'%quote_rate+'$ )|'+'%.3f'%quote +'$')
    await message.answer('\n'.join(bot.name))
#-------------------------------------------------------------------------------------------------------------------------#
@dp.message_handler(commands = ("altseason"), commands_prefix = "/!")
async def start(message: types.Message):
    await message.answer("Індекс сезону альткоїнів")
    await message.answer(parse.altseason())
    if int(parse.altseason()) < 50:
        nameseason = "Біткоїн сезон"
    else: nameseason = "Альткоїн сезон"
    await message.answer(nameseason)
#-------------------------------------------------------------------------------------------------------------------------#
@dp.message_handler(commands = ("dominance"), commands_prefix = "/!")
async def start(message: types.Message):
    await message.answer("Домінація біткоїну та ефіріуму")
    await message.answer(parse.dominance())
#-------------------------------------------------------------------------------------------------------------------------#    
@dp.message_handler(commands = ("feargreed"), commands_prefix = "/!")
async def start(message: types.Message):
    await message.answer("Індекс страху та жадібнсті")
    await message.answer(parse.feargreed())
    if int(parse.feargreed()) < 25:
        await message.answer("надзвичайний страх")
    elif (int(parse.feargreed()) > 25) and (int(parse.feargreed()) < 47) :
        await message.answer("страх")
    elif (int(parse.feargreed()) >= 47) and (int(parse.feargreed()) < 54) :
        await message.answer("нейтрально")
    elif (int(parse.feargreed()) >=53) and (int(parse.feargreed()) < 75) :
        await message.answer("жадібність")
    elif (int(parse.feargreed()) >=75) and (int(parse.feargreed()) < 100) :
        await message.answer("надзвичайна жадібність")
#-------------------------------------------------------------------------------------------------------------------------# 
@dp.message_handler(commands = ("cap"), commands_prefix = "/!")
async def start(message: types.Message):
    await message.answer("Загальна капіталізація криптовалют")
    await message.answer(parse.cap())
#-------------------------------------------------------------------------------------------------------------------------#  
@dp.message_handler(commands = ("delete"), commands_prefix = "/!")
async def start(message: types.Message):
    
    BotDB.delete_record(message.from_user.id)
    await message.answer("✅ Адресу видалено")
#-------------------------------------------------------------------------------------------------------------------------#
@dp.message_handler(commands = ("help"), commands_prefix = "/!")
async def start(message: types.Message):
    
    BotDB.delete_record(message.from_user.id)
    await message.answer("""команда /start - привітання, та запит на ввід наступної команди /address
команда /address *адреса гаманця* - додає в базу даних адресу гаманця. Бот повідомляє про успішність команди. 
В базі даних зберігається порядковий номер користувача ботом, user-id користувача телегам та безпосередньо адреса
команда /delete - видаляє адресу за user-id користувача телегам, який відправив відповідний запит. Бот повідомляє про видаленя
команда /get - бот повертає адресу, яку зараз використовую користувач
команда /balance - бот повертає перелік всіх криптоактивів, які зберігаються за відповідною адресою ( Назва, кількість, ціна за одиницю, собівартість актива) 
команда /cap - бот повертає значення загальної капіталізації криптовалют на час запиту
команда /feargreed - бот повертає значення індексу страху та жадібності на час запиту
команда /dominance - бот повертає значення відсотку домінації біткоїну та ефіріуму від загальної капіталізації
команда /altseason - бот повертає індекс сезону альткоїнів (всі монети окрім біткоїна) """)
#-------------------------------------------------------------------------------------------------------------------------#