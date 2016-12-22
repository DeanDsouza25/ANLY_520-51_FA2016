'''
@author: Dean D'souza
'''
# Tokenizer was created in order to handle improper Tokenization of data through the default word_tokenize() function of nltk
# These issues occurred due to the nature of the  typed data

# Importing Required Libraries
import re

# Main function to be used for Tokenization (in the context of the data)
def pToken(pSent):
    
    # Splitting based on space character
    tok = pSent.split(' ')
    
    # Declaring an empty holder for the tokens
    temp = []
    
    # Iteratively inspecting and properly Tokenizing special conditions
    for t in tok:
        # Proper Tokenization of '&' as the it was translated to '&amp;' while loading
        if re.search('^[A-Za-z0-9\'\-]*&amp;[A-Za-z0-9\'\-]*$',t):
            tlist = re.findall('[A-Za-z0-9\']+',t)
            if len(tlist) > 1:
                temp.append(tlist[0])
                temp.append('&')
                if len(tlist)>2:
                    temp.append(tlist[2])
            else:
                temp.append('&')
        # Proper Tokenization of '"' which was trasnlated to '&quot;' while loading
        elif re.search('^&quot;[A-Za-z0-9\'\-]*$',t):
            tlist = re.findall('[A-Za-z0-9\'\-]+',t)
            if len(tlist)>1:
                temp. append('"')
                temp.append(tlist[1])
            else:
                temp.append('"')       
        elif re.search('^[A-Za-z0-9\'\-]*[\!@\*\?]*&quot;$',t):
            if re.search('[A-Za-z0-9\'\-]+[\!@\*\?]*',t):
                tlist = re.findall('[A-Za-z0-9\'\-]+[\!@\*\?]*',t)
                temp.append(re.findall('[A-Za-z0-9\'\-]+',tlist[0])[0])
                if re.search('[\!@\*\?]+',tlist[0]):
                    temp.append(re.findall('[\!@\*\?]+',tlist[0])[0])
            temp. append('"')
        # Proper Tokenization of '('
        elif re.search('^\([A-Za-z0-9\'\-]*$',t):
            tlist = re.findall('[A-Za-z0-9\'\-]+',t)
            if len(tlist)>1:
                temp. append('(')
                temp.append(tlist[1])
            else:
                temp.append('(')
        # Proper Tokenization of ')'
        elif re.search('^[A-Za-z0-9\'\-]*[\!@\*\?]*\)$',t):
            if re.search('[A-Za-z0-9\'\-]+[\!@\*\?]*',t):
                tlist = re.findall('[A-Za-z0-9\'\-]+[\!@\*\?]*',t)
                temp.append(re.findall('[A-Za-z0-9\'\-]+',tlist[0])[0])
                if re.search('[\!@\*\?]+',tlist[0]):
                    temp.append(re.findall('[\!@\*\?]+',tlist[0])[0])
            temp. append(')')
        # Proper Tokenization of ','
        elif re.search('\,[A-Za-z0-9\'\-]*$',t):
            tlist = re.findall('[A-Za-z0-9\'\-]+',t)
            if len(tlist)>1:
                temp. append(',')
                temp.append(tlist[1])
            else:
                temp.append(',')
        elif re.search('^[A-Za-z0-9\'\-]*[\!@\*\?]*\,$',t):
            if re.search('[A-Za-z0-9\'\-]+[\!@\*\?]*',t):
                tlist = re.findall('[A-Za-z0-9\'\-]+[\!@\*\?]*',t)
                temp.append(re.findall('[A-Za-z0-9\'\-]+',tlist[0])[0])
                if re.search('[\!@\*\?]+',tlist[0]):
                    temp.append(re.findall('[\!@\*\?]+',tlist[0])[0])
            temp. append(',')
        # Tokenizing website links appropriately, this portion also ensures that end of sentences are properly Tokenized
        elif re.search('^[A-Za-z0-9]+\.[A-Za-z0-9]+$',t):
            if re.search('^[A-Za-z0-9]+\.[cnoim][oer][mtg]?$',t):
                temp.append(t)
            else:
                tlist = re.findall('[A-Za-z0-9]',t)
                temp.append(tlist[0])
                temp.append('.')
                if len(tlist)>1:
                    temp.append(tlist[1])
        # Proper Tokenization for text containing '...'  
        elif re.search('^[A-Za-z0-9\'\-]+(\.{2,}[A-Za-z0-9]*[\!@\*\?]*)+$',t):
            wlist = re.findall('[A-Za-z0-9\'\-]+[\!@\*\?]*',t)
            dlist = re.findall('\.{2,}',t)
            i=0
            j=0
            while i<len(wlist):
                if re.search('^[A-Za-z0-9\'\-]+[\!@\*\?]*$',wlist[i]):
                    tlist = re.findall('[A-Za-z0-9\'\-]+[!@\*\?]*',wlist[i])
                    temp.append(re.findall('[A-Za-z0-9\'\-]+',tlist[0])[0])
                    if re.search('[\!@\*\?]+',tlist[0]):
                        temp.append(re.findall('[\!@\*\?]+',tlist[0])[0])
                if j<len(dlist):
                    temp.append(dlist[j])
                i = i+1
                j = j+1
        # Proper Tokenization for punctuation attached to word tokens 
        elif re.search('^[A-Za-z0-9\'\-]+[\!@\*\?]+$',t):
            for x in re.findall('[A-Za-z0-9\'\-]+',t):
                temp.append(x)
            for x in re.findall('[\!@\*\?]+',t):
                temp.append(x)
        # Default action if string is not empty
        elif t != "":
            temp.append(t)
    
    # Final list of tokens
    return temp

# Code for testing out the function on its own
#var = raw_input("Enter the string :")
#tempList = pToken(var)
#for x in tempList:
#    print x