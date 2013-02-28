class _module:
	def __init__( self, config, bot ):
		self.bot = bot
		for k, v in config:
			setattr( self, k, v )
	def can_handle( self, cmd, admin ):
		return False
	def handle( self, bot, cmd, args, source, target, admin ):
		pass
