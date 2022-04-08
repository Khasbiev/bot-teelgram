import telebot.types
from telebot import TeleBot,types
from binance.client import Client
import sqlite3
import ccxt
import time
import math
from dataBaseFunctions import get_id_users
from dataBaseFunctions import add_user_id
from dataBaseFunctions import InsertBinanceSecretApi
from dataBaseFunctions import InsertBinanceApi
from dataBaseFunctions import InsertFTXApi
from dataBaseFunctions import InsertFTXSecretApi
from dataBaseFunctions import InsertFTXSUBSCHET
from dataBaseFunctions import getAllUserInfo
from exchangeFunctions import get_cash
from exchangeFunctions import create_buy_order_market
from dataBaseFunctions import add_user_id_current_position
from dataBaseFunctions import InsertFirstExchange
from dataBaseFunctions import InsertFirstPositionSide
from dataBaseFunctions import InsertFirstPositionPair
from dataBaseFunctions import InsertFirstPositionSize
from dataBaseFunctions import InsertSecondPositionSide
from dataBaseFunctions import InsertSecondPositionPair
from dataBaseFunctions import InsertSecondPositionSize
from threading import Thread
from dataBaseFunctions import getAllPositionInfo
from dataBaseFunctions import InsertSecondExchange
from dataBaseFunctions import delete_positions
from exchangeFunctions import create_buy_order_marketBinance
# create_buy_order_limit()
# create_buy_order_market()

