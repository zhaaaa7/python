import sqlite3

reset = True

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

if reset:
	cur.execute("DROP TABLE IF EXISTS Tweets")
	cur.execute("DROP TABLE IF EXISTS Hashtags")


# Create a table to store Tweets
table_spec = 'CREATE TABLE IF NOT EXISTS Tweets (tweet_id INTEGER PRIMARY KEY AUTOINCREMENT, tweet_text TEXT, likes INTEGER)'
cur.execute(table_spec)

# Create a table to store Hashtags

table_spec = 'CREATE TABLE IF NOT EXISTS Hashtags (hashtag_id INTEGER PRIMARY KEY AUTOINCREMENT, hashtag_text TEXT, num_occurrences INTEGER)'
cur.execute(table_spec)

# Do you need a third table?

