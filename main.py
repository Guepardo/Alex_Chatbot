# -*- coding: utf-8 -*-
import sys
from kernel.brain import Brain
from kernel.brain_train import BrainTrain
def main(): 
	# gettting some command line args
	print(sys.argv)

	mode = ''
	try: 
		mode = str(sys.argv[1])
	except: 
		pass 


	alex = Brain() 
	if mode == 'learn': 
		print("Initing on learn mode")
		alex = BrainTrain()
		alex.train_by_portugues_corpus()
		alex.train_by_some_exemples()
		alex.train_by_data_from_database()
	else: 
		alex = Brain()
		while True: 
			alex.get_response('  ')
			print 'User - '
main()