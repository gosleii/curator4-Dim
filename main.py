import telebot

botik = telebot.TeleBot('6567038969:AAFeCDAdTjoX7Awb5ZEooz2aEf1CQ4J6vkU')

@botik.message_handler(commands = ['start'])
def main(message):
    botik.send_message(message.chat.id, '*Привет, друг!*''\n*Я Бот Математик. Что я умею:*''\n\n/equations  -  формулы сокращённого умножения''\n/square  -  формула площади квадрата''\n/triangle  -  формула площади  треугольника''\n/rectangle  -  формула площади прямоугольника''\n/functions  -  основные функции в тригонометрии'
                                        '\n/mathsite  -  сайт математики', parse_mode = 'Markdown')

@botik.message_handler(commands = ['equations'])
def main(message):
    botik.send_message(message.chat.id, 'Формулы сокращённого умножения:''\n(a + b)^2 = a^2 + 2ab + b^2''\n(a - b)^2 = a^2 - 2ab + b^2''\na^2 - b^2 = (a + b)(a - b)')

@botik.message_handler(commands = ['square'])
def main(message):
    botik.send_message(message.chat.id, 'Формула площади квадрата:''\nS = a * a''\na - сторона квадрата')

@botik.message_handler(commands = ['triangle'])
def main(message):
    botik.send_message(message.chat.id, 'Формула площади треугольника:''\nS = 1/2 * a * h''\na - сторона треугольника''\nh - высота, опущенная к стороне a')

@botik.message_handler(commands = ['rectangle'])
def main(message):
    botik.send_message(message.chat.id, 'Формула площади прямоугольника:''\nS = a * b''\na - первая сторона''\nb - вторая сторона')

@botik.message_handler(commands = ['functions'])
def main(message):
    botik.send_message(message.chat.id, 'Основные функции в тригонометрии:''\ny = sin(x)''\ny = cos(x)''\ny = tg(x)''\ny = ctg(x)')

@botik.message_handler(commands = ['mathsite'])
def main(message):
    botik.send_message(message.chat.id, 'Для получения более подробной информации',
                                        'вы можете зайти на [официальный сайт математики](https://math.ru/)!')

botik.infinity_polling()