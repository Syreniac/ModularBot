class Dernarius:
	def __init__(self,parent):
		self.parent=parent
		
		self.active=True
		self.messagable=True
		self.trackable=False
		
	def help(self,admin):
		return ""
		
	def message(self,msg,admin,ignored):
		if ignored:
			return
		if self.active:
			if "dicks" in msg["body"].lower() and msg["type"]=="groupchat":
				self.parent.channel_message("^ Dernarius Starariur:")