import os

from telegram.ext import Updater, CommandHandler
import logging
from telegram.ext import MessageHandler, Filters

from tgbot.worker import goes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update):
    update.message.reply_text('Hello World!')


def hello(bot, update):
    # update.message.reply_text(
    #     'Hello {}'.format(update.message.from_user.first_name))
    t = goes()
    update.message.reply_text(t)

    # update.message


def echo(bot, update):
    # global d
    msg = update.message.text
    ans = "wwww"

    bot.send_message(chat_id=update.message.chat_id, text="I find: " + ans)


#################################################
from yaml import load, dump

env_file = '.env.yaml'

token_str = 'TELEGRAM_BOT_TOKEN'

if os.path.exists(env_file):
    with open(env_file, 'r') as f:
        data = load(f)
        assert token_str in data.keys()
        os.environ[token_str] = data[token_str]

assert token_str in os.environ.keys()

TOKEN = os.environ.get(token_str)
PORT = int(os.environ.get('PORT', '5000'))

#################################################


updater = Updater(TOKEN)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('hello', hello))

dispatcher.add_handler(MessageHandler(Filters.text, echo))

print("finish set up bot.")

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path="" + TOKEN)
updater.bot.set_webhook("https://parser-713.herokuapp.com/" + TOKEN)

# time to try webhooks
# updater.start_polling()

print("before idle")
updater.idle()
print("after idle")
