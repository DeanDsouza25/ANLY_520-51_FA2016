'''
Created on Nov 29, 2016

@author: demon
'''

from __future__ import division

import nltk
from nltk.text import Text

txtFile=open('C:/Users/demon/OneDrive/Documents/GitHub/ANLY_520-51_FA2016/FinalProject/data/AllText.txt','r')
temp = txtFile.read()
tok = temp.split(' ')
txtFile.close()

print("Number of Unique Words : "+str(len(set(tok))))
print("Number of Words : "+str(len(tok)))
print("Lexical Diversity : "+str(len(tok)/len(set(tok))))

nText = Text(tok)

fdistp = nltk.FreqDist(nText)
vocab = fdistp.keys()
