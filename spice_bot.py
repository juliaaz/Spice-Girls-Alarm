import telebot
bot = telebot.TeleBot('token')


from telebot import types
import random

import csv

import csv
import random

def generating_data():
    """Reading and generating necessary data about random word."""
    with open('word-meaning-examples.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        num = random.randint(0, 13160)
        data = {}
        for row in csv_reader:
            data[row["Word"]] = [row["Meaning"]]
            examples = [row[example] for example in
                        ["Examples/0", "Examples/1",
                         "Examples/2", "Examples/3",
                         "Examples/4", "Examples/5",
                         "Examples/6", "Examples/7",
                         "Examples/8", "Examples/9"] if
                        row[example] != ""]
            data[row["Word"]].append(examples)
    key = random.choice(list(data.keys()))
    data = data[key]
    return [key] + data


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    """
    Bot starts with the Hello message.
    """
    if message.text == "Hello":

        bot.send_message(message.from_user.id, "Hey buddy, choose what would you like to do :)")
        keyboard = types.InlineKeyboardMarkup()
        key_test = types.InlineKeyboardButton(text='Start English Test', callback_data='test')

        keyboard.add(key_test)
        key_exit = types.InlineKeyboardButton(text='Stop Bot', callback_data='stop')
        keyboard.add(key_exit)

        bot.send_message(message.from_user.id, text='Choose an option', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Write Hello")
    else:
        bot.send_message(message.from_user.id, "I don't understand you. Tap on /help.")


def main_function(call):
    """
    Main fucntion that operates everything.
    """
    num = random.randint(0,1)
    if num == 0:
        data_1 = generating_data()
        word_correct = data_1[0]
        words = [generating_data()[0], generating_data()[0], word_correct]
        words = random.sample(words, len(words))
        global correct_answer1
        correct_answer1 = word_correct

        sentence = random.choice(data_1[2]).lower().replace(word_correct.lower(),
                                                            '_________').capitalize()
        keyboard = types.InlineKeyboardMarkup()

        keyboard.add(types.InlineKeyboardButton(words[0], callback_data=words[0]),
                     types.InlineKeyboardButton(words[1], callback_data=words[1]),
                     types.InlineKeyboardButton(words[2], callback_data=words[2]),
                     types.InlineKeyboardButton("Stop", callback_data='stop'))
        bot.send_message(call.from_user.id, text=sentence, reply_markup=keyboard)
        @bot.callback_query_handler(func=lambda call: call.data in [words[0], words[1], words[2], correct_answer1])
        def otvet(call):
            global correct_answer1
            if call.data == correct_answer1:
                bot.send_message(call.from_user.id, "Good job, let's move on!")
                main_function(call)
            elif call.data == 'stop':
                bot.send_message(call.from_user.id, "I am sad")
                return
            else:
                bot.send_message(call.from_user.id, "You are wrong. The answer is: " + correct_answer1)
                main_function(call)


    else:
        data_1 = generating_data()
        word_correct = data_1[0]
        words = [generating_data()[0], generating_data()[0], word_correct]
        words = random.sample(words, len(words))
        keyboard = types.InlineKeyboardMarkup()
        global correct_answer
        correct_answer = word_correct

        keyboard.add(types.InlineKeyboardButton(words[0], callback_data=words[0]),
                types.InlineKeyboardButton(words[1], callback_data=words[1]),
                types.InlineKeyboardButton(words[2], callback_data=words[2]),
                types.InlineKeyboardButton("Stop", callback_data='stop'))
        bot.send_message(call.from_user.id, text=data_1[1], reply_markup=keyboard)
        @bot.callback_query_handler(func=lambda call: call.data in [words[0], words[1], words[2]])
        def otvet(call):
            """
            Generates bot's response.
            """
            global correct_answer
            if call.data == correct_answer:
                bot.send_message(call.from_user.id, "Good job, let's move on!")
                main_function(call)
            elif call.data == 'stop':
                bot.send_message(call.from_user.id, "I am sad")
                return
            else:
                bot.send_message(call.from_user.id, "You are wrong. The answer is: " + correct_answer)
                main_function(call)

@bot.callback_query_handler(func=lambda call: call.data in ['test', 'stop'])
def callback_worker(call):
    """
    Starts the bot.
    """
    if call.data == "test": 
        main_function(call)

    if call.data == "stop": 
        msg = 'Thank you for using bot!'
        bot.send_message(call.message.chat.id, msg)

bot.polling(none_stop=True, interval=0)
