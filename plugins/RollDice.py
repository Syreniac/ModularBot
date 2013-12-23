import random

class RollDice:
	def __init__(self,parent):
		self.parent=parent
		
		self.active=True
		
		self.messagable=True
		self.trackable=False
		
	def help(self,admin):
		if self.active:
			return "![X]D[Y] - rolls X dice with Y faces\n"
		return ""
		
	def roll_dice(self,number,faces=0):
		if faces==0:
			return number
		else:
			a=0
			for i in xrange(number):
				a+=random.randint(1,faces)
			return a
		
	def message(self,msg,admin,ignored):
		if ignored:
			return
		if self.active:
			if msg["body"].startswith("!") and "d" in msg["body"].lower():
				m=msg["body"].replace(" ","")
				m=m.replace("!","")
				split_by_pluses=m.split("+")
				
				total=0
				a=0
				for i in split_by_pluses:
					split_by_Ds=i.lower().split("d")
					
					
					b=True
					
					number=0
					face=0
					
					try:
						number=int(split_by_Ds[0])
					except:
						b=False
						if a==0:
							return
						
					if b:
						try:
							face=int(split_by_Ds[1])
						except:
							face=0
							
					try:
						total+=self.roll_dice(number,face)
					except:
						if msg["type"]=="chat":
							self.parent.private_message(msg["from"],"Y U DO THIS?!?!")
						else:
							self.parent.channel_message(msg["mucnick"]+":"+" Y U DO THIS!??!")
						return
					a+=1
							
					
				if msg["type"]=="chat":
					self.parent.private_message(msg["from"],"You rolled "+str(total)+"!")
				else:
					self.parent.channel_message("You rolled "+str(total)+"!")