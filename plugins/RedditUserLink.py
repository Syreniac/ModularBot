from praw import Reddit
import random

class RedditUserLink:
	def __init__(self,parent):
		self.parent=parent
		
		self.r=Reddit(user_agent="PollBotBestBot")
		self.active=True
		self.messagable=True
		self.trackable=True
		
	def help(self,admin):
		if self.active:
			return "!u/[username] - returns a random comment from a users recent history"
		return ""
		
	def message(self,msg,admin,ignored):
		if ignored:
			return
		if self.active:
			if msg["body"].lower().startswith("!u/"):
				redditor=msg["body"].lower()[3:]
				comment=self.get_random_comment(redditor)
				if not comment is None:
					s=redditor+" wrote:\n'"+str(comment.body)+"'\n in response to "+str(comment.submission.title)+" in r/"+str(comment.subreddit.display_name)
				else:
					s="Learn to Reddit please, "+msg["mucnick"]
				
				if msg["type"]=="chat":
					self.parent.private_message(msg["from"],s)
				else:
					self.parent.channel_message(s)
	
	def get_random_comment(self,user):
		rand=random.randint(1,25)
		try:
			user=self.r.get_redditor(user)
			if user.name:
				pass
		except:
			self.parent.send_message(mto=self.parent.channel,mbody="Learn to Reddit please, "+msg["mucnick"],mtype="groupchat")
			return None
		finally:
			if not isinstance(user,str):
				comments=user.get_comments()
				comment=None
				for i in range(rand):
					try:
						comment=comments.next()
					except StopIteration:
						break
				return comment
			return None
		