tgbot_key = list(open('settings.txt', 'r', encoding='utf-8').read().splitlines())[0]
bot = TeleBot(tgbot_key)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    user_id = message.from_user.id
    if message.text == '/start':
        allId = get_id_users()
        allId = [item[0] for item in allId]
        print(allId)
        name = message.from_user.username
        if user_id in allId:
            print('Yes')
            user_markup = telebot.types.ReplyKeyboardMarkup()
            user_markup.row('Профиль')
            user_markup.row('Торговля')
            user_markup.row('Добавить быстрые команды')
            bot.send_message(message.from_user.id,f'С возвращением, {name}',reply_markup=user_markup)
        else:
            lst = []
            lst.append(user_id)
            add_user_id(lst)
            user_markup = telebot.types.ReplyKeyboardMarkup()
            user_markup.row('Профиль')
            user_markup.row('Торговля')
            user_markup.row('Добавить быстрые команды(еще не поддерживается)')
            bot.send_message(message.from_user.id,f'Вы успешно авторизовались, {name}',reply_markup=user_markup)
    if message.text == 'Профиль':
        keyboard = types.InlineKeyboardMarkup()
        ftx = f'FTX-{user_id}'
        binance = f'Binance-{user_id}'
        checkdata = f'checkdata-{user_id}'
        key1 = types.InlineKeyboardButton(text='FTX',
                                          callback_data=ftx)  # кнопка «Да»
        keyboard.add(key1)
        key2 = types.InlineKeyboardButton(text='Binance',
                                          callback_data=binance)  # кнопка «Да»
        keyboard.add(key2)
        key2 = types.InlineKeyboardButton(text='Посмотреть данные',
                                          callback_data=checkdata)  # кнопка «Да»
        keyboard.add(key2)
        bot.send_message(message.from_user.id, 'Выберите:',reply_markup=keyboard)
    if message.text == 'Торговля':
        lstCurIdADd = []
        lstCurIdADd.append(user_id)
        try:
            delete_positions(user_id)
            add_user_id_current_position(lstCurIdADd)
        except:
            print('Уже имеется')
        FTXtrading = f'FTX-trading-{user_id}'
        BINANCEtrading = f'BINANCE-trading-{user_id}'
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='FTX', callback_data=FTXtrading)  # кнопка «Да»
        keyboard.add(key1)
        key2 = types.InlineKeyboardButton(text='Binance', callback_data=BINANCEtrading)  # кнопка «Да»
        keyboard.add(key2)
        bot.send_message(user_id, 'Выберите биржу для первой позиции:', reply_markup=keyboard)
        # keyboard = types.InlineKeyboardMarkup()
        # firsttrading = f'first-trading-{user_id}'
        # secondtrading = f'second-trading-{user_id}'
        # key1 = types.InlineKeyboardButton(text='1 вариант',
        #                                   callback_data=firsttrading)  # кнопка «Да»
        # keyboard.add(key1)
        # key2 = types.InlineKeyboardButton(text='2 вариант',
        #                                   callback_data=secondtrading)  # кнопка «Да»
        # keyboard.add(key2)
        # bot.send_message(message.from_user.id, 'Выберите:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker2(call):
    allId = get_id_users()
    allId = [item[0] for item in allId]
    for userId in allId:
        if call.data == f'FTX-{userId}':
            msg = bot.send_message(userId,'Введите API KEY:')
            bot.register_next_step_handler(msg, insertApiKeyFTX,userId)
        if call.data == f'Binance-{userId}':
            msg = bot.send_message(userId,'Введите API KEY:')
            bot.register_next_step_handler(msg,insertApiKeyBinance,userId)
        if call.data == f'checkdata-{userId}':
            info = getAllUserInfo(userId)
            infoLst = []
            for i in info[0]:
                infoLst.append(i)
            info = infoLst
            print(info)
            # print(len(info))
            msg = f' Данные аккаунта:\n\n FTX API KEY: {info[1]}\n\n FTX API SECRET: {info[2]}\n\n FTX Субсчет: {info[3]}\n\n Binance API KEY: {info[4]}\n\n Binance API SECRET: {info[5]}\n\n'
            bot.send_message(userId, msg)
        if call.data == f'FTX-trading-{userId}':
            InsertFirstExchange('FTX',userId)
            shortside = f'short{userId}'
            longside = f'long{userId}'
            keyboard = types.InlineKeyboardMarkup()
            key1 = types.InlineKeyboardButton(text='short', callback_data=shortside)  # кнопка «Да»
            keyboard.add(key1)
            key2 = types.InlineKeyboardButton(text='long', callback_data=longside)  # кнопка «Да»
            keyboard.add(key2)
            bot.send_message(userId, 'Выберите', reply_markup=keyboard)
        if call.data == f'BINANCE-trading-{userId}':
            InsertFirstExchange('BINANCE',userId)
            shortside = f'short{userId}'
            longside = f'long{userId}'
            keyboard = types.InlineKeyboardMarkup()
            key1 = types.InlineKeyboardButton(text='short', callback_data=shortside)  # кнопка «Да»
            keyboard.add(key1)
            key2 = types.InlineKeyboardButton(text='long', callback_data=longside)  # кнопка «Да»
            keyboard.add(key2)
            bot.send_message(userId, 'Выберите', reply_markup=keyboard)
        if call.data == f'short{userId}':
            msg = bot.send_message(userId, 'Введите инструмент:')
            side = 'sell'
            bot.register_next_step_handler(msg,gettoken,side, userId)
        if call.data == f'long{userId}':
            side = 'buy'
            msg = bot.send_message(userId, 'Введите инструмент:')
            bot.register_next_step_handler(msg, gettoken, side, userId)
        if call.data == f'FTX-trading-second-{userId}':
            InsertSecondExchange('FTX',userId)
            shortside = f'short2{userId}'
            longside = f'long2{userId}'
            keyboard = types.InlineKeyboardMarkup()
            key1 = types.InlineKeyboardButton(text='short', callback_data=shortside)  # кнопка «Да»
            keyboard.add(key1)
            key2 = types.InlineKeyboardButton(text='long', callback_data=longside)  # кнопка «Да»
            keyboard.add(key2)
            bot.send_message(userId, 'Выберите', reply_markup=keyboard)
        if call.data == f'BINANCE-second-trading-{userId}':
            InsertSecondExchange('BINANCE',userId)
            shortside2 = f'short2{userId}'
            longside2 = f'long2{userId}'
            keyboard = types.InlineKeyboardMarkup()
            key1 = types.InlineKeyboardButton(text='short', callback_data=shortside2)  # кнопка «Да»
            keyboard.add(key1)
            key2 = types.InlineKeyboardButton(text='long', callback_data=longside2)  # кнопка «Да»
            keyboard.add(key2)
            bot.send_message(userId, 'Выберите', reply_markup=keyboard)
        if call.data == f'short2{userId}':
            msg = bot.send_message(userId, 'Введите инструмент:')
            side = 'sell'
            bot.register_next_step_handler(msg,gettoken2,side, userId)
        if call.data == f'long2{userId}':
            side = 'buy'
            msg = bot.send_message(userId, 'Введите инструмент:')
            bot.register_next_step_handler(msg, gettoken2, side, userId)
        if call.data == f'first-trading-{userId}':
            print('1')
            msg =  bot.send_message(userId, 'Введите время(в минутах):')
            bot.register_next_step_handler(msg,getShag,userId)
        if call.data == f'second-trading-{userId}':
            print('2')

