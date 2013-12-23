import random

class Tune:
	def __init__(self,parent):
		self.parent=parent
		
		self.active=True
		
		self.trackable=False
		self.messagable=True
		
	def help(self,admin):
		if self.active:
			return "!tune - whistles a tune for you\n"
		return ""
		
	def message(self,msg,admin,ignored):
		if self.active:
			if msg["body"].lower().startswith("!tune") or msg["body"].lower().startswith("!toot"):
				list=["doo",
				      "bee",
					  "do-",
					  "dum",
					  "diddle",
					  "doodle",
					  "diddly"]
					 
				m=""
				for i in range(random.randint(5,10)):
					m+=random.choice(list)
					if m[-1]!="-":
						m+=" "
						
				self.parent.channel_message(m)