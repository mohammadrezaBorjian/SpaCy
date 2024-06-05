import spacy
from spacy.lang.en import English
from spacy.language import Language

#Default: Using the dependency parse NEEDS MO
# nlp = spacy.load("en_core_web_sm")
# doc = nlp("I am a boy. you are a girl")
# assert doc.has_annotation("SENT_START")
# for sent in doc.sents:
#     print(sent.text)


# Rule-based pipeline component

# nlp = English()  # just the language with no pipeline
# nlp.add_pipe("sentencizer")
# doc = nlp("This is a sentence. This is another sentence.")
# for sent in doc.sents:
#     print(sent.text)

#Custom rule-based strategy

text = "this is a sentence...hello...and another sentence."

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
print("Before:", [sent.text for sent in doc.sents])

@Language.component("set_custom_boundaries")
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == "...":
            doc[token.i + 1].is_sent_start = True
    return doc

nlp.add_pipe("set_custom_boundaries", before="parser")
doc = nlp(text)
print("After:", [sent.text for sent in doc.sents])
