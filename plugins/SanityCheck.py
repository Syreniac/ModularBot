import random

class SanityCheck:
	def __init__(self,parent):
		self.parent=parent
		
		self.messagable=True
		self.trackable=False
		
		self.active=True
		
	def help(self,admin):
		return ""
			
	def message(self,msg,admin,ignored):
		if msg["type"]=="groupchat":
			if msg["body"].lower().startswith("!sanitycheck"):
				self.parent.channel_message("Beginning sanity analysis of "+msg["mucnick"]+" using collected data")
				self.parent.channel_message("Analyzing...")
				self.parent.scheduler.add("SanityAnalysis:"+msg["mucnick"],1.0,self.results,args=(msg["mucnick"],),repeat=False)
				
	def results(self,mucnick):
		random.seed(mucnick)
		r=round(random.random()*100,3)
		if mucnick.lower()=="syreniac":
			r=100.0
		s=""
		if r<5.0:
			s=". Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn."
		elif r<10.0:
			s=". BE AFRAID. BE VERY AFRAID."
		elif r<15.0:
			s=". A straitjacket would be advisable."
		elif r<20.0:
			s=", and belives themselves to be the reincarnation of "+random.choice(("Elvis","Napoleon","Julius Caesar","Hitler","a psychic goldfish","a potted shrub"))+"."
		elif r<25.0:
			s=", and they should be kept away from sharp or reflective objects."
		elif r<30.0:
			s=". The prognosis is bleak."
		elif r<35.0:
			s=". Be careful of sudden mood swings."
		elif r<40.0:
			s=", and displays strong kleptomanic tendencies."
		elif r<45.0:
			s=", and has an intense phobia of "+random.choice(("cats","fish","buttons","waffles","sysadmins","mirrors","horses","the Polish","emoticons","chatbots","Sklullus","the colour mauve","music in E#","surprise birthday parties","vowels","Azerbijan"))+"."
		elif r<50.0:
			s=". Careful observation recommended."
		elif r<55.0:
			s=", although they seem to be regressing into a second childhood."
		elif r<60.0:
			s=", has an overly trusting nature indicative of [REDACTED]."
		elif r<65.0:
			s=". Their IQ falls below natural human levels however."
		elif r<70.0:
			s=", but should not be trusted with small children or animals."
		elif r<75.0:
			s=". Has a psychosomatically induced case of "+random.choice(("herpes","bubonic plague","logorrhea","ebola","the common cold","avian influenza","a broken arm","partial paralysis","sleeping sickness","malaria","[REDACTED]"))+"."
		elif r<80.0:
			s=". Has a fixation on "+random.choice(("counting paper clips","alphabetically sorting crisp packets","drawing concentric triangles","mimicking photocopier noises","impersonating people of authority","internet spaceships"))+"."
		elif r<85.0:
			s=", yet often talks to imaginary people."
		elif r<90.0:
			s=". Believes the world to be run by shapeshifting lizard people."
		elif r<95.0:
			s=", yet is asking a chat bot for a sanity check."
		else:
			s=", but either plays, or has played, internet spaceships far too seriously"
			
		self.parent.channel_message(mucnick+" currently is "+str(r)+"% sane"+s)