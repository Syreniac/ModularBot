class NuclearOption:
	def __init__(self,parent):
		self.parent=parent
		
		self.active=False
		
		self.trackable=True
		self.messagable=False
		
		self.nuking=False
		
		self.nuke_checking=0
		
	def help(self,admin):
		if self.active:
			return "The nuclear option is currently: ENABLED"
		return "The nuclear option is currently: DISABLED"
		
	def track(self):
		if self.active:
			for i in self.parent.jidList:
				if i.lower()=="syreniac":
					self.nuking=False
					return
			
			if self.nuke_checking>10:		
				if self.nuking:
					self.parent.channel_message("\n:bort:\n:bort:\n:bort:\n:bort:")
				else:
					self.parent.channel_message("Sensors indicate a sudden lack of Syreniac. Initiating NUCLEAR OPTION")
					self.nuking=True
			else:
				self.nuke_checking+=1