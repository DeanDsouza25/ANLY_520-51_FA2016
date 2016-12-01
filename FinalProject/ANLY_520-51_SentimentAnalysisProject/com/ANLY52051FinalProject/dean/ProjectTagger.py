'''
Created on Nov 30, 2016

@author: demon
'''
# Importing required Libraries
import re
import nltk

# Main function for performing tagging (in the context of the data)
# Note: Utilizes pos_tag() provided by nltk
def pTagger(tok):
    temp = []
    for t in tok:
        if re.search('^@[A-Za-z0-9_]$',t):
            temp.append(t,"UserID")
        elif re.search('http://[A-Za-z0-9\./]+$',t):
            temp.append((t,"LINK"))
        elif re.search('^[A-Za-z0-9]+\.[A-Za-z0-9]+$',t):
            temp.append((t,"LINK"))
        elif re.search('^[A-Za-z]+[A-Za-z0-9_\-\.!#\$\%& *+/=\?\^\`\{\|\}\~]@[A-Za-z\.\-]$',t):
            temp.append((t,"EMAIL"))
        elif re.search('^#[A-Za-z0-9_\-\+]$',t):
            temp.append((t,"TAG"))
        else:
            temp.append(nltk.pos_tag(t)[0])
    return temp
