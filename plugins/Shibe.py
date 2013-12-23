import random
import math


class Shibe:
	def __init__(self,parent):
		self.parent=parent
		self.ignored_phrases=["",
							  "\t",
			                  "\n"]
		self.messagable=True
		self.trackable=False
		
		self.active=True
		
	def help(self,admin):
		if self.active:
			return "!shibe [thing 1] [thing 2] ... [thing N] - shibefy text\n"
		return ""
			
	def shibefy(self,text_raw):
		text=[]
		s=""
		for i in text_raw:
			i=i.replace(":","")
			if len(i)<15 and len(text)<15:
				if i.startswith('"') or i.startswith("'") and len(text_raw)>1:
					i=i.replace("'","")
					i=i.replace('"',"")
					s+=i+" "
				elif i.endswith("'") or i.endswith('"') and len(text_raw)>1:
					i=i.replace("'","")
					i=i.replace('"',"")
					s+=i
					text.append(s)
					s=""
				elif s!="" and len(text_raw)>1:
					s+=i+" "
				else:
					text.append(i)
					
		a=0
		while a<len(text):
			if text[a] in self.ignored_phrases or text.count(text[a])>1:
				del text[a]
			else:
				a+=1
		# Here is the function that actually shibefies
		random.shuffle(text)
				
		l=["very",
		   "so",
		   "much",
		   "such"]
		   
		l2=[None]
		
		maxLength=min(8,len(text))
		wowCount=0
		dWowCount=random.randint(int(math.log(len(text))),int(len(text)))
		wows=[]
		for i in range(dWowCount):
			r=random.randint(0,len(text)+dWowCount-2)
			while r in wows and r-1 in wows and r+1 in wows:
				r=random.randint(0,len(text)+dWowCount-2) 
			wows.append(r)
		   
		sA="\r\n"
		runCount=0
		while len(text)>0:
			if len(l2)>maxLength:
				del l2[random.randint(1,len(l2)-1)]
			r=None
			while r in l2:
				r=random.randint(0,10)
			l2.append(r)
			s="    "
			for j in range(r):
				s+="\t"
			if not runCount in wows:
				sA+="\r\n"+s+random.choice(l)+" "+text.pop(0)
			else:
				sA+="\r\n"+s+"wow"
			runCount+=1
		return sA
		 
	def message(self,msg,admin,ignored):
		if ignored:
			return
		if self.active:
			if msg["body"].startswith("!shibe ") and not msg["mucnick"] in self.parent.excluded:
				
				# Separate the words to be shibefied
				
				spli=msg["body"].split(" ")
				
				del spli[0]
				if spli[0].lower()=="everyone" and msg["type"]=="chat":
					spli=self.parent.jidList.keys()
					
				a=0
				sA=self.shibefy(spli)
				
				if msg["type"]=="groupchat" and not str(msg["from"]).lower().split("@")[0]=="johnathanseverasse":
					self.parent.channel_message(sA)
				else:
					self.parent.private_message(msg["from"],sA)