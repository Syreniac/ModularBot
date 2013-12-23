import random
import string
	
def getLetter(a,b=None):
	if b!=None:
		l=[]
		for i in string.lowercase[a:b]:
			l.append(i)
		return l
	else:
		return string.lowercase[a]
		
def endreplace(s,fs,rs):
	if s.endswith(fs):
		s=s[:-len(fs)]
		s+=rs
	return s
	
class Polling:
	def __init__(self,parent):
		self.parent=parent
		
		self.messagable=True
		self.trackable=False
		self.polling=True
		
		self.active=True
		
		self.polling=0
		
		self.tiebreaker="eurobot"
		
		self.polltime=60.0
		
	def help(self,admin):
		if self.active:
			return "!poll [option 1] or [option 2] ... or [option N] - start a poll with the options\n!pollover - stops a poll if you started one\n"
		return ""
			
	def message(self,msg,admin,ignored):
		if ignored and not (self.polling==-1 and msg["mucnick"]==self.tiebreaker):
			return
		if self.active:
			if msg["type"]=="chat" and admin:
				if msg["body"].lower().startswith("!polltimer "):
					m=msg["body"].split(" ")
					try:
						i=float(m[1])
						self.polltime=i
					except ValueError:
						self.parent.private_message(msg["from"],"Care to repeat that?")
					
			elif msg["type"]=="groupchat":
				print msg["body"][:10]+"..."
				print self.polling
				if self.polling==1:
					m=msg["body"].lower()
					if msg["mucnick"]==self.pollStart or admin:
						if m.startswith("!pollover"):
							self.pollBreak()
					if m in self.pollkeys:
						if not msg["mucnick"] in self.polled:
							self.polled.append(msg["mucnick"])
							vote=ord(m[0]) - 97
							self.pollresults[vote]+=1
							
						else:
							sendString="No cheating please, "+str(msg["mucnick"])
							self.parent.channel_message(sendString)
				elif self.polling==-1:
					print self.tiebreaker
					print msg["mucnick"]
					print msg["mucnick"].lower()==self.tiebreaker
					print msg["body"][:10]+"..."
					if msg["mucnick"].lower()==self.tiebreaker:
						m=msg["body"].lower()
						if m.startswith("shibebot: "):
							m=m.replace("shibebot: ","")
						print m
						if m[0] in self.pollkeys:
							vote=ord(m[0]) - 97
							self.pollresults[vote]+=1
							self.pollOver(True)
						else:
							self.polling=0
							self.parent.channel_message("Once again, "+self.tiebreaker+" impresses me with its inability to make decisions")
				elif self.polling==0:
					if msg["body"].startswith("!poll"):
						
						
						m=msg["body"].lstrip("!poll")
						m=m.rstrip("?")
						if m[0]==" ":
							m=m[1:]
						
						m=m.split(" or ")
						m=m[:20]
						
						if len(m)>1:
						
						
							sendString="Poll noted."
							
							self.pollresults=[]
							self.pollOptions=[]
							self.pollkeys=[]
							self.polled=[]
							a=0
							for i in m:
								
								sendString+="\n\t"+getLetter(a).upper()+": "+i
								self.pollOptions.append(i)
								self.pollresults.append(0)
								self.pollkeys.append(getLetter(a))
								a+=1
								
							sendString+="\n\t"+getLetter(a).upper()+": "+"checkbox"
							self.pollOptions.append("checkbox")
							self.pollresults.append(0)
							self.pollkeys.append(getLetter(a))
						
							
							sendString+="\nPlease enter your choices using the relevant letters."
								
							self.polling=1
							
							self.pollStart=msg["mucnick"]
							
							self.parent.scheduler.add("Poll",self.polltime,self.pollFunc,repeat=False)
					
							self.parent.channel_message(sendString)
						else:
							self.parent.channel_message("That poll is terrible, and I don't like it")
					

	def pollBreak(self):
		self.parent.scheduler.remove("Poll")
		self.pollOver()
		
	
		
	def tiebreak(self):
		
		sendString=""
		
		a=0
		for i in self.pollkeys:
			
			sendString+="\n\t"+self.pollkeys[a]+": "+self.pollOptions[a]
			a+=1
			
		
		sendString=self.tiebreaker+": TIEBREAK: "+sendString
		self.parent.channel_message(sendString)
		
	
	def pollFunc(self):
		self.pollOver()
		
	def pollOver(self,b=None):
		if self.polling!=0 or b!=None:
			if b==None:
				self.parent.channel_message("The poll is over!")
			self.polling=0
			
			c=0
			m=max(self.pollresults)
			for i in self.pollresults:
				if i==m:
					c+=1
			
			if c>1 and b==None:
				sendString="It's a tie!"
				self.polling=-1
				self.parent.scheduler.add("Tiebreak",1.0,self.tiebreak,repeat=False)
			else:
				ind=self.pollresults.index(m)
				
				if b!=None:
					sendString=self.pollOptions[ind]+" is the winner through "+self.tiebreaker+"'s decision!"
				else:
					sendString=self.pollOptions[ind]+" is the winner with "+str(self.pollresults[ind])+" votes!"
			

				
			self.parent.channel_message(sendString)