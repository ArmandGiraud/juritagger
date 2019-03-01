# -*- coding: utf-8 -*-

"""display utilites for spacy matcher"""

from spacy import displacy

COLOR_LIST = ["#FFE4E1",
              '#C0C0C0',
              '#808080',
              '#FFD700',
              '#FF0000',
              '#6495ED',
              '#FFFF00',
              '#808000',
              '#00FF00',
              '#008000',
              '#00FFFF',
              '#008080',
              '#FF7F50',
              '#87CEEB',
              '#FF00FF',
              '#800080']

class MyDoc:
    def __init__(self, doc):
        self.doc = doc

    def __getitem__(self, item):
        return self.doc[item].text

    def _split(self, s=None):
        return self.doc.text.split(s)

    def __add__(self, o):
        return self.doc.text + o

    def __radd__(self, o):
        return o + self.doc.text


def serve_ents(doc, matches, options, title=None):
    matches = [convert_match(match) for match in matches]
    displacy_container = [{
        "text" : MyDoc(doc),
        "ents" : matches,
        "title" : title
    }]
    displacy.serve(displacy_container, style="ent", manual=True, options=options)


def convert_match(match):
    match_out = {}
    match_out["label"] =  match[0]
    match_out["start"] =  match[1]
    match_out["end"] =  match[2]
    return match_out



def render_html():
    pass


def check_overlap(i, entity_range):
    v = []
    entity = entity_range[i]
    for j, a in enumerate(entity_range):
        if j != i and entity.intersection(a) != set():
            v.append(j)
    return v

def keep_longer_match(matches):
    entity_range = []
    for _, start, end in matches:
        entity_range.append(set(range(start, end)))

    new_matches = []
    for i in range(len(entity_range)):
        overlaps = check_overlap(i, entity_range)
        longer = [len(entity_range[over]) > len(entity_range[i]) for over in overlaps]
        equal = [len(entity_range[over]) == len(entity_range[i]) for over in overlaps]
        if any(longer):
            continue
            
        if any(equal):
            if matches[i] not in new_matches:
                new_matches.append(matches[i])
        
        else:
            new_matches.append(matches[i])
    return new_matches