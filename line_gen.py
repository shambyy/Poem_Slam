from nltk.corpus import gutenberg as gt
from nltk.text import Text
import random
from nltk.corpus import brown as br
from nltk.corpus import pros_cons as pc

"""Off of nltk tutorials"""

#sentences = gt.sents()
sentences = pc.sents(categories='Pros')
#how many sentences in this set
#print(len(sentences))

#printing a few words
#print(gt.words())

#this does the same as the last thing
#print first sent
#print(sentences[0])

#lookup table repping n gram (we will 2 in this 2-gram dict)
#every word in corpus is a key

n_grams = {}

for sentence in sentences:
    #remove nonn char
    words = [word for word in sentence if word[0].isalpha()]
    for i in range(len(words) - 1):
        #every ending word ignored (bc no list of words after)
        try:
            n_grams[words[i]].append(words[i + 1])
        except KeyError as _:
            #if first time word is being seen
            n_grams[words[i]] = []
            #append in unseen
            n_grams[words[i]].append(words[i+1])

def generate_sentence(nb = 7):
    words = []
    next_word = random.choice(list(n_grams.keys()))
    words.append(next_word)
    while len(words) < nb: 
        next_word = random.choice(n_grams[next_word]) #now from list
        words.append(next_word)
    
    return " ".join(words)

generate_sentence()
print("sent here")
print(generate_sentence())
#print(generate_sentence())
#how do i make it more sensible at end?
#tokenization...

corpus = gt.words('melville-moby_dick.txt')
text = Text(corpus)

#concordance shows every occurrence of word
#print(text.concordance("sad"))

#print(br.categories())
#print(br.tagged_words(categories=['romance']))
#print(br.words(categories=['romance']))
#print(pc.sentences(categories='Cons')) #doesn't work

"""If you have user put in pro or con then can pull those words for line2
then for line3 maybe just link the pro usage to newspeak words?
so line1 is their word inserted into random sentence and so forth

but still how to eval??"""