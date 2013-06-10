#!/usr/bin/env python

# MAKE IT UNICODE OK
import sys
reload( sys )
sys.setdefaultencoding( 'utf-8' )

import os, sys
import Bot
import logging

logging_level = logging.DEBUG
logging_format = '[%(asctime)s] %(levelname)s: %(message)s'
	
if __name__ == '__main__':
	fork = True
	if len( sys.argv ) > 1:
		if sys.argv[1] == '-nofork':
			fork = False
	if fork:
		logging.basicConfig( filename = 'ircbot.log', level = logging_level, format = logging_format )
	else:
		logging.basicConfig( level = logging_level, format = logging_format )
	logging.info( "Welcome to botje" )
	if fork:
		try:
			pid = os.fork()
			if pid > 0:
				logging.info( 'Forked into PID {0}'.format( pid ) )
				sys.exit(0)
			sys.stdout = open( '/tmp/ircbot.log', 'w' )
		except OSError as error:
			logging.error( 'Unable to fork. Error: {0} ({1})'.format( error.errno, error.strerror ) )
			sys.exit(1)
	botje = Bot.Bot()
	while True:
		try:
			botje.start()
		except Bot.BotReloadException:
			logging.info( 'Force reloading Bot class' )
			botje = None
			reload(Bot)
			botje = Bot.Bot()
		logging.info( 'Botje died, restarting in 5...' )
		import time
		time.sleep( 5 )
