from tensorflow.keras.layers import Input, Embedding, LSTM, Dropout, TimeDistributed, Dense
from tensorflow.keras.models import Model
import numpy as np
import emb_spacy
import label

# Définir les constantes ou configurations nécessaires
MAX_SEQ_SIZE = 92  # Taille maximale de la séquence
tailleDictionnaire = emb_spacy.get_size_dict()  # Taille du dictionnaire de mots
config = ...  # Configuration du modèle (hidden size, etc.)
nbLabels = len(label.extract_label("atis.train"))  # Nombre d'étiquettes potentielles

# Lire le fichier texte "atis.train" pour obtenir les données d'entraînement prétraitées
def lire_fichier_texte(chemin_fichier):
    donnees_train = []
    with open(chemin_fichier, 'r') as fichier:
        for ligne in fichier:
            mots = ligne.strip().split('\t')
            if len(mots) == 2:
                mot = mots[0]  # Sélectionner le premier mot
                représentation_mot = get_embedding(mot)  # Obtenir la représentation du mot
                donnees_train.append(représentation_mot)
    return np.array(donnees_train)

# Créer le modèle
def creer_modele():
    # Définir l'entrée du modèle
    entree = Input(shape=(MAX_SEQ_SIZE,), dtype='int32')

    # Créer la couche d'embedding en utilisant la fonction get_embedding
    emb = Embedding(tailleDictionnaire, 100)(entree)

    # Ajouter une couche LSTM bidirectionnelle
    bi = LSTM(config.hidden, return_sequences=True)(emb)

    # Ajouter une couche Dropout
    drop = Dropout(0.5)(bi)

    # Ajouter une couche de sortie
    out = TimeDistributed(Dense(units=nbLabels, activation='softmax'))(drop)

    # Créer le modèle
    modele = Model(inputs=entree, outputs=out)

    return modele

if __name__ == "__main__":
    # Charger les données d'entraînement
    données_entraînement = lire_fichier_texte("atis.train")

    # Créer le modèle
    modèle = creer_modele()

    # Compiler le modèle
    modèle.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Entraîner le modèle
    modèle.fit(données_entraînement, epochs=10, batch_size=32, validation_split=0.2)

    # Évaluer le modèle sur les données de test si nécessaire
    # modèle.evaluate(données_test, batch_size=32)