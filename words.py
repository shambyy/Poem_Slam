from line_gen import *

class Words:

    def __init__(self) -> None:
        self.newspeak_words = {"bad": "anodyne", "happy": "bellyfeel",}
        self.banned_word_categories = {"freedom", "independence", "joy", \
            "sadness", "pain"}
        self.fear = ['labour camp','thoughtcrime', 'unperson', 'vaporized']
        self.anger =['hate week', 'two minute hate']
        self.anticip = ['unperson']
        self.trust = ['Big Brother', 'blackwhite', 'doublethink', 'Newspeak', 'ThinkPol']
        self.surprise = ['Ingsoc', 'Golden Country']
        self.positive = ['artsem','crimestop', 'doubleplus']
        self.joy = ['goodthinkful','bellyfeel', 'goodthinker', 'joycamp']
        self.negative = ['doubleplusungood', 'crimethink', 'ownlife']
        self.sadness =['unperson']
        self.disgust = ['crimethink', 'facecrime', 'Oldspeak', 'oldthink']

    def link_to_newspeak()