import random

class Composition:
	def __init__(self,parent):
		self.parent=parent
		self.active=True
		self.messagable=True
		self.trackable=False
		
		self.ships={"Rattlesnake":21,
					"Vindicator":20,
					"Bhaalgorn":20,
					"Machariel":20,
					"Nightmare":20,
					"Dominix Navy Issue":20,
					"Kronos":19,
					"Paladin":19,
					"Golem":19,
					"Vargur":19,
					"Megathron Navy Issue":19,
					"Dominix Navy Issue":19,
					"Apocalypse Navy Issue":19,
					"Armageddon Navy Issue":19,
					"Tempest Navy Issue":19,
					"Typhoon Navy Issue":19,
					"Raven Navy Issue":19,
					"Scorpion Navy Issue":19,
					"Dominix":18,
					"Sin":18,
					"Megathron":17,
					"Hyperion":17,
					"Abaddon":17,
					"Apocalypse":17,
					"Armageddon":17,
					"Rokh":17,
					"Raven":17,
					"Scorpion":17,
					"Maelstrom":17,
					"Tempest":17,
					"Typhoon":17,
					"Panther":17,
					"Redeemer":17,
					"Widow":17,
					"Eos":16,
					"Astarte":16,
					"Claymore":16,
					"Sleipnir":16,
					"Nighthawk":16,
					"Vulture":16,
					"Absolution":16,
					"Damnation":16,
					"Proteus":16,
					"Legion":16,
					"Tengu":16,
					"Loki":16,
					"Arazu":14,
					"Lachesis":14,
					"Pilgrim":14,
					"Curse":14,
					"Huginn":14,
					"Rapier":14,
					"Falcon":14,
					"Rook":14,
					"Brutix Navy Issue":14,
					"Harbinger Navy Issue":14,
					"Hurricane Navy Issue":14,
					"Drake Navy Issue":14,
					"Myrmidon":14,
					"Brutix":13,
					"Prophecy":13,
					"Harbinger":13,
					"Hurricane":13,
					"Cyclone":13,
					"Drake":13,
					"Ferox":13,
					"Oneiros":13,
					"Scimitar":13,
					"Guardian":13,
					"Basilisk":13,
					"Ishtar":13,
					"Vexor Navy Issue":13,
					"Gila":13,
					"Exequror Navy Issue":12,
					"Augoror Navy Issue":12,
					"Omen Navy Issue":12,
					"Scythe Fleet Issue":12,
					"Stabber Fleet Issue":12,
					"Osprey Navy Issue":12,
					"Caracal Navy Issue":12,
					"Vigilant":12,
					"Phantasm":12,
					"Cynabal":12,
					"Ashimmu":12,
					"Deimos":12,
					"Vagabond":12,
					"Muninn":12,
					"Zealot":12,
					"Sacrilege":12,
					"Eagle":12,
					"Cerberus":12,
					"Phobos":12,
					"Devoter":12,
					"Onyx":12,
					"Broadsword":12,
					"Exequror":10,
					"Osprey":10,
					"Scythe":10,
					"Augoror":10,
					"Vexor":8,
					"Thorax":7,
					"Celestis":7,
					"Moa":7,
					"Caracal":7,
					"Blackbird":7,
					"Rupture":7,
					"Stabber":7,
					"Bellicose":7,
					"Maller":7,
					"Omen":7,
					"Arbitrator":7,
					"Keres":6,
					"Hyena":6,
					"Sentinel":6,
					"Kitsune":6,
					"Nemesis":5,
					"Purifier":5,
					"Hound":5,
					"Manticore":5,
					"Worm":4,
					"Succubus":4,
					"Daredevil":4,
					"Dramiel":4,
					"Cruor":4,
					"Enyo":4,
					"Ishkur":4,
					"Retribution":4,
					"Vengeance":4,
					"Wolf":4,
					"Jaguar":4,
					"Hawk":4,
					"Harpy":4,
					"Griffin":4,
					"Maulus":4,
					"Vigil":4,
					"Crucifier":4,
					"Eris":3,
					"Heretic":3,
					"Sabre":3,
					"Flycatcher":3,
					"Ares":3,
					"Taranis":3,
					"Crusader":3,
					"Malediction":3,
					"Claw":3,
					"Stiletto":3,
					"Crow":3,
					"Raptor":3,
					"Algos":3,
					"Catalyst":3,
					"Talwar":3,
					"Thrasher":3,
					"Dragoon":3,
					"Coercer":3,
					"Cormorant":3,
					"Corax":3,
					"Battle indy":3,
					"Tristan":2,
					"Incursus":2,
					"Navitas":2,
					"Atron":2,
					"Punisher":2,
					"Tormentor":2,
					"Inquisitor":2,
					"Executioner":2,
					"Merlin":2,
					"Kestrel":2,
					"Bantam":2,
					"Condor":2,
					"Rifter":2,
					"Slasher":2,
					"Breacher":2,
					"Burst":2,
					"Immolator":2,
					"Echo":2,
					"Hematos":2,
					"Taipan":2,
					"Violator":2}
					
		self.offense_options=["AC fit",
							  "Arty fit",
							  "Beam fit",
							  "Pulse fit",
							  "SR Missile fit",
							  "LR Missile fit",
							  "Drone damage fit",
							  "RR Fit",
							  "Tackle fit"]
							  
		self.defense_options=["Shield tanked",
							  "Hull tanked",
							  "Armor tanked",
							  "Honour tanked",
							  "Speed tanked",
							  "E-war tanked"]
		
	def help(self,admin):
		if self.active:
			return "!comp - suggests a fleet composition for SCL\n"
		return ""
		
	def message(self,msg,admin,ignored):
		if ignored:
			return
		if self.active:
			if msg["body"].lower().startswith("!comp"):
				if msg["type"]=="chat":
					self.parent.private_message(msg["from"],self.get_comp())
				else:
					self.parent.channel_message(self.get_comp())
				
	def get_comp(self):
		def get_entry(limit):
			l=[]
			for i in self.ships:
				if self.ships[i]<=limit:
					l.append(i)
					
			ship=random.choice(l)
			point_value=self.ships[ship]
			r=random.randint(1,3)
			while point_value*r>limit:
				r-=1
				
			offense_option=random.choice(self.offense_options)
			defense_option=random.choice(self.defense_options)
			plural=""
			if r>1:
				if ship.endswith("s") or ship.endswith("x"):
					plural="es"
				else:
					plural="s"
			
			return str(r)+" "+defense_option+" "+offense_option+" "+ship+plural+"\n",point_value*r,r
				
			
		def get_entries():
			entries="\n"
			points=85
			a=0
			while points>=2:
				entry,point,amount=get_entry(points)
				points-=point
				entries+=entry
				a+=amount
			
			return entries+"@ "+str(85-points)+" points",a
			
		a=11
		s=""
		while a!=10:
			s,a=get_entries()
			
		return s
			