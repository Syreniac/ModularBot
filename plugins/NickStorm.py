import sleekxmpp
import ssl
from sleekxmpp.exceptions import *
import logging
import multiprocessing

class StormBot(sleekxmpp.ClientXMPP):
	def __init__(self,jid,password,nick,server,safe_channel,mucnick):
		sleekxmpp.ClientXMPP.__init__(self, jid, password)
		self.server=server
		self.jid = jid
		self.password = password
		self.nick = nick
		self.mucnick=mucnick
		self.safe_channel=safe_channel
		
		self.register_plugin('xep_0030')	 # Service discovery.
		self.register_plugin('xep_0045')	 # MUC support.
		self.register_plugin('xep_0199')	 # XMPP Ping
		
		self.mucs=[]
		
		self.seek="AgentHawk [EVAAK]"
		
		self.ssl_version = ssl.PROTOCOL_SSLv3
		
		self.ignored_channels=["spergsquad@chat.pleaseignore.com"]

		self.add_event_handler("groupchat_presence", self.updateJIDs)
		self.add_event_handler("session_start", self.start)
		
		self.scheduler.add("Disconnect",15.0,self.shut_down,repeat=False)
		
	def updateJIDs(self,msg):
		if str(msg["from"]).split("/")[1].lower()==self.seek:
			channel=str(msg["from"]).split("/")[0]
			self.send_message(mto=channel,mbody=self.mucnick+" wants you, koahi",mtype="groupchat")
		
	def start(self,arg):
		self.send_presence()
		self.get_roster()
	#	self.plugin['xep_0045'].joinMUC(self.channel, self.nick, wait=False)
		
		self.info_types = ["",'all', 'info', 'identities', 'features']
		self.identity_types = ["",'all', 'info', 'identities']
		self.feature_types = ["",'all', 'info', 'features']
		self.items_types = ["",'all', 'items']
		
		self.target_jid=self.parent.server
		self.target_node=""

		self.get = "items"
		
		try:
			items = self['xep_0030'].get_items(jid=self.target_jid,
											   node=self.target_node,
											   block=True)
		except IqError as e:
			logging.error("Entity returned an error: %s" % e.iq['error']['condition'])
		except IqTimeout:
			logging.error("No response received.")
		else:

			if self.get in self.items_types:
				for item in items['disco_items']['items']:
					if item[0]!=self.safe_channel and not item[0] in self.ignored_channels:
						self.plugin['xep_0045'].joinMUC(item[0],self.nick,wait=False)
						self.mucs.append(item[0])
		
	def shut_down(self):
		self.disconnect()
		
class NickStorm:
	def __init__(self,parent):
		self.parent=parent
		
		self.messagable=True
		self.trackable=True
		self.active=False
		
	def help(self,admin):
		if self.active:
			return "!storm - pings koahi once in every room he's in\n"
		return ""
		
	def message(self,msg,admin,ignored):
		if ignored:
			return
		if self.active and msg["type"]=="groupchat":
			if msg["body"].lower().startswith("!storm"):
				self.make_bot("PollBot@eurosquad.co.uk",
							  "A1gg24Dtxg",
							  "StormBot",
							  "eurosquad.co.uk",
							  "",
							  msg["mucnick"])
				
	def make_bot(self,jid,password,nick,server,safe_channel,mucnick):
		logging.basicConfig(format='%(levelname)-8s %(message)s')		
		sb=StormBot(jid,password,nick,server,safe_channel,mucnick)
		if sb.connect((server,5222)):
			sb.process()
		