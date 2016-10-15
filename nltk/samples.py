# Natural Language Tool Kit
# - Website:nltk.org
# - Documentation: http://www.nltk.org/genindex.html
# Importing the nltk data is a separate step than the module.
# When I installed the data using PiCharm nltk.download() brought up a menu box
# - http://www.nltk.org/data.html

import nltk

sample_sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."

# Prints a list of hundreds of stopwords
from nltk.corpus import stopwords
#print stopwords.words()

# Tokenize some text:
my_tokens = nltk.word_tokenize(sample_sentence)
# print my_tokens

# Tag some text
tagged = nltk.pos_tag(my_tokens)
# print tagged[0:6]

