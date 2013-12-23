import time
import random

class Te:
	def __init__(self,parent):
		self.parent=parent
		self.time=time.time()
		
		self.messagable=True
		self.trackable=False
		
		self.active=True
		
		self.high_score=0
		
	def help(self,admin):
		if self.active:
			return "!te - find how long it has been since Te has graced us with his presence\n"
		return ""
		
	def message(self,msg,admin,ignored):
		if ignored:
			return
		if self.active:
			if msg["mucnick"]=="TeTumatauenga":
				time_waited=time.time()-self.time
			
				if time_waited>self.high_score:
					self.high_score=time_waited
					self.parent.channel_message("TeTumatauenga managed to wait "+str(int(self.high_score))+" seconds before talking. New high score!")
			
				self.time=time.time()
			
			if msg["body"].startswith("!te"):
				time_waited=time.time()-self.time
				l=["This is too long!",
				   "Not long enough if you ask me...",
				   "I miss him already :(",
				   "This channel needs more TeTumatauenga.",
				   "This channel feels so much better without TeTumatauenga",
				   "Come back TeTumatauenga, we miss you!",
				   "Good riddance!"]
				time_waited=str(time_waited).split(".")
				time_waited=time_waited[0]
				self.parent.channel_message("It has been "+time_waited+" seconds since TeTumatauenga has spoken. "+random.choice(l))