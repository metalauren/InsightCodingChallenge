tweetfile = open("/Users/marcomichaeldipalma/Desktop/Lauren/InsightCodingChallenge/tweet_input/tweets.txt", "r")  # open file
alltweets = tweetfile.read()  # read the file
tweets = alltweets.splitlines()  # a list where each element is an tweet

runningmedians = []
wordsintweet = []


def median(x):
    x.sort()
    mid = len(x) // 2
    if len(x) % 2:
        return x[mid]
    else:
        return (x[mid - 1] + x[mid]) / 2.0


for i in range(0, (len(tweets))):  # loops over every tweet
    tweets[i] = tweets[i].split()  # splits each tweet into a list of words
    wordsintweet.append(len(set(tweets[i])))  # maintains a list of unique word in each tweet
    runningmedians.append(median(wordsintweet))  # maintains the running median unique words for each new tweet

ft2 = open("/Users/marcomichaeldipalma/Desktop/Lauren/InsightCodingChallenge/tweet_output/ft2.txt", "w")  # prints the running medians file
for med in runningmedians:
    ft2.write('%s\n' % (med))
ft2.close()
