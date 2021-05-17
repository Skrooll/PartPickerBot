from settings import token
from PartPicker import getCPUbyId, getMotherboardById, getMotherboard, getCPU, getCooling, getRAM, getVideocard, getPowersupply, getSSD, getHDD, getCase, getCoolingById, getRAMById, getVideocardById, getPowersupplyById, getSSDById, getHDDById, getCaseById
from partData import cpuData, motherboardData, coolingData, ramData, videocardData, powersupplyData, ssdData, hddData, caseData
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


bot = telebot.TeleBot(token)
users = {}
steps = {
    0: 'start', 
    1: 'cpu', 
    2: 'motherboard', 
    3: 'cooling', 
    4: 'ram', 
    5: 'videocard', 
    6: 'power_supply', 
    7: 'ssd',
    8: 'hdd',
    9: 'case',
    10:'finish',
}

# формирование итого, можешь менять то что после \n
def getFullData(userid):
    user = users[userid]
    price = 0
    mes = 'Here is your parts:'
    if user['cpu'] != None:
        part = getCPUbyId(user['cpu'])
        price += int(str(part[8]).replace(" ", ""))
        mes += f'\nCPU: {part[1]}, {part[10]}'
    if user['motherboard'] != None:
        part = getMotherboardById(user['motherboard'])
        price += int(str(part[4]).replace(" ", ""))
        mes += f'\nMotherboard: {part[1]}, {part[6]}'
    if user['cooling'] != None:
        part = getCoolingById(user['cooling'])
        price += int(str(part[4]).replace(" ", ""))
        mes += f'\nCooling: {part[1]}, {part[6]}'
    if user['ram'] != None:
        part = getRAMById(user['ram'])
        price += int(str(part[3]).replace(" ", ""))
        mes += f'\nRAM: {part[1]}, {part[5]}'
    if user['videocard'] != None:
        part = getVideocardById(user['videocard'])
        price += int(str(part[4]).replace(" ", ""))
        mes += f'\nVideocard: {part[1]}, {part[6]}'
    if user['power_supply'] != None:
        part = getPowersupplyById(user['power_supply'])
        price += int(str(part[3]).replace(" ", ""))
        mes += f'\nPower supply: {part[1]}, {part[5]}'
    if user['ssd'] != None:
        part = getSSDById(user['ssd'])
        price += int(str(part[4]).replace(" ", ""))
        mes += f'\nSSD: {part[1]}, {part[6]}'
    if user['hdd'] != None:
        part = getHDDById(user['hdd'])
        price += int(str(part[6]).replace(" ", ""))
        mes += f'\nHDD: {part[1]}, {part[8]}'
    if user['case'] != None:
        part = getCaseById(user['case'])
        price += int(str(part[4]).replace(" ", ""))
        mes += f'\nCase: {part[1]}, {part[6]}'
    mes += f'\nFull price: {price} rub'
    return mes

# генертор для кнопок "выбрать"
def gen_markup(i):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Выбрать", callback_data=f"{i}"))
    return markup

# удаление предыдущих вариантов
def deleteMessages(userid):
    for j in range(len(users[userid]['messages'])):
        bot.delete_message(userid, users[userid]['messages'][j].message_id)
    users[userid]['messages'] = []


# обработка шага
def processStep(userid, i):
    rec = users[userid]['recommended']
    # отмена первого шага
    if users[userid]['step'] == -1:
        deleteMessages(userid)
        users[userid]['step'] = 0
    # выдача процессоров, дальше аналогично
    elif users[userid]['step'] == 0:
        deleteMessages(userid)
        users[userid]['step'] = 1
        cpu = getCPU(rec=rec)
        for c in cpu:
            users[userid]['messages'].append(bot.send_message(userid, cpuData(c), reply_markup=gen_markup(c[0])))
    elif users[userid]['step'] == 1:
        deleteMessages(userid)
        users[userid]['cpu'] = i
        users[userid]['step'] = 2
        if i==None:
            motherboards = getMotherboard(socket=None, rec=rec)
        else:
            cpu = getCPUbyId(i)
            motherboards = getMotherboard(socket=cpu[2], rec=rec)
        for m in motherboards:
            users[userid]['messages'].append(bot.send_message(userid, motherboardData(m), reply_markup=gen_markup(m[0])))
    elif users[userid]['step'] == 2:
        deleteMessages(userid)
        users[userid]['motherboard'] = i
        users[userid]['step'] = 3
        coolings = getCooling(rec=rec)
        for c in coolings:
            users[userid]['messages'].append(bot.send_message(userid, coolingData(c), reply_markup=gen_markup(c[0])))
    elif users[userid]['step'] == 3:
        deleteMessages(userid)
        users[userid]['cooling'] = i
        users[userid]['step'] = 4
        rams = getRAM(rec=rec)
        for c in rams:
            users[userid]['messages'].append(bot.send_message(userid, ramData(c), reply_markup=gen_markup(c[0])))
    elif users[userid]['step'] == 4:
        deleteMessages(userid)
        users[userid]['ram'] = i
        users[userid]['step'] = 5
        videocards = getVideocard(rec=rec)
        for c in videocards:
            users[userid]['messages'].append(bot.send_message(userid, videocardData(c), reply_markup=gen_markup(c[0])))
    elif users[userid]['step'] == 5:
        deleteMessages(userid)
        users[userid]['videocard'] = i
        users[userid]['step'] = 6
        powersupplys = getPowersupply(rec=rec)
        for c in powersupplys:
            users[userid]['messages'].append(bot.send_message(userid, powersupplyData(c), reply_markup=gen_markup(c[0])))
    elif users[userid]['step'] == 6:
        deleteMessages(userid)
        users[userid]['power_supply'] = i
        users[userid]['step'] = 7
        ssds = getSSD(rec=rec)
        for c in ssds:
            users[userid]['messages'].append(bot.send_message(userid, ssdData(c), reply_markup=gen_markup(c[0])))
    elif users[userid]['step'] == 7:
        deleteMessages(userid)
        users[userid]['ssd'] = i
        users[userid]['step'] = 8
        hdds = getHDD(rec=rec)
        for c in hdds:
            users[userid]['messages'].append(bot.send_message(userid, hddData(c), reply_markup=gen_markup(c[0])))
    elif users[userid]['step'] == 8:
        deleteMessages(userid)
        users[userid]['hdd'] = i
        users[userid]['step'] = 9
        cases = getCase(rec=rec)
        for c in cases:
            users[userid]['messages'].append(bot.send_message(userid, caseData(c), reply_markup=gen_markup(c[0])))
    elif users[userid]['step'] == 9:
        deleteMessages(userid)
        users[userid]['case'] = i
        users[userid]['step'] = 10
        markup = ReplyKeyboardMarkup()
        markup.add('/new', '/recommended', '/help')
        users[userid]['messages'].append(bot.send_message(userid, getFullData(userid), reply_markup=markup))

