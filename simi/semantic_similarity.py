import spacy

# nlp = spacy.load("en_core_web_sm")
# tokens = nlp("dog cat banana bad")

# for token in tokens:
#     print(token.text, token.has_vector, token.vector_norm, token.is_oov)



nlp = spacy.load("en_core_web_sm")  # make sure to use larger package!
doc1 = nlp("I like salty fries and hamburgers.")
doc2 = nlp("Fast food tastes very bad.")

# Similarity of two documents
print(doc1, "<->", doc2, doc1.similarity(doc2))
# Similarity of tokens and spans
french_fries = doc1[2:4] #salty fries
burgers = doc1[5]
print(french_fries, "<->", burgers, french_fries.similarity(burgers))