# def getShag(message, userId):
#     shag = message.text
#     bot.send_message(userId, 'Введите время:')
#     bot.register_next_step_handler(msg, getShag, userId)
def gettoken2(message,side,userId):
    pair = message.text
    msg = bot.send_message(userId, 'Введите сумму:')
    bot.register_next_step_handler(msg, endAddingFirstPosition2, side, userId,pair)

def endAddingFirstPosition2(message, side, userId,pair):
    size = message.text
    print('дошел сюда')
    InsertSecondPositionSide(side,userId)
    InsertSecondPositionPair(pair,userId)
    InsertSecondPositionSize(size,userId)
    print('done')
    msg = bot.send_message(userId, 'Введите время (в минутах), которое бот будет кидать по рынку:')
    bot.register_next_step_handler(msg, getShag, userId)
    # keyboard = types.InlineKeyboardMarkup()
    # firsttrading = f'first-trading-{userId}'
    # secondtrading = f'second-trading-{userId}'
    # key1 = types.InlineKeyboardButton(text='1 вариант',
    #                                   callback_data=firsttrading)  # кнопка «Да»
    # keyboard.add(key1)
    # key2 = types.InlineKeyboardButton(text='2 вариант',
    #                                   callback_data=secondtrading)  # кнопка «Да»
    # keyboard.add(key2)
    # bot.send_message(message.from_user.id, '1 вариант - ваша сумма сама делится на введенное время (ex. вы ввели 100к, 10мин => по рынку кидается 10к раз в минуту в обе позици)\n\n2 вариант - вводите время и шаг и ваша сумма умножается на шаг в течение времени(ex. вы ввели 1000$, шаг - 10 секунд, время - 5 минут => в течение 5 минут, каждые 10 секунд по рынку будет кидаться по 1000$ в обе позиции)\nВыберите:', reply_markup=keyboard)

def getShag(message, userId):
    vremya = message.text
    msg = bot.send_message(userId, 'Введите шаг(в секундах):')
    bot.register_next_step_handler(msg,createOrders, userId, vremya)

