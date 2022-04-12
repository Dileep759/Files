#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spacy

class Predictor:
    def __init__(self):
        self.nlp = spacy.load("trained_model")

    def predict(self, text):
        try:
            doc = self.nlp(text)
            response = {}
            for ent in doc.ents:
                response[ent.label_] = ent.text
            return response
        except:
            return {}
