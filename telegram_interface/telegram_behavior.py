from kernel.brain import Brain
class TelegramBehavior: 
	@staticmethod
	def start(bot, updater):
		bot.sendMessage(chat_id=updater.message.chat_id, text="I'm a bot, please talk to me!")

	@staticmethod
	def echo(bot, updater): 
		brain = Brain()
		bot.sendMessage(chat_id=updater.message.chat_id, text=brain.get_response(updater.message.text))