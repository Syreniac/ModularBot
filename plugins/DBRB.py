class DBRB:
	def __init__(self,parent):
		self.parent=parent
		
		self.messagable=True
		self.trackable=False
		
		self.active=True
		
	def help(self,admin):
		if self.active:
			return "!DBRB - You know you want to\n"
		return ""
			
	def message(self,msg,admin,ignored):
		if ignored:
			return
		if self.active:
			if msg["body"].lower().startswith("!dbrb"):
				
				if msg["type"]=="groupchat":
					self.parent.channel_message("BARK BARK BARK")
				elif msg["type"]=="chat":
					self.parent.private_message(msg["from"],"BARK BARK BARK")