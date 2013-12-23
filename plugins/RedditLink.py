from praw import errors,Reddit
from requests.exceptions import HTTPError, RequestException, MissingSchema, InvalidURL
import random
import datetime

def choice_pop(list):
	if len(list)==0:
		raise IndexError
	i=random.randint(0,len(list)-1)
	return list.pop(i)
	

class RedditLink:
	def __init__(self,parent):
		self.r=Reddit(user_agent="PollBotBestBot")
		self.parent=parent
		self.messagable=True
		self.trackable=False
		self.active=True
		
		self.cache=[]
		
	def help(self,admin):
		if self.active:
			return "!r/[subredditname] - return random result from a subreddit\n"
		return ""
		
	def message(self,msg,admin,ignored):
		if ignored:
			return
		if self.active:
			if msg["body"].lower().startswith("!r/"):
				m=msg["body"].lstrip("!r/")
				spli=m.split(":")
				subreddit=spli[0]
				if subreddit in self.parent.banned_subreddits:
					self.parent.send_message(mto=self.parent.channel,mbody="Nope, not touching that.",mtype="groupchat")
					return
						
				body=self.get_hot(subreddit,msg)
				if body!=None:
					self.parent.send_message(mto=self.parent.channel,mbody=body,mtype="groupchat")
			
			if msg["body"].lower().startswith("!block ") and msg["mucnick"] in self.parent.admins:
				m=m.spli(" ")
				subreddit=spli[1]
				self.parent.banned_subreddits.append(subreddit)
			
	def get_hot(self,subreddit,msg):
				
		def pick(subreddit):	
			a=None
			a1=None
			limit=random.randint(0,9)
			while limit>0:
				a1=a
				limit-=1
			return a
			
		if msg["type"]=="groupchat":
			subreddit=self.r.get_subreddit(subreddit)
			try:
				if subreddit.over18:
					pass
			except (HTTPError, errors.InvalidSubreddit) as E:
				self.parent.send_message(mto=self.parent.channel,mbody="Learn to Reddit please, "+msg["mucnick"],mtype="groupchat")
				return None
				
			if subreddit.over18:
				#self.parent.send_message(mto=self.parent.channel,mbody="NSFW content is currently blocked. Direct complaints to mods and admins.",mtype="groupchat")
				extra=" :nws: "
			else:
				extra=""
				
			submission_list=[]
			submissions=subreddit.get_hot(limit=10)
			limit=10
			while limit>0:
				try:
					submission_list.append(next(submissions))
				except StopIteration:
					break
				limit-=1
				
			submission_list_fixed=submission_list[:]
			
			submission=choice_pop(submission_list)
			while submission.title in self.cache:
				try:
					submission=choice_pop(submission_list)
				except IndexError:
					submission=random.choice(submission_list_fixed)
					break
				
				
			try:
				if len(self.cache)>10:
					self.cache=[]
				self.cache.append(submission.title)
				return "\n"+extra+str(submission.title)+extra+"\n"+extra+str(submission.url)+extra
			except AttributeError:
				return "Reddit API is currently not accepting connections. Please wait ~30 seconds before retrying."