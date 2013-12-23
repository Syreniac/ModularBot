class Deedee:
	def __init__(self,parent):
		self.parent=parent
		
		self.messagable=True
		self.trackable=False
		
		self.active=False
		
	def help(self,admin):
		if self.active:
			return "!ping - ping all the deedeereddit handlers"
		return ""	
		
	def message(self,msg,admin,ignored):
		if ignored:
			return
		if self.active:
			if msg["body"].lower().startswith("!ping"):
				
				if msg["type"]=="groupchat":
					self.parent.channel_message("Aerix, courtjester, Dante Tsaronis, demeteloaf, dorisig404, gerardgendri, Hevlikn Ilunar, Jack Snipe, Jafit, Jim E Raynor, keilandnaari, Kline Eto, Ludwig Frohlich, luxspoor, NUXI, saikado, skierx, sroasa, Tycho Naskingar, Zervonn, zheothethird")
				elif msg["type"]=="chat":
					self.parent.private_message("Aerix, courtjester, Dante Tsaronis, demeteloaf, dorisig404, gerardgendri, Hevlikn Ilunar, Jack Snipe, Jafit, Jim E Raynor, keilandnaari, Kline Eto, Ludwig Frohlich, luxspoor, NUXI, saikado, skierx, sroasa, Tycho Naskingar, Zervonn, zheothethird")