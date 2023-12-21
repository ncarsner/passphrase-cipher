import numpy as np
import random
import re

from functions import date_key
from _adjectives import adjective
from _adverbs import adverb
from _articles import article
from _nouns import noun
from _prepositions import preposition
from _verbs import verb


sentence_structures = [
    'article-noun-verb-preposition-noun',
    'noun-verb-preposition-article-noun',
    'article-noun-verb-article-noun',
    'article-noun-verb-adjective-noun',
    'noun-verb-preposition-article-noun',
    'noun-verb-noun-preposition-noun',
    'noun-verb-article-adjective-noun',
    'noun-verb-adverb-preposition-noun',
]

word_lists = {
    "adjective": np.array(adjective),
    "adverb": np.array(adverb),
    "article": np.array(article),
    "noun": np.array(noun),
    "preposition": np.array(preposition),
    "verb": np.array(verb),
}

selected_structure = random.choice(sentence_structures)

sentence = [np.random.choice(word_lists[word_type]) for word_type in selected_structure.split("-")]

print(sentence)


# print(reference_day().strftime(("%a %b %d %H:%M %p")))

print([i for i in date_key.split()])