def createOrders(meassage,userId,vremya):
    shag = meassage.text
    Kolvo = int(vremya) * 60 / int(shag)
    lstInput = getAllUserInfo(userId)
    lst = []
    for i in lstInput[0]:
        lst.append(i)
    ftxApiKey = lst[1]
    ftxSecretKey = lst[2]
    ftxSubchet = lst[3]
    binanceApiKey = lst[4]
    binanceSecretKey = lst[5]
    positionInput = getAllPositionInfo(userId)
    lst = []
    for i in positionInput[0]:
        lst.append(i)
    FIRST_POSITION_EXCHANGE = lst[1]
    FIRST_POSITION_SIDE = lst[2]
    FIRST_POSITION_SIZE = lst[3]
    FIRST_POSITION_PAIR = lst[4]
    SECOND_POSITION_EXCHANGE = lst[5]
    SECOND_POSITION_SIDE = lst[6]
    SECOND_POSITION_SIZE = lst[7]
    SECOND_POSITION_PAIR = lst[8]
    for _ in  range(math.ceil(Kolvo)):
        if FIRST_POSITION_EXCHANGE == 'FTX' and SECOND_POSITION_EXCHANGE == 'FTX':
            Thread(target=createOrderFTX, args=(ftxApiKey, ftxSecretKey, ftxSubchet, FIRST_POSITION_SIDE, FIRST_POSITION_SIZE, userId, FIRST_POSITION_PAIR)).start()
            Thread(target=createOrderFTX, args=(
            ftxApiKey, ftxSecretKey, ftxSubchet, SECOND_POSITION_SIDE, SECOND_POSITION_SIZE, userId,
            SECOND_POSITION_PAIR)).start()
        elif FIRST_POSITION_EXCHANGE == 'FTX' and SECOND_POSITION_EXCHANGE == 'BINANCE':
            if SECOND_POSITION_SIDE == 'sell':
                SECOND_POSITION_SIDE = 'SELL'
            if SECOND_POSITION_SIDE == 'buy':
                SECOND_POSITION_SIDE = 'BUY'
            Thread(target=createOrderFTX, args=(
            ftxApiKey, ftxSecretKey, ftxSubchet, FIRST_POSITION_SIDE, FIRST_POSITION_SIZE, userId,
            FIRST_POSITION_PAIR)).start()
            Thread(target=create_buy_order_marketBinance, args=(
                binanceApiKey, binanceSecretKey, SECOND_POSITION_SIZE, SECOND_POSITION_PAIR, SECOND_POSITION_SIDE)).start()
        elif FIRST_POSITION_EXCHANGE == 'BINANCE' and SECOND_POSITION_EXCHANGE == 'FTX':
            if FIRST_POSITION_SIDE == 'sell':
                FIRST_POSITION_SIDE = 'SELL'
            if FIRST_POSITION_SIDE == 'buy':
                FIRST_POSITION_SIDE = 'BUY'
            Thread(target=create_buy_order_marketBinance, args=(
                binanceApiKey, binanceSecretKey, FIRST_POSITION_SIZE, FIRST_POSITION_PAIR, FIRST_POSITION_SIDE)).start()
            Thread(target=createOrderFTX, args=(
                ftxApiKey, ftxSecretKey, ftxSubchet, SECOND_POSITION_SIDE, SECOND_POSITION_SIZE, userId,
                SECOND_POSITION_PAIR)).start()
        elif FIRST_POSITION_EXCHANGE == 'BINANCE' and SECOND_POSITION_EXCHANGE == 'BINANCE':
            if SECOND_POSITION_SIDE == 'sell':
                SECOND_POSITION_SIDE = 'SELL'
            if SECOND_POSITION_SIDE == 'buy':
                SECOND_POSITION_SIDE = 'BUY'
            if FIRST_POSITION_SIDE == 'sell':
                FIRST_POSITION_SIDE = 'SELL'
            if FIRST_POSITION_SIDE == 'buy':
                FIRST_POSITION_SIDE = 'BUY'
            Thread(target=create_buy_order_marketBinance, args=(
                binanceApiKey, binanceSecretKey, FIRST_POSITION_SIZE, FIRST_POSITION_PAIR, FIRST_POSITION_SIDE)).start()
            Thread(target=create_buy_order_marketBinance, args=(
                binanceApiKey, binanceSecretKey, SECOND_POSITION_SIZE, SECOND_POSITION_PAIR, SECOND_POSITION_SIDE)).start()
        time.sleep(int(shag))

def gettoken(message,side,userId):
    pair = message.text
    msg = bot.send_message(userId, 'Введите сумму:')
    bot.register_next_step_handler(msg, endAddingFirstPosition, side, userId,pair)
    # firsttrading = f'first-trading-{userId}'
    # secondtrading = f'second-trading-{userId}'
    # keyboard = types.InlineKeyboardMarkup()
    # key1 = types.InlineKeyboardButton(text='1 вариант(ex. каждые 10 секунд кидает по рынку 200$)',
    #                                   callback_data=firsttrading)  # кнопка «Да»
    # keyboard.add(key1)
    # key2 = types.InlineKeyboardButton(text='2 вариант(ex. 10 минут кидает по рынку 10000$ - т.е. сам делит время)',
    #                                   callback_data=secondtrading)  # кнопка «Да»
    # keyboard.add(key2)
    # bot.send_message(message.from_user.id, 'Выберите:', reply_markup=keyboard)