# срабатывает при нажатии на кнопки "выбрать"
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    userid = call.message.chat.id
    i = call.data
    processStep(userid, i)

# обработчик команды /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    userid = message.chat.id
    markup = ReplyKeyboardMarkup()
    markup.add('/new', '/recommended', '/help')
    bot.send_message(userid, 'Привет!', reply_markup=markup)
    
# обработчик команды /help
@bot.message_handler(commands=['help'])
def help_handler(message):
    userid = message.chat.id
    markup = ReplyKeyboardMarkup()
    markup.add('/new', '/recommended', '/help')
    bot.send_message(userid, 'Выбери /new, если хочешь сделать новую сборку\nВыбери /recommended, если хочешь получить рекомендации по сборке', reply_markup=markup)    
    
# обработчик команды /recommended
@bot.message_handler(commands=['recommended'])
def rec_handler(message):
    userid = message.chat.id
    markup = ReplyKeyboardMarkup()
    markup.add('Очень бюджетная', 'Бюджетная', 'Средняя', 'Наилучшая')
    msg = bot.send_message(userid, 'Хорошо, теперь выбери тип сборки', reply_markup=markup) 
    bot.register_next_step_handler(msg, process_rec_step)

# обработчик выбора сборки
def process_rec_step(message):
    if message.text == 'Очень бюджетная':
        rec = 35
    elif message.text == 'Бюджетная':
        rec = 50
    elif message.text == 'Средняя':
        rec = 100
    elif message.text == 'Наилучшая':
        rec = 101
    else:
        rec = None
    userid = message.chat.id
    users[userid] = {
        'id': userid,    
        'recommended': rec,
        'step': 0,
        'start': None,
        'cpu': None,
        'motherboard': None,
        'cooling': None,
        'ram': None,
        'videocard': None,
        'power_supply': None,
        'ssd': None,
        'hdd': None,
        'case': None,
        'messages': [],
    }
    markup = ReplyKeyboardMarkup()
    markup.add('/more', '/skip', '/cancel')
    bot.send_message(userid, 'Ok, let\'s start', reply_markup=markup)
    processStep(userid, None)

# обработчик команды /new
@bot.message_handler(commands=['new'])
def new_handler(message):
    userid = message.chat.id
    users[userid] = {
        'id': userid,    
        'recommended': None,
        'step': 0,
        'start': None,
        'cpu': None,
        'motherboard': None,
        'cooling': None,
        'ram': None,
        'videocard': None,
        'power_supply': None,
        'ssd': None,
        'hdd': None,
        'case': None,
        'messages': [],
    }
    markup = ReplyKeyboardMarkup()
    markup.add('/more', '/skip', '/cancel')
    bot.send_message(userid, 'Ok, let\'s start', reply_markup=markup)
    processStep(userid, None)
        
# обработчки команды /cancel
@bot.message_handler(commands=['cancel'])
def cancel_handler(message):
    userid = message.chat.id
    user = users[userid]
    user[steps[user['step']]] = None
    users[userid]['step'] -=2
    if users[userid]['step'] > 0:
        processStep(userid, user[steps[user['step']]])
    else:
        processStep(userid, None)
        
# обработчик команды /skip
@bot.message_handler(commands=['skip'])
def skip_handler(message):
    userid = message.chat.id
    user = users[userid]
    if users[userid]['step'] > 0:
        processStep(userid, user[steps[user['step']]])
    else:
        processStep(userid, None)
    

bot.polling(none_stop=True)