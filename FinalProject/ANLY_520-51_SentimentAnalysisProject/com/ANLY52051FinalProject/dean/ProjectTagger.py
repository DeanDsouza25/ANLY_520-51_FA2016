'''
@author: Dean D'souza
'''
# Importing required Libraries
import re
import nltk

# Main function for performing tagging (in the context of the data)
# Note: Utilizes pos_tag() provided by NLTK
def pTagger(tok):
    
    # Creating empty list holder for tagged words
    temp = [((),())]
    
    # Iteratively inspecting and tagging with custom tags
    for t in tok:
        # Matching for UserID
        if re.search('^@[A-Za-z0-9_]+$',t):
            temp.append((t,"UserID"))
            print("UserId")
        # Matching for website links
        elif re.search('^http://[A-Za-z0-9\./]+$',t):
            temp.append((t,"link"))
            print("link")
        elif re.search('^[A-Za-z0-9]+\.[A-Za-z0-9]+$',t):
            temp.append((t,"link"))
            print("link")
        # Matching for emails
        elif re.search('^[A-Za-z]+[A-Za-z0-9_\-\.\!\#\$\%\&\*\+/=\?\^\`\{\|\}\~]+@[A-Za-z\.\-]+$',t):
            temp.append((t,"email"))
            print("email")
        # Matching for hashtags, which could possibly be used to understand the topic of the post
        elif re.search('^#[A-Za-z0-9_\-\+\.]+$',t):
            temp.append((t,"htag"))
            print("hashtag")
        # This section contains conditions for matching emojis, however as the data is not supposed to contain emojis, it is left out
        elif re.search('^[\:\;\%8XB\=]{,2}[\-]?[\$\|\\#\^\<\>\&_\*3ODLSJPdC\[\]\'\{\}/\(\)@\!\,]+$',t) :
            if re.search('^[8XB3oO0DLSJPdC]+$',t):
                temp.append(nltk.pos_tag(t)[0])
                print("default")
            elif re.search('^[8XB3oO0DLSJPdC]+/[8XB3oO0DLSJPdC]+$',t):
                temp.append(nltk.pos_tag(t)[0])
                print("default")
            elif re.search('^\$[0-9]+$',t):
                temp.append((t,"num"))
                print("num")
            elif len(t)<2:
                temp.append(nltk.pos_tag(t)[0])
                print("default")
            else:
                temp.append((t,"emoji"))
                print("emoji")
        # Matching for punctuation
        elif re.search('^[\.\*\?\,\!\&/\^\`\{\|\}\~\"\$\#\'\:\s]+$',t):
            temp.append((t,"punct"))
            print("punct")
        # Matching numerical data        
        elif re.search('^[0-9]+\.?[0-9]*\$?$',t):
            temp.append((t,"num"))
            print("num")
        # Allowing for default tagging through pos_tag() function of NLTK
        elif nltk.pos_tag(t) != []:
            temp.append(nltk.pos_tag(t)[0])
            print("default")
        # Special condition to prevent tagging of empty tokens introduced due to improper Tokenization
        else:
            print("Encountered empty")
    
    # Final list of tagged tokens returned
    return temp
