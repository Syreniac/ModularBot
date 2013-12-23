class UnrealBlight:
	def __init__(self,parent):
		self.parent=parent
		
		self.active=True
		
		self.messagable=True
		self.trackable=False
		
	def help(self,admin):
		if self.active:
			return "!unrealblight [ISK] - Returns double an amount of ISK\n"
		return ""
		
	def message(self,msg,admin,ignored):
		if ignored:
			return
		if self.active:
			if msg["body"].lower().startswith("!unrealblight"):
				try:
					s=msg["body"].split(" ")[1]
					i=int(s)
					
					if msg["type"]=="groupchat":
						self.parent.channel_message("Double that would be "+str(i*2)+" ISK")
					else:
						self.parent.private_message(msg["from"],"Double that would be "+str(i*2)+" ISK")
					
				except:
					self.parent.channel_message("Uh, no.")
					
					