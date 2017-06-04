from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram_interface.telegram_behavior import TelegramBehavior

class TelegramConnector: 
	def __init__(cls): 
		cls.updater = Updater(token='211611433:AAF8h0BHccdogqnzRzhicQBb6Q0qeiqp6-Q')

	def start_bot(cls): 
		dispatcher = cls.updater.dispatcher
		
		start_handler = CommandHandler('start', TelegramBehavior.start)
		echo_hander = MessageHandler(Filters.text, TelegramBehavior.echo)

		dispatcher.add_handler(start_handler)
		dispatcher.add_handler(echo_hander)

		cls.updater.start_polling()