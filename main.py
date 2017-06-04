# -*- coding: utf-8 -*-
import sys
from kernel.brain import Brain
from kernel.brain_train import BrainTrain
from telegram_interface.telegram_connector import TelegramConnector
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main():
	TelegramConnector().start_bot() 
	# # gettting some command line args
	# print(sys.argv)

	# mode = ''
	# try: 
	# 	mode = str(sys.argv[1])
	# except: 
	# 	pass 


	# alex = Brain() 
	# if mode == 'learn': 
	# 	print("Initing on learn mode")
	# 	alex = BrainTrain()
	# 	alex.train_by_portugues_corpus()
	# 	alex.train_by_some_exemples()
	# 	alex.train_by_data_from_database()
	# else: 
	# 	alex = Brain()
	# 	while True: 
	# 		alex.get_response('  ')
	# 		print 'User - '
main()