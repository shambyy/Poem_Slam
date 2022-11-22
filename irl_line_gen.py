import random
from nltk.corpus import brown as br
from nltk.corpus import pros_cons as pc
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nrclex import NRCLex
from words import *

"""sentences = br.sents(categories='reviews') + br.sents(categories='romance') + \
    br.sents(categories='humor') + br.sents(categories='fiction') + \
    br.sents(categories='adventure') + br.sents(categories='science_fiction')"""

"""
Brown categories
['adventure', 'belles_lettres', 'editorial', 'fiction', \
    'government', 'hobbies', 'humor', 'learned', 'lore', \
    'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
"""
# same genres as book
sentences = br.sents(categories='romance') + \
    br.sents(categories='government') + \
    br.sents(categories='fiction') + br.sents(categories='adventure') + \
    br.sents(categories='science_fiction') + br.sents(categories='lore') 
    #br.sents(categories='religion') + br.sents(categories='news')
#sentences = pc.sents(categories='Pros')

#lookup table repping n gram (we will 2 in this 2-gram dict)
#every word in corpus is a key

n_grams = {}

for sentence in sentences:
    #remove nonn char
    words = [word for word in sentence \
        if (word[0].isalpha() and word[0].lower())]
    
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
    
    return output_line.lower()

def pull_nouns_and_adjs(output_line):
    """takes out nouns from our sentence"""
    sentence = output_line
    
    nouns_adjs = [token for token, pos in pos_tag(word_tokenize(sentence)) \
        if ((pos.startswith('N')) or (pos.startswith('J')))]
    
    return nouns_adjs


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

    empty_val = [('fear', 0.0), ('anger', 0.0), ('anticip', 0.0), \
        ('trust', 0.0), ('surprise', 0.0), ('positive', 0.0), \
        ('negative', 0.0), ('sadness', 0.0), ('disgust', 0.0), ('joy', 0.0)]
    
    while (i < len(words)):
        
        cute_dict[words[i][0]] = words[i][2]
        i += 1
    
    #only show ones with values/associated emotions
    cute_dict = {key:val for key, val in cute_dict.items() if val != empty_val}
    
    return cute_dict


def list_felt_emotions(cute_dict):
    emotions_to_check = list(cute_dict.values())

    newspeak_emotions = []


    for item in emotions_to_check:

        newspeak_emotions.append([item])

    return newspeak_emotions

def iterate_emotion_tups(newspeak_emotions):
    listed_tups = []
    
    for word_list in newspeak_emotions:
        
        for tuple_list in word_list:
            
            for tup in tuple_list:
                
                for item in tup:
                    
                    listed_tups.append(item)
    
    clean = []
    
    for item in listed_tups:
        
        if type(item) is not float:
            clean.append(item)
            
    cleaned_list = list(set(clean))
    return cleaned_list

#n_gram_sent = generate_sentence()
n_gram_sent = "blue and green love"
print("n_gram_sent: ") 
print(n_gram_sent)

pulled_nouns_and_adjs = pull_nouns_and_adjs(n_gram_sent)
print(pulled_nouns_and_adjs)

emotional_words = determine_emotions(pulled_nouns_and_adjs)
print("dictionary******")
cute_emotional_dict = convert_to_dict(emotional_words)
print(cute_emotional_dict)

print("is this it???????")
please = (list_felt_emotions(cute_emotional_dict))
print("please*********************")
print(please)
print("tough*******")

tough = list(cute_emotional_dict.values())
print(list(cute_emotional_dict.values()))
print("hello cutie*********")
print(iterate_emotion_tups(please))


"""print("tough: ")
print(tough[0])
print("tough[0][0]")
print(tough[0][0])
# try
# except IndexError
print('negative' in (tough[0][0]))
print('positive' in (tough[0][0]))
print('negative' in (tough[0]))
print('positive' in (tough[0]))"""







# if you can make this into a dict, then can put keys into trex - maybe split left of :
    # once you have list of values from trex
    # pull out keys that actually have values
    # use word to create newspeak buncha if statements
    # rerun can just involve user selecting the category