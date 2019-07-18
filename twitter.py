# '''
# In this program, we print out all the text data from our twitter JSON file.
# Please explain the comments to students as you code.
# '''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.

tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# RANDOMTHINGS
# print(type(tweetData))
# print(type(tweetData[0]))

# AVERAGE
# favoritecount, counter = 0, 0
#
# for i in range(0,len(tweetData)):
# 	if "favorite_count" in tweetData[i]:
# 		favoritecount += tweetData[i]["favorite_count"]
# 		counter += 1
# avg = favoritecount / counter
#
# print(avg)
#
# TWEETS
tweets = []
for i in range(0,len(tweetData)):
	word = tweetData[i]["text"]
	tweets.append(word)

# print(tweets)
#POLARITY
polaritylist = []

for i in range(0,len(tweets)):
	tweet = tweets[i]
	tb = TextBlob(tweet)
	tbp = tb.polarity
	polaritylist.append(tbp)

# print(polaritylist)
# LIST OF Everything
leest = []

for i in range(len(tweetData)):
	diction = {}
	diction["Tweet_id"] = tweetData[i]["id"]
	diction["Polarity"] = polaritylist[i]
	diction["Tweet"] = tweets[i]
	leest.append(diction)

# print(leest)

tweetstr = ""
for i in tweets:
	i += " "
	tweetstr += i

# print(tweetstr)

wordcloud = WordCloud().generate(tweetstr)
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()
plt.savefig('fatouchart.png')















# # We then print the data of ONE tweet:
# # the [0] denotes the *first* tweet object.
# # We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])
#
# # First ask students how they might print the text object:
# # Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])
#
#
# # First ask students how might they use loops
# # to print the ["text"] of all the tweets:
#
# # Show them the following two options:
#
# # Explain how here, we're using index and
# # counting the number of tweets in the tweetData
# # using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])
#
# # Encourage students to think about how there are
# # often multiple solutions for each problem, and
# # how each solution might have strenghts and drawbacks.
