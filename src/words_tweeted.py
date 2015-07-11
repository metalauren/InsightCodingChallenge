tweetfile = open("/Users/marcomichaeldipalma/Desktop/Lauren/InsightCodingChallenge/tweet_input/tweets.txt", "r")  # open file
alltweets = tweetfile.read()  # read the file
tweets = alltweets.splitlines()  # a list where each element is an tweet

tweetdict = {}

for i in range(0, (len(tweets))):  # loops over every tweet
    tweets[i] = tweets[i].split()  # splits each tweet into a list of words
    for j in range(0, (len(tweets[i]))):  # loops over each word in a single tweet
        if tweets[i][j] not in tweetdict:  # checks if it is already in the dictionary of words in tweets
            tweetdict[tweets[i][
                j]] = 1  # if it is not in the dictionary, puts word in dictionary with a value (i.e. count) of 1
        else:
            tweetdict[tweets[i][
                j]] += 1  # if it is already in the dict, adds to the value associated with the word (i.e. adds 1 to the count)

keylist = list(tweetdict.keys())  # list of all the keys in the tweet dictionary.
keylist.sort()  # sorts this list. NB: Doing this at the end so it only needs to be sorted once rather than iteratively during the for loop.

ft1 = open("/Users/marcomichaeldipalma/Desktop/Lauren/InsightCodingChallenge/tweet_output/ft1.txt", "w")  # prints the word counts file
for key in keylist:
    ft1.write('%-25s %5s\n' % (key, tweetdict[key]))
ft1.close()
