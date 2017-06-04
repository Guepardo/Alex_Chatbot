class TerminalMongodb: 
	@staticmethod
	def get_style():
		storage_adapter = 'chatterbot.storage.MongoDatabaseAdapter'
		input_adapter = 'chatterbot.input.TerminalAdapter'
		output_adapter ='chatterbot.output.TerminalAdapter'
		database = 'chatbot'
		logic_adapters = [
			{
				'import_path': 'chatterbot.logic.BestMatch'
			},
			{
				'import_path': 'chatterbot.logic.LowConfidenceAdapter',
				'threshold': 0.1,
				'default_response': 'I am sorry, but I do not understand.'
			}
		]
		filters = ['chatterbot.filters.RepetitiveResponseFilter']
		return storage_adapter, input_adapter, output_adapter, \
		logic_adapters, database, filters
