'''
@author: Dean D'souza
'''
# Importing Required Libraries
import csv
import nltk
import math
import random
import re
import collections
from ProjectTokenizer import pToken
from nltk.corpus import stopwords

# Empty holder for all Tweets
allTweets = []

# Reading in the data from the file
csvfile = open('C:/Users/demon/OneDrive/Documents/GitHub/ANLY_520-51_FA2016/FinalProject/data/EmotionText.csv')
reader = csv.DictReader(csvfile, dialect='excel')
for row in reader:
    allTweets.append((row['content'], row['sentiment']))
csvfile.close()

# Separating based on sentiment
emptySet = [(e,s) for (e,s) in allTweets if s in ['empty']]
neutralSet = [(e,s) for (e,s) in allTweets if s in ['neutral']]
sadnessSet = [(e,s) for (e,s) in allTweets if s in ['sadness']]
happinessSet = [(e,s) for (e,s) in allTweets if s in ['happiness']]
loveSet = [(e,s) for (e,s) in allTweets if s in ['love']]
hateSet = [(e,s) for (e,s) in allTweets if s in ['hate']]
surpriseSet = [(e,s) for (e,s) in allTweets if s in ['surprise']]
reliefSet = [(e,s) for (e,s) in allTweets if s in ['relief']]
worrySet = [(e,s) for (e,s) in allTweets if s in ['worry']]

# Defining cutoffs
emCutOff = int(math.floor(len(emptySet)*0.80))
neCutOff = int(math.floor(len(neutralSet)*0.80))
saCutOff = int(math.floor(len(sadnessSet)*0.80))
hapCutOff = int(math.floor(len(happinessSet)*0.80))
loCutOff = int(math.floor(len(loveSet)*0.80))
haCutOff = int(math.floor(len(hateSet)*0.80))
suCutOff = int(math.floor(len(surpriseSet)*0.80))
reCutOff = int(math.floor(len(reliefSet)*0.80))
woCutOff = int(math.floor(len(worrySet)*0.80))

# Separating training and testing sets
trainTweets = emptySet[:emCutOff] + neutralSet[:neCutOff] + sadnessSet[:saCutOff] + happinessSet[:hapCutOff] + loveSet[:loCutOff] + hateSet[:haCutOff] + surpriseSet[:suCutOff] + reliefSet[:reCutOff] + worrySet[:woCutOff]
testTweets = emptySet[emCutOff:] + neutralSet[neCutOff:] + sadnessSet[saCutOff:]+ happinessSet[hapCutOff:] + loveSet[loCutOff:] + hateSet[haCutOff:] + surpriseSet[suCutOff:] + reliefSet[reCutOff:] + worrySet[woCutOff:]

# Randomizing the order
random.shuffle(trainTweets)
random.shuffle(testTweets)

# Creating a list of tokenized words and sentiment
tweets = []
for (content,sentiment) in trainTweets:
    tweets.append((content,sentiment))

# Function to create list of all words
def getWordsInTweets(tweets):
    wordsInTweets=[]
    for (sentences, sentiment) in tweets:
        wordsInTweets.extend(w.lower() for w in pToken(sentences) if len(w) >= 2 and w not in stopwords.words('english'))
    return wordsInTweets

# Function to get frequency distribution to be used as feature
def getWordFeatures(tWordList):
    tWordList = nltk.FreqDist(tWordList)
    wordFeats = tWordList.keys()[:1000]
    return wordFeats

tweetsFeats = getWordFeatures(getWordsInTweets(tweets))

# Function to extract features from new Tweets
def FeatExt(ttweet):
    tokWords = set(w.lower() for w in pToken(ttweet) if len(w) >= 2 and w not in stopwords.words('english'))
    feat = {}
    for e in tweetsFeats:
        feat['contains(%s)' % e] = (e in tokWords)
    feat['pemoj']=0
    for e in tokWords:
        if re.search('^[\.\*\?\,\!\&/\^\`\{\|\}\~\"\$\#\'\:\;\)\(\s]+$',e):
            if len(e) > feat['pemoj']:
                feat['pemoj'] = len(e)
    return feat

# Preparing data for building and testing Naive Bayes Classifier
trainTweetsApplied = nltk.classify.apply_features(FeatExt, trainTweets)
testTweetsApplied = nltk.classify.apply_features(FeatExt, testTweets) 

# Building the Naive Bayes classifier
classifierNB = nltk.NaiveBayesClassifier.train(trainTweetsApplied)

# Most Informative features
print(classifierNB.show_most_informative_features(30))

# Preparing data for evaluation
refSet = collections.defaultdict(set)
testFeatSet = collections.defaultdict(set)
for i, (feature,sentiment) in enumerate(testTweetsApplied):
    refSet[sentiment].add(i)
    pred= classifierNB.classify(feature)
    testFeatSet[pred].add(i)

# Evaluation function
def evaluate(refSet, testFeatSet):
    print("For empty class:")
    print("Precision:",nltk.metrics.precision(refSet['empty'], testFeatSet['empty']))
    print("Recall:",nltk.metrics.recall(refSet['empty'], testFeatSet['empty']))
    print("For neutral class:")
    print("Precision:",nltk.metrics.precision(refSet['neutral'], testFeatSet['neutral']))
    print("Recall:",nltk.metrics.recall(refSet['neutral'], testFeatSet['neutral']))
    print("For sadness class:")
    print("Precision:",nltk.metrics.precision(refSet['sadness'], testFeatSet['sadness']))
    print("Recall:",nltk.metrics.recall(refSet['sadness'], testFeatSet['sadness']))
    print("For happiness class:")
    print("Precision:",nltk.metrics.precision(refSet['happiness'], testFeatSet['happiness']))
    print("Recall:",nltk.metrics.recall(refSet['happiness'], testFeatSet['happiness']))
    print("For love class:")
    print("Precision:",nltk.metrics.precision(refSet['love'], testFeatSet['love']))
    print("Recall:",nltk.metrics.recall(refSet['love'], testFeatSet['love']))
    print("For hate class:")
    print("Precision:",nltk.metrics.precision(refSet['hate'], testFeatSet['hate']))
    print("Recall:",nltk.metrics.recall(refSet['hate'], testFeatSet['hate']))
    print("For surprise class:")
    print("Precision:",nltk.metrics.precision(refSet['surprise'], testFeatSet['surprise']))
    print("Recall:",nltk.metrics.recall(refSet['surprise'], testFeatSet['surprise']))
    print("For relief class:")
    print("Precision:",nltk.metrics.precision(refSet['relief'], testFeatSet['relief']))
    print("Recall:",nltk.metrics.recall(refSet['relief'], testFeatSet['relief']))
    print("For worry class:")
    print("Precision:",nltk.metrics.precision(refSet['worry'], testFeatSet['worry']))
    print("Recall:",nltk.metrics.recall(refSet['worry'], testFeatSet['worry']))

# Evaluating
print(nltk.classify.accuracy(classifierNB,testTweetsApplied))
evaluate(refSet,testFeatSet)