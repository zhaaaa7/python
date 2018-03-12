#analyze_tweets.py

import sqlite3 
import nltk
import nltk.data
from nltk import word_tokenize,sent_tokenize


conn = sqlite3.connect('tweets.db')
cur = conn.cursor()


print('***** MOST FREQUENTLY MENTIONED AUTHORS *****')

# Print the 10 most frequently mentioned authors in the entire corpus
count=1
q = "SELECT mentions, COUNT(mentions)  FROM Mentions GROUP BY mentions ORDER BY COUNT(mentions) DESC"
r = cur.execute(q)
for row in r:
	print(row[0],'is mentioned',row[1],'times')
	count+=1
	if count>10:
		break

print('*' * 20, '\n\n') # dividing line for readable output



print('***** TWEETS MENTIONING AADL *****')

# Print all tweets that mention the twitter user 'aadl' (the Ann Arbor District Library)
q = "SELECT tweettext,time_stamp FROM Tweets JOIN Mentions ON Tweets.tweet_id = Mentions.tweet_id WHERE Mentions.mentions='aadl'"
r = cur.execute(q)
for row in r:
	print(row[0],'(',row[1],')')

print('*' * 20, '\n\n')



print('***** MOST COMMON VERBS IN UMSI TWEETS *****')

# Print the 10 most common verbs ('VB' in the default NLTK part of speech tagger) 
# that appear in tweets from the umsi account
def countvb(filename):
	taglis=[]
	tagdic={}
	f1=open(filename,'r')
	r1=f1.readlines()
	for i in r1:
		dic=eval(i) 
		text=dic['text']
		tokens = nltk.word_tokenize(text)
		tagged = nltk.pos_tag(tokens)
		for j in tagged:
			if j[1]=='VB':
				taglis.append(j[0])
	for i in taglis:
		if i not in tagdic:
			tagdic[i]=0
		tagdic[i]+=1
	sorttag=sorted(tagdic,key=lambda x: tagdic[x],reverse=True)
	count=0
	for i in sorttag:
		if i!='@': 
			print(i,'(',tagdic[i],'times)')
		count+=1
		if count>10:
			break
countvb('umsitweets.json')


print('*' * 20, '\n\n')



print('***** MOST COMMON VERBS IN UMSI "NEIGHBOR" TWEETS *****')

# Print the 10 most common verbs ('VB' in the default NLTK part of speech tagger) 
# that appear in tweets from umsi's "neighbors", giving preference to tweets from
# umsi's most "mentioned" accounts
countvb('mentionedusertweets.json')
print('*' * 20, '\n\n')


conn.close()