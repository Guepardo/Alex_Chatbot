import logging
from chatterbot import ChatBot

from kernel.brain_styles.terminal_mongodb import TerminalMongodb
from enums.bot import Name, Style

class Brain(ChatBot): 
	def __init__(cls):
		
		# starting logging 
		# logging.basicCofing(level=logging.INFO)

		storage_adapter, input_adapter, output_adapter, \
		logic_adapters, database, filters = TerminalMongodb.get_style()

		# loading super class with some style
		super(Brain, cls).__init__(Name.BOT_NAME, \
			storage_adapter=storage_adapter, 
			input_adapter=input_adapter, 
			output_adapter=output_adapter, 
			logic_adapters=logic_adapters, 
			database=database,
			filters=filters, read_only=True) 
	
	# function to get reponses from an statement
	# def response(cls, statement):
	# 	return cls.get_response(statement)
