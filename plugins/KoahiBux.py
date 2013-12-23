import random
import os

def to2sfigs(num):
	s=str(num)
	s1=s.split(".")
	if len(s1)==1:
		s1.append("")
	while len(s1[1])<2:
		s1[1]+="0"
	return s1[0]+"."+s1[1]

class KoahiBux:
	def __init__(self,parent):
		self.parent=parent
		
		self.messagable=True
		self.trackable=False
		
		self.active=False
		
		self.base_chance=0.02
		self.reduction_base=2.0
		
		self.reduction=["",0]
		
		
		#self.internal_data={}
		self.read_data()
		
	def help(self,admin):
		if self.active:
			s=u"!kb balance - check your koahibux balance"+"\n"
			s+=u"!kb give [nickname] [amount] - give [amount] of koahibux to [nickname]"+"\n"
			return s
		return ""
		
	def message(self,msg,admin,ignored):
		if self.active and str(msg["mucnick"])!=u"":
			print self.parent.jidList[str(msg["mucnick"])]
			
			if self.parent.jidList[str(msg["mucnick"])]!=self.parent.jid and msg["type"]=="groupchat":
				self.earn_koahibux(self.parent.jidList[str(str(msg["mucnick"]))],str(msg["mucnick"]))
				
			self.commands(msg,admin,ignored)
		
		
	def commands(self,msg,admin,ignored):
		m=""
		if msg["body"].lower().startswith("!kb "):
			m=msg["body"][4:]
		elif msg["body"].lower().startswith(unicode("!")+u"\u20AD"+" "):
			m=msg["body"][3:]
			
		if m!="":
			print m
			if m.lower().startswith("give "):
				#giving
				print "YES"
				m=m[5:]
				
				max_length=len(m)
				point=max_length
				char=""
				
				while char!=" ":
					point-=1
					char=m[point]
					
				number=float(m[point+1:])
				print number
				old_point=point
					
				name=m[:point]
				print name
					
				self.give(str(msg["mucnick"]),self.parent.jidList[str(msg["mucnick"])],name,number)
			if m.lower().startswith("balance"):
				self.balance(msg)
				
			if m.lower().startswith("reload"):
				self.reload(msg)
				
	def reload(self,msg):
		if self.parent.jidList[str(msg["mucnick"])] in self.parent.admins:
			self.read_data()
			self.parent.channel_message("Koahibux totals reloaded from file!")
				
	def balance(self,msg):
		if msg["type"]=="chat":
			jid=msg["from"].bare
			if jid in self.internal_data:
				self.parent.private_message(msg["from"],unicode("You currently have "+u"\u20AD"+to2sfigs()))
			else:
				self.parent.private_message(msg["from"],"You have no koahibux.")
		if msg["type"]=="groupchat":
			jid=self.parent.jidList[str(msg["mucnick"])]
			if jid in self.internal_data:
				self.parent.channel_message(unicode(str(msg["mucnick"])+": You currently have "+u"\u20AD"+to2sfigs(self.internal_data[jid])))
			else:
				self.parent.channel_message(unicode(str(msg["mucnick"])+": You have no koahibux"))
				
	def give(self,mucnick,jid,name,number):
		jid=str(jid)
		number=round(number,10)
		if number<0:
			self.parent.channel_message(mucnick+": Positive amounts only please.")
			return
		elif number<0.01:
			self.parent.channel_message(mucnick+": That amount is too small.")
			return
		if number<self.internal_data[jid] and jid in self.internal_data:
			if name in self.parent.jidList.keys():
				if self.parent.jidList[name] in self.internal_data:
					self.internal_data[self.parent.jidList[name]]+=number
				else:
					self.internal_data[self.parent.jidList[name]]=number
				self.internal_data[jid]-=number
				self.parent.channel_message(unicode(mucnick+" gave "+name)+" "+u"\u20AD"+to2sfigs(number))
				self.write_data()
			else:
				self.parent.channel_message(mucnick+": That person isn't here right now.")
				return
		else:
			self.parent.channel_message(mucnick+": You don't have enough koahibux for that!")
			return
			
	def earn_koahibux(self,jid,mucnick):
		
		# This is where the randomisation goes
		chance=self.base_chance
		r=random.random()
		if str(jid)==self.reduction[0]:
			chance/=(self.reduction_base**self.reduction[1])
			self.reduction[1]+=1
		else:
			self.reduction=[str(jid),1]
		if r>chance:
			return
			
		amount=float(5+random.randint(0,5))/100
		
		if not str(jid) in self.internal_data:
			self.internal_data[str(jid)]=amount
		else:
			self.internal_data[str(jid)]+=amount
			
		self.parent.channel_message(u"Congratulations, "+mucnick+" has earnt "+u"\u20AD"+to2sfigs(amount)+"!")
		self.write_data()
		
	def read_data(self):
		p=os.path.join("saveddata",self.parent.bot_id,"koahibux.txt")
		print p
		self.internal_data={}
		try:
			f=open(p,"r")
			
			for line in f:
				print line
				split_line=line.split(":")
				self.internal_data[split_line[0]]=float(split_line[1])
			
			f.close()
			
		except:
			pass
		
	def write_data(self):
		p=os.path.join("saveddata",self.parent.bot_id,"koahibux.txt")
		print p
		f=open(p,"w")
		
		for jid in self.internal_data.keys():
			f.write(str(jid)+":"+str(self.internal_data[jid])+"\n")
			
		f.close()
		
		