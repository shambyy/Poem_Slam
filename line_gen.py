import random
from nltk.corpus import brown as br
from nltk.corpus import pros_cons as pc
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nrclex import NRCLex

"""sentences = br.sents(categories='reviews') + br.sents(categories='romance') + \
    br.sents(categories='humor') + br.sents(categories='fiction') + \
    br.sents(categories='adventure') + br.sents(categories='science_fiction')"""

"""
Brown categories
['adventure', 'belles_lettres', 'editorial', 'fiction', \
    'government', 'hobbies', 'humor', 'learned', 'lore', \
    'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
"""

sentences = pc.sents(categories='Pros') + br.sents(categories='romance')

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

def generate_sentence(nb = 6): # should this be random length
    """ 
    args: nb, number of words that will be generated
    return: output_line, list of the n-gram generated words
    """
    words = []

    next_word = random.choice(list(n_grams.keys()))
    words.append(next_word)
    
    while len(words) < nb:
        next_word = random.choice(n_grams[next_word]) #now from list
        words.append(next_word)

    output_line = " ".join(words)
    
    return output_line

def pull_nouns_and_adjs(output_line):
    """takes out nouns from our sentence"""
    sentence = output_line
    
    nouns_adjs = [token for token, pos in pos_tag(word_tokenize(sentence)) \
        if ((pos.startswith('N')) or (pos.startswith('J')))]
    
    return nouns_adjs

print("sentence here")
n_gram_sent = generate_sentence()
print("n_gram_sent:" + n_gram_sent)

pulled_nouns_and_adjs = pull_nouns_and_adjs(n_gram_sent)
print(pulled_nouns_and_adjs)

#should run nouns and adjectives into trex 
colors = ['pink', 'red', 'green']
def determine_emotions(nouns_adjs):
    # looks at main emotions associated with adjectives
    
    to_be_converted = []
    for i in range(len(nouns_adjs)):
        # make into dict
        emotion = NRCLex(nouns_adjs[i])
        emotion_dict = nouns_adjs[i], ': ', emotion.top_emotions
        to_be_converted.append(emotion_dict)

    return to_be_converted 

def convert_to_dict(to_be_converted):
    cute_dict = {}
    words = to_be_converted
    i = 0
    
    while (i < len(words)):
        cute_dict[words[i][0]] = words[i][2]
        i += 1
    return cute_dict
    


def cleanup_emotions(emotion_dict):
    pass

#print(determine_emotions(adj_sent, pulled_nouns_r
#))
emotional_words = determine_emotions(pulled_nouns_and_adjs)
print(emotional_words)
print("indexing attempts")
print(emotional_words[0][2]) # this gives us list
print(emotional_words[0][0]) # gives us word
print(emotional_words[1][0])
print(len(emotional_words))
print("dictionary******")
print(convert_to_dict(emotional_words))

# if you can make this into a dict, then can put keys into trex - maybe split left of :
    # once you have list of values from trex
    # run determine_emotions 
    # pull out keys that actually have values
    # use word to create newspeak buncha if statements
    # rerun can just involve user selecting the category