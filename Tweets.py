'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
# Continue your program below!

polarty = []
subjectiv = []

for tweet in tweetData:
    text = tweet["text"]
    tb = TextBlob(text)

    polar = tb.polarity
    polarty.append(polar)

    subj = tb.subjectivity
    subjectiv.append(subj)

plt.hist(polarty, bins = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])
plt.xlabel('Feeling scale')
plt.ylabel('Tweets')
plt.title('Polarity')
plt.axis([-1,1,0,100])
plt.grid(True)
plt.show()

plt.hist(subjectiv, bins = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])
plt.xlabel('Feeling scale')
plt.ylabel('Tweets')
plt.title('Subjectivity')
plt.axis([-1,1,0,100])
plt.grid(True)
plt.show()


alltext = ""

for twt in tweetData:
    txt = twt["text"]
    alltext += str(txt)
    thetexts = TextBlob(txt)
#print(alltext)
filtered = {}
wordlist = thetexts.words
for word in wordlist:
    #filters
    if len(word) <= 2:
        continue
    else:
        filtered[word] = thetexts.word_counts[word]

wordcloud = WordCloud().generate_from_frequencies(filtered)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()
