# -*- coding: utf-8 -*-

"""main script for juriscrapper: load dict and setup matching class"""
import json
import logging
from collections import defaultdict

import spacy
from spacy.matcher import Matcher

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)

class JuriMatcher:
    "main class to match specific words in text using spaCy matcher"
    def __init__(self, dico_files, spacy_model):
        self.flat_dico, self.classified_dico = dico_files
        self.spacy_model = spacy_model

        # pipeline
        self._load_spacy_model()
        self._load_dicts()
        self._build_flat_matcher()
        self._build_class_matcher()

    def _load_spacy_model(self):
        logging.info("Loading spacy model {}".format(self.spacy_model))
        self.nlp = spacy.load(self.spacy_model)

    def _load_dicts(self):
        """load flat dict and classified dicts"""
        with open(self.flat_dico, "r") as f:
            self.flat = f.read().splitlines()
        with open(self.classified_dico, "r") as f:
            self.classif = json.load(f)

    def _add_event_ent(self, matcher, doc, i, matches):
        # Get the current match and create tuple of entity label, start and end.
        # Append entity to the doc's entity. (Don't overwrite doc.ents!)
        match_id, start, end = matches[i]
        entity = (match_id, start, end)
        doc.ents += (entity,)

    def _build_flat_matcher(self):
        "add patterns to matcher"
        logging.info("building flat matcher")
        self.flat_matcher = Matcher(self.nlp.vocab)
        pat = [[{"LOWER": u} for u in p.split()] for p in self.flat]
        self.flat_matcher.add('JUR', self._add_event_ent, *pat)

    def _build_class_matcher(self):
        """add patterns to matcher, but add entity type according to dict keys"""
        logging.info("building class matcher")
        self.classif_matcher = Matcher(self.nlp.vocab)
        res = defaultdict(list)

        for label, list_terms in self.classif.items():
            for line in list_terms:
                res[label].append([{"LOWER": u} for u in line.split()])

        self.entity_types = res.keys()
        for label, pattern in res.items():
            self.classif_matcher.add(label, self._add_event_ent, *pattern)

    def tag_doc(self, doc,  mode="flat"):
        "tag documents in one of ['flat', 'class']"
        doc = self.nlp(doc)
        if mode == "flat":
            matches = self.flat_matcher(doc)
            self.entity_types = ["JUR"]
        elif mode == "class":
            matches = self.classif_matcher(doc)
        
        # self._tag2ents(matches)
        return self._tag2ents(matches), doc

    def _tag2ents(self, matches):
        "convert entity id to string"
        return [(self.nlp.vocab.strings[lab], start, end) for lab, start, end in matches]

if __name__ == "__main__":
    FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
    logging.basicConfig(format=FORMAT)


    jm = JuriMatcher(["./dicos/merged.txt", "./dicos/cluster_merged_classif.json"], "fr_core_news_md")
    fiche_text = """Fermeture de l'entreprise pour congés: comment le salarié est-il indemnisé?\n
    L'indemnisation du salarié dépend du nombre de jours de fermeture
    de l'entreprise et du nombre de jours de congés acquis par le salarié.\n
    Si le salarié possède suffisamment de jours de congés par rapport au
    nombre de jours de fermeture de congés, il perçoit l'indemnité de congés payés dans les conditions habituelles. \n
    Si le salarié n'a pas acquis suffisamment de jours de congés payés pour être indemnisé
    durant l'intégralité de la fermeture de l'entreprise, Pôle emploi peut verser, sous conditions,
    une aide financière pour congés non payés.\nCette aide pour congés non payés est versée au salarié qui percevait,
    avant sa reprise d'emploi, l'allocation d'aide au retour à l'emploi (ARE)  ou l'allocation de solidarité spécifique
    (ASS).\nSi c'était le cas, le salarié doit formuler une demande d'aide auprès de l'agence Pôle emploi
    dont il dépendait en tant que demandeur d'emploi.\nPôle emploi\npole_emploi\n\nPôle emploi\n\n\n
    Le montant de l'aide est calculé par Pôle emploi qui tient compte \n\n\ndu nombre de jours de fermeture
    de l'entreprise;\n\n\net des droits à congés payés acquis par le salarié au titre de son nouvel emploi.
    \n\n\nÀ défaut d'avoir droit à l'aide pour congés non payés, le salarié peut demander à son employeur de bénéficier 
    de congés payés par anticipation, mais l'employeur n'est pas obligé d'accepter (sauf accord collectif ou
    usages contraires).\nLe salarié peut également demander à bénéficier d'un congé sans solde ou d'une indemnité d'activité partielle,
    en cas d'intempérie à caractère exceptionnel notamment."""

    matches, doc = jm.tag_doc(fiche_text, mode="flat")
    
    from display_entities import serve_ents, keep_longer_match
    matches = keep_longer_match(matches) # remove overlapping matches


    from display_entities import COLOR_LIST
    options = {
        "ents": list(jm.entity_types),
        "colors" : {entity:COLOR_LIST[i] for i, entity in enumerate(jm.entity_types)}
    }

    serve_ents(doc, matches, options=options)