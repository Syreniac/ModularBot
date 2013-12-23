# TEST GENERAL

from ModularBot import ModularBot
import logging
import ssl


jid="Bot's Jid Here"
password="Password Here"#"A1gg24Dtxg"#"dc53HeUp"

nick="Bot's Nickname here"

channel="The channel to join here"

excluded=["Excluded users go here"]

tiebreaker="The tiebreaker goes here"

server="the Server goes here"

admins=["Admin's JIDs go here"]

port=5222

banned_subreddits=["spacedicks","spaceclop","blackfathers","picsofdeadkids","sexwithdogs","gore","clopclop","treesgonewild","horsecore"]

reddit_password="You can probably ignore this"

plugin_status={"KoahiBux":False} # Any special status you want for plugins (enabled/disabled) goes here

		
if __name__=="__main__":
	logging.basicConfig(format='%(levelname)-8s %(message)s')		
			
	mb=ModularBot(jid,password,nick,channel,excluded,tiebreaker,server,admins,banned_subreddits,reddit_password,"AutoKoahi",plugin_status)
	mb.register_plugin('xep_0030')	 # Service discovery.
	mb.register_plugin('xep_0045')	 # MUC support.
	mb.register_plugin('xep_0199')	 # XMPP Ping
	mb.ssl_version = ssl.PROTOCOL_SSLv3

	if mb.connect((server,port)):
		print "Attempting to connect"
		mb.process(block=True)
	else:
		print "Failed to connect."
		exit()