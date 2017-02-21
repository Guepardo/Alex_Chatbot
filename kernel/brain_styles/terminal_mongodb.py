class TerminalMongodb: 
	@staticmethod
	def get_style():
		storage_adapter = 'chatterbot.storage.MongoDatabaseAdapter'
		input_adapter = 'chatterbot.input.TerminalAdapter'
		output_adapter ='chatterbot.output.TerminalAdapter'
		database = 'chatbot'
		logic_adapters = ['chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation']
		filters = ['chatterbot.filters.RepetitiveResponseFilter']
		return storage_adapter, input_adapter, output_adapter, \
		logic_adapters, database, filters
