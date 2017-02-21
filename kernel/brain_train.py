# -*- coding: utf-8 -*- 
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

from kernel.brain_styles.terminal_mongodb import TerminalMongodb
from enums.bot import Name, Style

from helpers.database import Database
import sys

reload(sys)  
sys.setdefaultencoding('utf-8')

class BrainTrain(ChatBot): 
	def __init__(cls):
		# loading super class with some style
		storage_adapter, input_adapter, output_adapter, \
		logic_adapters, database, filters = TerminalMongodb.get_style()

		# loading super class with some style
		super(BrainTrain, cls).__init__(Name.BOT_NAME, \
			storage_adapter=storage_adapter, 
			input_adapter=input_adapter, 
			output_adapter=output_adapter, 
			logic_adapters=logic_adapters, 
			database=database,
			filters=filters) 

	
	# function to get reponses from an statement
	# def response(cls, statement):
	# 	return cls.get_response(statement)

	# this function train the brain with common community 
	# database. This helps fast start up our bots. 
	def train_by_portugues_corpus(cls): 
		cls.set_trainer(ChatterBotCorpusTrainer)
		cls.train("chatterbot.corpus.portuguese")

	# this function train the bot with specific rules
	def train_by_list(cls, training_list): 
		cls.set_trainer(ListTrainer)
		cls.train(training_list)

	def train_by_some_exemples(cls): 
		cls.train_by_list(['Quem te programou?', 'Allyson Maciel'])
		cls.train_by_list(['Quem é o seu mestre?', 'Allyson Maciel'])
		cls.train_by_list(['Em qual linguagem você é escrito?', 'Fui escrito em Python e você?'])

	def train_by_data_from_database(cls): 
		cls.set_trainer(ListTrainer)

		db = Database()
		cur = db.get_cursor()

		query = """SELECT msg, replay_to_id FROM messages WHERE replay_to_id IS NOT NULL order by id desc"""
		result = db.execute(query)
		count = 0
		for row in result:
			count += 1 
			answer = row[0]
			query = """SELECT msg FROM messages WHERE telegram_id = {replay_to_id}""".format(replay_to_id=row[1])
			temp = db.execute(query)
			
			if len(temp) > 0: 
				statement = temp[0][0]
				data_set = [unicode(statement.replace('\n','').strip(), errors='replace'), unicode(answer.replace('\n','').strip(), errors='replace')]
				print(data_set)
				cls.train(data_set)
			else: 
				continue

		db.close()
