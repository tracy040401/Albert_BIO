import spacy 
import emb_spacy

from emb_spacy import get_embedding
from input import count_examples_and_max_length, pad_sentences_from_file
import label

def main():
    # Ouverture en lecture des données
    with open("train_corpus", "r", encoding="utf-8") as file:
        data = file.readlines()

    # Compter les exemples et trouver la taille maximale
    num_examples, MAX_SEQ_SIZE = count_examples_and_max_length(data)

    # Affichage des résultats
    print("Nombre d'exemples :", num_examples) 
    print("Taille maximale de la phrase :", MAX_SEQ_SIZE)

    vec_word, sortie = pad_sentences_from_file("train_corpus", MAX_SEQ_SIZE)
    #print("vecteur : ", vec_label[0])

    # Création du vecteur d'entrée 
    entree = []
    v = []
    i = 0 
    for sentence in vec_word:
        for word in sentence:
            i+=1
            if word:
                v.append(get_embedding(word))
            else:
                zero = [0] * MAX_SEQ_SIZE
                v.append(zero)
            print(i, "/", MAX_SEQ_SIZE*num_examples)
        entree.append(v)
    print(entree[0][0])


    # on récupère la taille du dictionnaire
    tailleDictionnaire = emb_spacy.get_size_dict() 

    '''
    ########################################
    ############## MODEL LSTM ##############
    ########################################
    '''
    # Définir les constantes ou configurations nécessaires
    tailleDictionnaire = emb_spacy.get_size_dict()  # Taille du dictionnaire de mots
    # config = ...  # Configuration du modèle (hidden size, etc.)
    labels = label.extract_label("atis.train")
    nbLabels = len(labels)  # Nombre d'étiquettes potentielles
    
    '''
    TODO : 
    #X=(nbexamples*MAX_SEQ_SIZE)
    entree = Input(shape=(MAX_SEQ_SIZE,), dtype=’int32’))
    emb = Embedding(tailleDictionnaire,100)(entree)
    bi = LSTM(config.hidden, return_sequences=True)(emb)
    #bi = Bidirectional(LSTM(config.hidden, return_sequences=True))(emb)
    drop = Dropout(0.5)(bi)
    out = TimeDistributed(Dense(units=nbLabels,activation=’softmax’))(drop)
    #Y=(nbexamples*MAX_SEQ_SIZE*1)
    '''



if __name__ == "__main__":
    main()
