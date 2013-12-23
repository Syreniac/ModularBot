import random
import string
	
class Choose:
	def __init__(self,parent):
		self.parent=parent
		
		self.messagable=True
		self.trackable=False
		self.polling=True
		
		self.active=True
		
		self.polling=0
		
		self.tiebreaker=self.parent.tiebreaker
		
		self.polltime=60.0
		
		self.always_choose={0:"umi",
		                    1:"rhubarb",
							2:"boobs"}
		
		self.never_choose=["justin beiber",
						   "poledance"]
		
	def help(self,admin):
		if self.active:
			return "!choose [option 1] or [option 2] ... or [option N] - chooses from a list\n"
		return ""
			
	def message(self,msg,admin,ignored):
		if self.active:
			print 1
			if msg["body"].lower().startswith("!choose"):
				random.seed(msg["body"])
				m=msg["body"][7:].split(" or")
				m2=[]
				lower_list=[]
				for i in m:
					if not i[1:] in m2:
						m2.append(i[1:])
						lower_list.append(i[1:].lower())
						
				print 2
						
						
				if len(m2)>1:
					print 2.1
					l=self.always_choose.keys()
					choose_list=[]
					a=0
					print 2.2
					while a<max(l):
						b=0
						print "max(l):"+str(max(l))
						while b<len(m2):
							i=m2[b]
							c=True
							for j in self.never_choose:
								if j in i.lower():
									del m2[b]
									c=False
									break
							if c and self.always_choose[a] in i.lower():
								choose_list.append(i)
							if c:
								b+=1
						print "a:"+str(a)
						a+=1
						print "a:"+str(a)
					a-=1
					
					print 3
						
					if len(choose_list)>0:
						choose=random.choice(choose_list)
					else:
						choose=random.choice(m2)
						
					extra=""
					if len(choose_list)>0:
						if a+1 in self.always_choose.keys():
							for choice in m2:
								if self.always_choose[a+1] in choice.lower():
									extra=". Tough choice, though."
									
						print 4			
						if extra=="":
							if len(choose_list)==1:
								extra=". No contest."
					print 5
					
					self.parent.channel_message("I choose "+choose+extra)
				else:
					self.parent.channel_message("That's not a choice!")