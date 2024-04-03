#Before usage : pip install english-words
#               pip install nltk

import re
import sys
from english_words import get_english_words_set

def testLength(arg):
    if len(arg)<8:
        return 0
    return 1

def checkSpelChars(arg):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(regex.search(arg) == None):
        return 0
    return 1


def checkNumb(arg):
    return any(i.isdigit() for i in arg)

def checkWordList(arg):
    for i in wordset:
        if i in arg:
            return 0
    

pwd = input ( " Type in your pawword :")
test = testLength(pwd)
if test == 0: 
  print('Your paasword does not meet the lenth requirements.')
  sys.exit()
test = checkSpelChars(pwd)
if test == 0: 
  print('Your paasword does not contain any special characters.')
  sys.exit()
test = checkNumb(pwd)
if test == 0: 
  print('Your paasword does not cantain any numbers.')
  sys.exit()
wordset =list( get_english_words_set(['gcide']))
test = checkWordList(pwd)
if test == 0:
    print('Your word belongs in a forbidden list')
else:
     print('Your password has been stored: ')