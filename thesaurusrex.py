from lxml import etree
import requests
from line_gen import *

"""Imported from Evan MiltenBurg: ThesaurusRex API"""

class Result(object):
    "General result class."
    
    def data_from_element(self, element):
        "Get weight and text from an element"
        text = element.text.strip()
        weight = int(element.attrib['weight'])
        return text, weight
    
    def dict_from_elements(self, elements):
        "Turn a list of elements into a dictionary. K: text, V: weight."
        return dict(self.data_from_element(element) for element in elements)
    
    def dict_from_xml(self, singular, plural):
        "Generate dictionary from result XML. Useful for singular/plural elements."
        results_dict = dict()
        # WHY IS THIS LEFT UNUSED
        plural_root = self.root.find(plural)
        element_generator = plural_root.iterfind(singular)
        return self.dict_from_elements(element_generator)


class SingleResult(Result):
    "Result object for a single word."
    
    base_url = "http://ngrams.ucd.ie/therex3/common-nouns/member.action?member={term}&kw={term}&needDisamb=false&xml=true"
    
    def __init__(self, word):
        query = SingleResult.base_url.format(term=word)
        response = requests.get(query)
        self.root = etree.fromstring(response.content)
        self.categories = self.dict_from_xml("Category", "Categories")
        self.modifiers = self.dict_from_xml("Modifier", "Modifiers")
        self.category_heads = self.dict_from_xml("CategoryHead", "CategoryHeads")

def trex_on_combo(combo_list):
    