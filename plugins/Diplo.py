import random

class Diplo:
	def __init__(self,parent):
		self.parent=parent
		
		self.messagable=True
		self.trackable=False
		
		self.active=True
		
	def help(self,admin):
		if self.active:
			return "!diplo - get sound diplomatic advice\n"
		return ""
			
	def diplomancy(self):
		verb = [
			"Kick",
			"Gas",
			"Reset",
			"Invade",
			"Blue",
			"Camp"
		]
		noun = [
			"PL",
			"Goons",
			"NC.",
			"S2N",
			"TRIBE",
			"TEST",
			"FA",
			"EXE",
			"TROLL",
			"EMP",
			"INIT",
			"BL",
			"401k",
			"PIZZA",
			"CVA",
			"-DD-",
			"-A-"
		]
	
		return random.choice(verb) + " " + random.choice(noun)
			
	def message(self,msg,admin,ignored):
		if ignored:
			return
		if self.active:
			if msg["body"].lower().startswith("!diplo"):
				
				if msg["type"]=="groupchat":
					self.parent.channel_message(self.diplomancy())
				elif msg["type"]=="chat":
					self.parent.private_message(msg["from"],self.diplomancy())
		
	