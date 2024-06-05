import spacy

# English pipelines include a rule-based lemmatizer
nlp = spacy.load("en_core_web_sm")
# lemmatizer = nlp.get_pipe("lemmatizer")
# nlp.add_pipe("lemmatizer", config={"mode": "lookup"})

# print(lemmatizer.mode)  # 'rule'

doc = nlp("I was reading the paper. this sophisticated than he assume buy an apple for you")
print([token.lemma_ for token in doc])
# ['I', 'be', 'read', 'the', 'paper', '.']