def endAddingFirstPosition(message, side, userId,pair):
    size = message.text
    InsertFirstPositionSide(side,userId)
    InsertFirstPositionPair(pair,userId)
    InsertFirstPositionSize(size,userId)
    FTXtrading2 = f'FTX-trading-second-{userId}'
    BINANCEtrading2 = f'BINANCE-second-trading-{userId}'
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='FTX', callback_data=FTXtrading2)  # кнопка «Да»
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Binance', callback_data=BINANCEtrading2)  # кнопка «Да»
    keyboard.add(key2)
    bot.send_message(userId, 'Выберите биржу для второй позиции:', reply_markup=keyboard)


def createOrderFTX(ftxApiKey,ftxSecretKey, ftxSubchet, side,size, userId,pair):
    try:
        exchange = ccxt.ftx({
            'apiKey': ftxApiKey,
            'secret': ftxSecretKey,
            'enableRateLimit': True}
        )
        exchange.headers = {'FTX-SUBACCOUNT': ftxSubchet, }
        msg = create_buy_order_market(exchange, pair, side, size)
        mstg = f'{side} Order Created'
        # msg = bot.send_message(userId, mstg)
    except Exception as e:
        print(e)
        bot.send_message(userId, 'Ошибка. Проверьте корректность введенных данных и повторите попытку')

def insertApiKeyFTX(message,name):
    print(message.text)
    print(name)

    ApiKey = message.text
    msg = bot.send_message(name, 'Введите API SECRET:')
    bot.register_next_step_handler(msg, insertSecretApiKeyFTX,name,ApiKey)

def insertSecretApiKeyFTX(message,name,ApiKey):
    print(message.text)
    print(name)
    ApiSecretKey = message.text
    msg = bot.send_message(name, 'Введите субсчет')
    bot.register_next_step_handler(msg, insertSUBSCHET, name,ApiKey, ApiSecretKey)

def insertSUBSCHET(message,name,ApiKey, ApiSecretKey):
    try:
        SUBSCHET = message.text
        exchange = ccxt.ftx({
            'apiKey': ApiKey,
            'secret': ApiSecretKey,
            'enableRateLimit': True}
        )
        exchange.headers = {'FTX-SUBACCOUNT': SUBSCHET, }
        sidet_only = True
        balance = get_cash(exchange)
        print(balance)
        outBalance = ''
        for _ in balance:
            outBalance += '\n' + _
        print(outBalance)
        msg = bot.send_message(name, f'Успешно записано. \nВаш баланс: {outBalance}')
        InsertFTXApi(ApiKey, name)
        InsertFTXSecretApi(ApiSecretKey, name)
        InsertFTXSUBSCHET(SUBSCHET, name)
    except:
        bot.send_message(name, 'Ошибка. Проверьте корректность введенных данных и повторите попытку')

def insertApiKeyBinance(message,name):
    print(message.text)
    print(name)
    InsertBinanceApi(message.text, name)
    msg = bot.send_message(name, 'Введите API SECRET:')
    bot.register_next_step_handler(msg, insertSecretApiKeyBinance,name)

def insertSecretApiKeyBinance(message,name):
    print(message.text)
    print(name)
    InsertBinanceSecretApi(message.text, name)
    bot.send_message(name, 'Успешно записано')




try:
    sqlite_connection = sqlite3.connect('data_info.db')
    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    sqlite_crypto_users = '''create table if not exists usersIds (NAME USERID UNIQUE,FTX_API_KEY TEXT, FTX_SECRET_KEY TEXT,SUBSCHET TEXT, BINANCE_API_KEY TEXT, BINANCE_SECRET_KEY TEXT);'''
    cursor.execute(sqlite_crypto_users)
    sqlite_crypto_users = '''create table if not exists currentPostion (NAME USERID UNIQUE,FIRST_POSITION_EXCHANGE TEXT, FIRST_POSITION_SIDE TEXT, FIRST_POSITION_SIZE TEXT,FIRST_POSITION_PAIR TEXT, SECOND_POSITION_EXCHANGE, SECOND_POSITION_SIDE TEXT, SECOND_POSITION_SIZE TEXT, SECOND_POSITION_PAIR TEXT);'''
    cursor.execute(sqlite_crypto_users)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")

while True:
    try:
        bot.infinity_polling()
    except:
        continue
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
