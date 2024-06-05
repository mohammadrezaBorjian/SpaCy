import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion Barack Obama 1399-12-12 10:30 iphone14")
# doc = nlp("I want eat Apple")
# doc = nlp("my loptop is Apple")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
    
