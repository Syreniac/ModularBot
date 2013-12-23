class Koahi:
	def __init__(self,parent):
		self.parent=parent
		
		self.messagable=True
		self.trackable=False
		
		self.active=True
		
	def help(self,admin):
		if self.active:
			return "!koahi - returns the laws of koahi\n"
		return ""
			
	def message(self,msg,admin,ignored):
		if ignored:
			return
		if self.active:
			if msg["body"].lower().startswith("!koahi"):
				
				if msg["type"]=="groupchat":
					self.parent.channel_message("\nDo:\n\tBe Cool\n\tHave Fun\nDon't\n\tBe Uncool\n\tGet Butthurt")
					self.parent.channel_message("Also, he sounds less gay than you'd think")
				elif msg["type"]=="chat":
					self.parent.private_message(msg["from"],"\nDo:\n\tBe Cool\n\tHave Fun\nDon't\n\tBe Uncool\n\tGet Butthurt")
					self.parent.private_message(msg["from"],"Also, he sounds less gay than you'd think")
		
			if "usa #1" in msg["body"].lower() and msg["type"]=="groupchat":
				self.parent.channel_message(msg["mucnick"]+": :frogout:  USA scum")
				
	