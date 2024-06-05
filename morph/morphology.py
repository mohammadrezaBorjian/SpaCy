import spacy

nlp = spacy.load("en_core_web_sm")
# print("Pipeline:", nlp.pipe_names)
# doc = nlp("I was reading the paper	.")

doc = nlp("I was reading the paper	.")

token = doc[1]  # 'I'
print(token)
print(token.morph)  # 'Case=Nom|Number=Sing|Person=1|PronType=Prs'
print(token.morph.get("PronType"))  # ['Prs']
