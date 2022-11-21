
import random
from nltk.corpus import brown as br
from nltk.corpus import pros_cons as pc
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from nltk.corpus import gutenberg as gt
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nrclex import NRCLex


"""Off of nltk tutorials"""

#sentences = twitter_samples.sents()
#sentences = gt.sents()
"""sentences = br.sents(categories='reviews') + br.sents(categories='romance') + \
    br.sents(categories='humor') + br.sents(categories='fiction') + \
    br.sents(categories='adventure') + br.sents(categories='science_fiction')"""
sentences = br.sents(categories='romance')
#sentences = pc.sents(categories='Pros') 
#sentences = "i have all these trolls in my box. this is sad. how?" can't
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

def generate_sentence(nb = 15): # should this be random length
    words = []
    next_word = random.choice(list(n_grams.keys()))
    words.append(next_word)
    while len(words) < nb:
        # next two lines are the og
        next_word = random.choice(n_grams[next_word]) #now from list
        words.append(next_word)

    output_line = " ".join(words)
    return output_line
    """first_half = words[:7]
    second_half = words[7:]
    print(first_half, second_half, sep=os.linesep)"""

def pull_noun(output_line):
    """takes out nouns from our sentence"""
    sentence = output_line
    nouns_adjs = [token for token, pos in pos_tag(word_tokenize(sentence)) \
        if ((pos.startswith('N')) or (pos.startswith('J')))]
    return nouns_adjs

def pull_adj(output_line):
    """takes out adjectives from our sentence"""
    sentence = output_line
    # maybe don't need sentence variable
    adjs = [token for token, pos in pos_tag(word_tokenize(sentence)) if pos.startswith('J')]
    return adjs


"""
Brown categories
['adventure', 'belles_lettres', 'editorial', 'fiction', \
    'government', 'hobbies', 'humor', 'learned', 'lore', \
    'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
"""
print("sent here")
store_1 = generate_sentence()
print("store_1:" + store_1)

noun_sent = pull_noun(store_1)
print(noun_sent)

adj_sent = pull_adj(store_1)
print(adj_sent)

# :)
#print(generate_sentence())


#should run nouns and adjectives into trex 
colors = ['pink', 'red', 'green']
def determine_emotions(nouns_adjs):
    # looks at main emotions associated with adjectives
    
    emotions_list = []
    for i in range(len(nouns_adjs)):
        # make into dict
        emotion = NRCLex(nouns_adjs[i])
        emotion_dict = nouns_adjs[i], ': ', emotion.top_emotions
        emotions_list.append(emotion_dict)

    return emotions_list 
    # if you can make this into a dict, then can put keys into trex - maybe split left of :
    # once you have list of values from trex
    # run determine_emotions 
    # pull out keys that actually have values
    # use word to create newspeak buncha if statements
    # rerun can just involve user selecting the category


    #it's only returning the first one you doofus- bc u switched to return


#list_adjs = adjs + nouns
#try next



def cleanup_emotions(emotion_dict):
    pass

#print(determine_emotions(adj_sent, noun_sent))
emotional_word = determine_emotions(noun_sent)
print(emotional_word)





#print(br.categories())
#print(twitter_samples.categories()) it doesnt have cats
#print(pc.categories())
#print(br.tagged_words(categories=['romance']))
#print(br.words(categories=['romance'])) # is mass spitting out words from romance category
#print(pc.sentences(categories='Cons')) #doesn't work