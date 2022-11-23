import random
from nltk.corpus import brown as br
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nrclex import NRCLex
import os


matching_genres = ['romance', 'government', 'fiction', 'science_fiction', \
    'lore']
print(matching_genres)
category = input("Which of the above genres of "'1984'" interest you? ")

if category == 'romance':
    sentences = br.sents(categories='romance')
if category == 'government':
    sentences = br.sents(categories='government')
if category == 'fiction':
    sentences = br.sents(categories='fiction')
if category == 'science_fiction':
    sentences = br.sents(categories='science_fiction')
if category == 'lore':
    sentences = br.sents(categories='lore')


# Line generation prep

n_grams = {}

for sentence in sentences:
    
    # remove unwanted characters
    words = [word for word in sentence \
        if (word[0].isalpha() and word[0].lower())]
    
    for i in range(len(words) - 1):
        # con: every ending word ignored (bc no list of words after)
        # con: exception does not always catch

        try:
            n_grams[words[i]].append(words[i + 1])

        except KeyError as _:
            #if unseen
            n_grams[words[i]] = []
            #append in unseen
            n_grams[words[i]].append(words[i+1])


def generate_sentence(num_words = 26): 
    """ 
    Creates line based off of above prep work
    args: num_words, number of words that will be generated
    return: output_line, list of the n-gram generated words
    """

    words = []

    next_word = random.choice(list(n_grams.keys()))
    words.append(next_word)
    
    while len(words) < num_words:
        next_word = random.choice(n_grams[next_word]) #now from list
        words.append(next_word)

    output_line = " ".join(words)
    output_line = output_line.lower()
    
    return output_line


def pull_nouns_and_adjs(output_line):
    """
    Takes out nouns and adjectives from our sentence
    args: line in full
    returns: nouns, adjectives, and superlatives aka emotional words
    """

    sentence = output_line

    nouns_adjs = [token for token, pos in pos_tag(word_tokenize(sentence)) \
        if ((pos.startswith('N')) or (pos.startswith('J')))]
    
    return nouns_adjs


def sentence_frame(output_line):
    """
    Takes out frame from our sentence
    args: line in full
    return: non-nouns, non-adjectives, and non-superlatives
    """
    
    sentence = output_line

    frame = [token for token, pos in pos_tag(word_tokenize(sentence)) \
        if not ((pos.startswith('N')) or (pos.startswith('J')))]
    
    return frame


def determine_emotions(nouns_adjs):
    """
    Finds tagged emotions via line and Lexicon
    args: list of emotional words
    return: main emotions associated with emotional words
    """
    # looks at main emotions associated with adjectives
    
    to_be_converted = []
    for i in range(len(nouns_adjs)):
        # make into dict
        emotion = NRCLex(nouns_adjs[i])
        emotion_dict = nouns_adjs[i], ': ', emotion.top_emotions
        to_be_converted.append(emotion_dict)

    return to_be_converted 


def convert_to_dict(to_be_converted):
    """
    Evaluation metric to proceed onto phase 2!
    arg: tagged emotions list
    return: dictionary with levels of emotions
    
    """
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
    """
    Pulls out only emotional words with scores from previous dict
    arg: dictionary with emotion scoring
    return: basic emotions found in first emotional line
    """
    emotions_to_check = list(cute_dict.values())
    newspeak_emotions = []

    for item in emotions_to_check:

        newspeak_emotions.append([item])

    return newspeak_emotions


def iterate_emotion_tups(newspeak_emotions):
    """
    Return tagged emotions from first line (of Lexicon)
    arg: emotional word list
    return: list of emotions expressed in emotional line
    """

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


# commence phase two 
n_gram_sent = generate_sentence()
#n_gram_sent = "blue and green this our love"
print("n_gram_sent: ") 
print(n_gram_sent)

pulled_nouns_and_adjs = pull_nouns_and_adjs(n_gram_sent)
print(pulled_nouns_and_adjs)

emotional_words = determine_emotions(pulled_nouns_and_adjs)
print("dictionary******")
cute_emotional_dict = convert_to_dict(emotional_words)
print(cute_emotional_dict)


list_list_tups_emotions = (list_felt_emotions(cute_emotional_dict))
print("tagged emotions*********")
tagged_emotions = iterate_emotion_tups(list_list_tups_emotions)
print(tagged_emotions)


def link_to_newspeak(cleaned_list):

    fear = ['labour camp','thoughtcrime', 'unperson', 'vaporized']
    anger =['hate week', 'two minute hate']
    anticip = ['unperson']
    trust = ['Big Brother', 'blackwhite', 'doublethink', 'Newspeak', \
        'ThinkPol']
    surprise = ['Ingsoc', 'Golden Country']
    positive = ['artsem','crimestop', 'doubleplus']
    joy = ['goodthinkful','bellyfeel', 'goodthinker', 'joycamp']
    negative = ['doubleplusungood', 'crimethink', 'ownlife']
    sadness =['unperson']
    disgust = ['crimethink', 'facecrime', 'Oldspeak', 'oldthink']

    newspeak_options = []
    
    for i in cleaned_list:
        if 'fear' == i:
            newspeak_options.append(fear)
        if 'anger' == i:
            newspeak_options.append(anger)
        if 'anticip' == i:
            newspeak_options.append(anticip)
        if 'trust' == i:
            newspeak_options.append(trust)
        if 'surprise' == i:
            newspeak_options.append(surprise)
        if 'positive' == i:
            newspeak_options.append(positive)
        if 'joy' == i:
            newspeak_options.append(joy)
        if 'negative' == i:
            newspeak_options.append(negative)
        if 'sadness' == i:
            newspeak_options.append(sadness)
        if 'disgust' == i:
            newspeak_options.append(disgust)

    newspeak_options_list = []
    
    for emotion in newspeak_options:
        
        for vocab in emotion:
            newspeak_options_list.append(vocab)
    
    return newspeak_options_list


def newspeak_integrated_line(frame, words_to_add):
    """generate line with newspeak words"""

    newspeak_start = random.choice(words_to_add)
    frame.insert(0, newspeak_start )

    newspeak_mid = random.choice(words_to_add)
    frame = frame[:len(frame)//2] + [newspeak_mid] + frame[len(frame)//2:]

    newspeak_end = random.choice(words_to_add)
    frame.append(newspeak_end)

    frame = " ".join(frame)

    return frame


def printing_cuter_a(long_string):
    """slice line in two for poem effect, this is the first portion"""
    part_a = long_string[:len(long_string)//2]
    return part_a

def printing_cuter_b(long_string):
    """slice line in two for poem effect, this is the second portion"""
    part_b = long_string[len(long_string)//2:]
    return part_b

n_gram_sent2 = generate_sentence()
book_line = sentence_frame(n_gram_sent2)
noun_adj_book_line = pull_nouns_and_adjs(n_gram_sent2)
print("second generated line**********")
print(n_gram_sent2)
print(book_line)
print(noun_adj_book_line)
print("emotions list:")
test = link_to_newspeak(tagged_emotions)
print(test)
print(random.choice(test))
print("plese im so tierd")
godly = newspeak_integrated_line(noun_adj_book_line, test)
print("LET'S SEEEEEEEEEEE")
print(printing_cuter_a(n_gram_sent))
print(printing_cuter_b(n_gram_sent))
print(godly)
os.system("say " + n_gram_sent)
os.system("say " + godly)
print("last one*****")

