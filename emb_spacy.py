import spacy

# Charger le modèle linguistique
nlp = spacy.load("en_core_web_md")

# Obtenir l'embedding d'un mot
def get_embedding(mot):
    embedding = nlp.vocab[mot].vector
    return embedding