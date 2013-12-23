class RachelEnWelle:
	def __init__(self,parent):
		self.parent=parent
		
		self.messagable=True
		self.trackable=True
		
		self.active=True
		
	def help(self,admin):
		return ""
			
	def message(self,msg,admin,ignored):
		if msg["mucnick"].lower()=="rachel en welle":
			self.parent.channel_message("^ is Polish!")