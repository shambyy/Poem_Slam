from nltk.corpus import gutenberg as gt
from nltk.text import Text

corpus = gt.words('melville-moby_dick.txt')
text = Text(corpus)

#concordance shows every occurrence of word
print(text.concordance("sad"))


"""
could count occurrences of emotion words 
maybe compare number of emotion words prior to newspeak
larger difference shows we were more expressive

or:
count how many adjectives
count how many newspeak words
"""