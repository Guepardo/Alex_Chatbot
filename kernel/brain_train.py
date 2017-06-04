# -*- coding: utf-8 -*- 
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

from kernel.brain_styles.terminal_mongodb import TerminalMongodb
from enums.bot import Name, Style

from helpers.database import Database
import sys, os, json

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
		files = [ file for file in os.listdir('./training_set')]

		for file in files: 
			arq = open('./training_set/%s' % file)
			train_set = json.loads(arq.readline())
			for train in train_set:
				cls.train([train['question'], train['answer']])
				print(train)
				break
