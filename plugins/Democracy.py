import random
 
class Democracy:
        def __init__(self,parent):
			self.parent=parent
		   
			self.messagable=True
			self.trackable=False
			self.polling=True
		   
			self.active=True
			
			self.cache=[]
               
        def help(self,admin):
			if self.active:
					return "!democracy - ask for BrootherHood advice\n"
			return ""
                       
        def message(self,msg,admin,ignored):
			if self.active:
					if msg["body"].lower().startswith("!democracy"):
							if msg["type"]=="groupchat":
									self.parent.channel_message(self.Democracy())
							elif msg["type"]=="chat":
									self.parent.private_message(msg["from"],self.Democracy())
       
        def Democracy(self):
			commands=["CHAIRMAN CHENG WILL FAIL...GAYLENTE WILL FALL!",
					  "EMERGENCY COMMUNIST ACQUISITION DIRECTIVE: IMMEDIATE SELF-DESTRUCT. BETTER DEAD THAN RED!!",
					  "TACTICAL ASSESSMENT: RED GAYLENTE VICTORY, IMPOSSIBLE!",
					  "DEMOCRACY IS TRUTH! COMMUNISM IS DEATH!",
					  "THE LAST DOMINO FALLS HERE!",
					  "INITIATING DIRECTIVE #7395: DESTROY ALL COMMUNISTS!",
					  "COMMUNISM IS A LIE.",
					  "WE WILL NOT FEAR THE RED MENACE!",
					  "DEATH IS A PREFERABLE ALTERNATIVE TO COMMUNISM.",
					  "COMMUNISM IS THE VERY DEFINITION OF FAILURE.",
					  "FREEDOM...IS THE SOVEREIGN RIGHT OF EVERY AMERICAN.",
					  "EMBRACE DEMOCRACY, OR YOU WILL BE ERADICATED.",
					  "DEMOCRACY IS NON-NEGOTIABLE.",
					  "ENGAGING RED GAYLENTE AGGRESSORS.",
					  "WARNING: FORCIBLE IMPACT ALERT, SCANNING FOR GAYLENTE CAPITALS.",
					  "GAYLENTE SPACE WILL BE LIBERATED.",
					  "GAYLENTE's LIBERATION IS IMMINENT!",
					  "COMMENCING TACTICAL ASSESSMENT: RED GAYLENTE THREAT DETECTED.",
					  "COMMUNISTS DETECTED ON AMERICAN SOIL. LETHAL FORCE ENGAGED.",
					  "COMMUNISM IS A TEMPORARY SETBACK ON THE ROAD TO FREEDOM.",
					  "DEMOCRACY WILL NEVER BE DEFEATED!",
					  "ENGAGING GAYLENTE INVADER!",
					  "AMERICA WILL NEVER FALL TO COMMUNIST INVASION.",
					  "OBSTRUCTION DETECTED. COMPOSITION: GAYLENTE GATE CAMP. GAYLENTE BLOCKADE ATTEMPT: FUTILE!!",
					  "OBSTRUCTION DETECTED. COMPOSITION: GAYLENTE TEARS IN LOCAL. PROBABILITY OF MISSION HINDRANCE...ZERO PERCENT!!"]
			
			if len(self.cache)>=commands:
				self.cache=[]
			a=random.choice(commands)
			while a in self.cache:
				a=random.choice(commands)
			
			self.cache.append(a)
					  
			return a