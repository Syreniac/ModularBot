class Umi:
	def __init__(self,parent):
		self.parent=parent
		
		self.active=True
		
		self.messagable=True
		
		self.trackable=True
		
	def help(self,admin):
		if self.active:
			return "Also, shibebot now responds to many Umi statements!"
		return ""
		
	def message(self,msg,admin,ignored):
		if self.active:
			if msg["type"]=="groupchat":
				if msg["mucnick"].lower()=="umi":
					
					
					
					m=msg["body"].lower()
					s=[]
					
					if ":hug:" in m and msg["body"].lower().startswith("shibebot"):
						s.append(":hug:")
						
					if ":glomp:" in m and msg["body"].lower().startswith("shibebot"):
						s.append(":glomp:")
						
					if "pole" in m:
						s.append(":colbert:")
						
					if "thong" in m:
						s.append("the motherfucking pterodactyl!")
						
					sendstring="Umi:"
					
					if len(s)>0:
					
						for i in s:
							sendstring+=" "+i
							
						self.parent.channel_message(sendstring)
					