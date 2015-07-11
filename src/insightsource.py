tweetfile = open("tweet_input/tweets.txt", "r")  # open file
alltweets = tweetfile.read()  # read the file
tweets = alltweets.splitlines()  # a list where each element is an tweet

runningmedians = []
wordsintweet = []
tweetdict = {}


def median(x):
    x.sort()
    mid = len(x) // 2
    if len(x) % 2:
        return x[mid]
    else:
        return (x[mid - 1] + x[mid]) / 2.0


for i in range(0, (len(tweets))):  # loops over every tweet
    tweets[i] = tweets[i].split()  # splits each tweet into a list of words
    for j in range(0, (len(tweets[i]))):  # loops over each word in a single tweet
        if tweets[i][j] not in tweetdict:  # checks if it is already in the dictionary of words in tweets
            tweetdict[tweets[i][
                j]] = 1  # if it is not in the dictionary, puts word in dictionary with a value (i.e. count) of 1
        else:
            tweetdict[tweets[i][
                j]] += 1  # if it is already in the dict, adds to the value associated with the word (i.e. adds 1 to the count)
    wordsintweet.append(len(set(tweets[i])))  # maintains a list of unique word in each tweet
    runningmedians.append(median(wordsintweet))  # maintains the running median unique words for each new tweet

keylist = list(tweetdict.keys())  # list of all the keys in the tweet dictionary.
keylist.sort()  # sorts this list. NB: Doing this at the end so it only needs to be sorted once rather than iteratively during the for loop.

ft1 = open("tweet_output/ft1.txt", "w")  # prints the word counts file
for key in keylist:
    ft1.write('%-25s %5s\n' % (key, tweetdict[key]))
ft1.close()

ft2 = open("tweet_output/ft2.txt", "w")  # prints the running medians file
for med in runningmedians:
    ft2.write('%s\n' % (med))
ft2.close()
