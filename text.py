import tracery
from tracery.modifiers import base_english
import random
import json
import csv

encouraging_words =json.loads(open("downloadJson/encouraging_words.json").read())


rules = {
    "origin": "Don't #encorage#"
    }

rules["encorage"] = encouraging_words["encouraging_words"]
    
grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
print(grammar.flatten("#origin#"))