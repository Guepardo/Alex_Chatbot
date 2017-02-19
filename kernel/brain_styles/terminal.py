class Terminal:
	@staticmethod
	def get_style():
		storage_adapter = "chatterbot.storage.JsonFileStorageAdapter"
		input_adapter = "chatterbot.input.TerminalAdapter"
		output_adapter ="chatterbot.output.TerminalAdapter"
		database = "./database.json"
		logic_adapters = ["chatterbot.logic.BestMatch"]
		filters = ["chatterbot.filters.RepetitiveResponseFilter"]
		return storage_adapter, input_adapter, output_adapter, \
		logic_adapters, database, filters




