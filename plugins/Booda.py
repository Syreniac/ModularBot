import random

class Booda:
	def __init__(self,parent):
		self.parent=parent
		
		self.active=True
		self.messagable=True
		self.trackable=False
		
	def help(self,admin):
		if self.active:
			return "!booda - Boodabooda left you a message!\n"
		return ""
		
	def message(self,msg,admin,ignored):
		if ignored:
			return
		if self.active:
			if msg["body"].lower().startswith("!booda"):
				if msg["mucnick"].lower()=="boodabooda":
					if msg["type"]=="chat":
						self.parent.private_message(msg["from"],"All hail Boodabooda!")
					else:
						self.parent.channel_message("All hail Boodabooda!")
					
				else:
					if msg["type"]=="chat":
						self.parent.private_message(msg["from"],"\nDear "+msg["mucnick"]+"\nYou're a faggot\nLove,\nBoodabooda")
					else:
						self.parent.channel_message("\nDear "+msg["mucnick"]+"\nYou're a faggot\nLove,\nBoodabooda")