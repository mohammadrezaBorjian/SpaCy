import spacy
from spacy.symbols import nsubj, VERB

nlp = spacy.load("en_core_web_sm")
doc = nlp("Autonomous cars shift insurance liability toward manufacturers")
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])
    
print('----------------------')
    
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
            chunk.root.head.text)
print('----------------------')

verbs = set()
for possible_subject in doc:
    if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
        verbs.add(possible_subject.head)
print(verbs)
print('----------------------')

#Iterating around the local tree
doc = nlp("bright red apples on the tree")
print(doc)
print([token.text for token in doc[2].lefts])  # ['bright', 'red']