import spacy
from spacy.symbols import ORTH
from spacy.lang.en import English

nlp = spacy.load("en_core_web_sm")
#doc = nlp("Apple is looking at buying USA startup for $1 billion. this startup is biggest startup of the world. Let's go")
# for token in doc:
#     print(token.lemma_)
    
#Adding special case tokenization rules
doc = nlp("gimme that")  # phrase to tokenize
# print([w.text for w in doc])  # ['gimme', 'that']

# # Add special case rule
# special_case = [{ORTH: "gim"}, {ORTH: "me"}]
# nlp.tokenizer.add_special_case("gimme", special_case)

# # Check new tokenization
# print([w.text for w in nlp("gimme that")])  # ['gim', 'me', 'that']



# nlp = English()
# text = '''"Let's go!"'''
# doc = nlp(text)
# tok_exp = nlp.tokenizer.explain(text)
# assert [t.text for t in doc if not t.is_space] == [t[1] for t in tok_exp]
# for t in tok_exp:
#     print(t[1], "\\t", t[0])

nlp = spacy.load("en_core_web_sm")
# doc = nlp(" سلام دوست عزیز پروفسور سمیعی")
doc = nlp("San Francisco Hi my friend")
for token in doc:
    print(token)
    