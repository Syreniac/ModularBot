import urllib2

class Insult:
	def __init__(self,parent):
		self.parent=parent
		
		self.active=True
		
		self.messagable=True
		self.trackable=False
		
	def help(self,admin):
		if self.active:
			return "!insult - insults you\n"
		return ""
		
	def message(self,msg,admin,ignored):
		if self.active:
			
			if msg["body"].lower().startswith("!insult"):
				u=urllib2.urlopen("http://www.insultgenerator.org/")
				 
				s=u.read()

				s=s.split("<TD>")[1].split("</TD>")

				insult=s[0][:-1]
				
				if msg["type"]=="chat":
					self.parent.private_message(msg["from"],insult)
				else:
					self.parent.channel_message(msg["mucnick"]+": "+insult)