import sqlite3
import tweepy
from tweepy import OAuthHandler
import json
import datetime, time

CONSUMER_KEY = 'IyFWeJnaeGjpxfUiCVS81ayz5'          
CONSUMER_SECRET = 'E2q3F9oRQvbFuOyH4ioXXUQ93LhHwrj9RrQDZuPmoTmIGWSbaR'     
ACCESS_TOKEN = '3875764692-Hx1EervO3KzeQYeoTDqQsVjzrKeyrf4Jk63NWhQ'             
ACCESS_TOKEN_SECRET = 'm87V4bqsMWZ9j1QS8yFGCSO5B7hG3Y4xfhpnrOkFgUc0Q'  


#config tweet api
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#create database
reset = True
conn = sqlite3.connect('tweets.db')
cur = conn.cursor()
if reset:
    cur.execute("DROP TABLE IF EXISTS Tweets")
    cur.execute("DROP TABLE IF EXISTS Mentions")
    cur.execute("DROP TABLE IF EXISTS Authors")

#creat 3 tables
table_spec = 'CREATE TABLE IF NOT EXISTS Tweets (tweet_id INTEGER PRIMARY KEY AUTOINCREMENT, author_id INTEGER, time_stamp TEXT,tweettext TEXT)'
cur.execute(table_spec)

table_spec = 'CREATE TABLE IF NOT EXISTS Mentions (allno INTEGER PRIMARY KEY AUTOINCREMENT,tweet_id INTEGER, author_id INTEGER, mentions TEXT)'
cur.execute(table_spec)

table_spec = 'CREATE TABLE IF NOT EXISTS Authors (author_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT)'
cur.execute(table_spec)


#fetch umis tweets 371
flag=True
page = 1
json_file=open('umsitweets.json', 'w')
while flag:
    tweets = api.user_timeline(id='umsi',count=20,page=page) 
    for tweet in tweets:
        if tweet.created_at>datetime.datetime(2016,9,1):
            json_tweet = tweet._json 
            json_file.write(str(json_tweet)+'\n')
        else:
            flag=False
            break       
    page += 1

#get mentioned users screenname
each_tweet_mentioned=[]
mentioned_dic={}
j=open('umsitweets.json','r')
r=j.readlines()
for i in r:
    inlis=[]
    dic=eval(i)    
    mentinoned=dic['entities']['user_mentions'] 
    for j in mentinoned:
        inlis.append(j['screen_name'])
    each_tweet_mentioned.append(tuple(inlis))# 371 items with each as a tuple
    for each in inlis:
        if each not in mentioned_dic:
            mentioned_dic[each]=0
        mentioned_dic[each]+=1



#insert values into Mentions table
def inserttomentions(filename):
    count=0
    j=open(filename,'r')
    r=j.readlines()
    for i in r:
        inlis=[]
        dic=eval(i)
        tweetid=dic['id']
        authorid=dic['user']['id']
        if each_tweet_mentioned[count]==():
            mention=None
        else:
            mention=each_tweet_mentioned[count]
            for each_item in mention:
                #print(each_item)
                item=(None,tweetid,authorid,each_item)
                statement = 'INSERT INTO Mentions VALUES (?, ?, ?, ?)'
                cur.execute(statement, item)
                conn.commit()

        count+=1
inserttomentions('umsitweets.json')


#get the first 20 most mentioned users, including umsi
sort_mention_dic=sorted(mentioned_dic,key=lambda x:mentioned_dic[x],reverse=True)
mentioned_user_list=[]
count=1
for i in sort_mention_dic:
    mentioned_user_list.append(i)
    if count>19:
        break
    count+=1
#get most mentioned user most recent 20 tweets
def getmentionedtweets(name):
    json_lis=[]
    tweets = api.user_timeline(id=name,count=20) 
    for tweet in tweets:
        if tweet.created_at>datetime.datetime(2016,9,1):
            json_tweet = tweet._json 
            json_lis.append(json_tweet)
        else:
            break
    return json_lis
mentioned_user_tweets=[]

#fetch 380 mentioned user's tweets
for i in mentioned_user_list:
    if i!='umsi':
        mentioned_user_tweets+=getmentionedtweets(i)
json_file=open('mentionedusertweets.json', 'w')
for i in mentioned_user_tweets:
   json_file.write(str(i)+'\n')
json_file.close()


#insert value into Tweets table
def inserttotweets(filename):
    data_items=[]
    j=open(filename,'r')
    r=j.readlines()
    for i in r:
        dic=eval(i)
        tweetid=dic['id']
        authorid=dic['user']['id']
        time=dic['created_at']
        text=dic['text']
        data_items.append((tweetid,authorid,time,text))  
    statement = 'INSERT INTO Tweets VALUES (?, ?, ?, ?)'
    for item in data_items:
        cur.execute(statement, item)
    conn.commit()
inserttotweets('mentionedusertweets.json')
inserttotweets('umsitweets.json')



#find mentions of mentioned users
each_tweet_mentioned=[]
mentioned_dic={}

j=open('mentionedusertweets.json','r')
r=j.readlines()
for i in r:
    inlis=[]
    dic=eval(i)    
    mentinoned=dic['entities']['user_mentions'] 
    for j in mentinoned:
        inlis.append(j['screen_name'])
    each_tweet_mentioned.append(tuple(inlis))# 371 items with each as a tuple
    for each in inlis:
        if each not in mentioned_dic:
            mentioned_dic[each]=0
        mentioned_dic[each]+=1
#insert new mentioned info into Mentioan table
inserttomentions('mentionedusertweets.json')

#merge umsi mentioned.json
f1=open('umsitweets.json','r')
r1=f1.readlines()
f2=open('mentionedusertweets.json','r')
r2=f2.readlines()
all=r1+r2
f=open('alltweets.json','w')
for i in all:
    f.write(i)
f.close()
#insert value into Authors table
userid_lis=[]
q = 'SELECT DISTINCT author_id FROM Tweets'
r = cur.execute(q)
for row in r:
    userid_lis.append((row[0]))
fusername=open('alltweets.json','r')
rusername=fusername.readlines()
data_items=[]
for i in userid_lis:
    for j in rusername:
        dic=eval(j)
        if dic['user']['id']==i:
            username=dic['user']['screen_name']
            data_items.append((i,username))
            break
statement = 'INSERT INTO Authors VALUES (?, ?)'
for item in data_items:
    cur.execute(statement, item)
conn.commit()


conn.close()






