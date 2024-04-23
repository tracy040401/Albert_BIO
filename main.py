import spacy 
import emb_spacy
from tensorflow.keras.layers import Input, Embedding, LSTM, Bidirectional, Dropout, TimeDistributed, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import ProgbarLogger


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


    

    print(' \
    #################################################################### \n \
    ########################## MODEL LSTM ############################## \n \
    #################################################################### \n \
    ')
    labels = label.extract_label("atis.train")
    nbLabels = len(labels)  # Nombre d'étiquettes potentielles
    embedding_size = len(entree[0][0])

    tailleDictionnaire = emb_spacy.get_size_dict()  # Taille du dictionnaire de mots
    config = {
        'hidden_size': 128, # Taille de la couche cachée du RNN
        'dropout_ rate': 0.3,  # Taux de dropout
        'nb_labels': nbLabels
    }  

    # Définir l'entrée du modèle
    # pas besoin de mettre le nb d'ex car il les fait passer un par un 
    input_layer = Input(shape=(MAX_SEQ_SIZE, embedding_size), dtype='float32')

    # Ajouter une couche LSTM bidirectionnelle
    bi = Bidirectional(LSTM(config['hidden_size'], return_sequences=True))(input_layer)
    drop = Dropout(config['dropout_ rate'])(bi)
    out_layer = TimeDistributed(Dense(units=config['nb_labels'], activation='softmax'))(bi)
    print('config ok')

    # Création du model
    model = Model(inputs=input_layer, outputs=out_layer)
    print("create ok")

    # Compilation du modèle
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    print("compil ok")

    # Entrainement du model 
    '''
    x : entree de la forme nb_example x MAX_SEQ_SIZE x embedding_size
    y : sortie de la forme nb_example x MAX_SEQ_SIZE
    batch_size : nb d'échantillon à utiliser à chaque itération lors de l'entrainement
    => un batch_size + gd = accélère l'entrainement mais besoin de + de mémoire GPU
    => + petit = ralentit l'entrainement mais meilleure convergence du modèle
    epochs : nb d'itération sur l'ens des données d'entrainement 
    validation_split : spécifie le fraction des données à utiliser comme données de validation
    '''
    progbar = ProgbarLogger()
    model.fit(x=entree, y=sortie, batch_size=32, epochs=10, validation_split=0.2, callbacks=[progbar])
    print('training ok')


    # TODO : remplacer val_entree/sortie par les données de test
    # loss, accuracy = model.evaluate(x=val_entree, y=val_sortie)
    # print("Loss:", loss)
    # print("Accuracy:", accuracy)





    # Ajouter une couche Dropout
    # TODO : à ajuster 
    # drop = Dropout(0.5)(bi)

    # # Ajouter une couche de sortie
    # out = TimeDistributed(Dense(units=nbLabels, activation='softmax'))(drop)

    # # Créer le modèle
    # modele = Model(inputs=entree, outputs=out)
    
if __name__ == "__main__":
    main()


'''
    TODO : 
    #X=(nbexamples*MAX_SEQ_SIZE*100)
    entree = Input(shape=(MAX_SEQ_SIZE,100), dtype=’float32’))
    bi = LSTM(config.hidden, return_sequences=True)(entree)
    #bi = Bidirectional(LSTM(config.hidden, return_sequences=True))(emb)
    drop = Dropout(0.5)(bi)
    out = TimeDistributed(Dense(units=nbLabels,activation=’softmax’))(drop)
    #Y=(nbexamples*MAX_SEQ_SIZE*1)
    '''