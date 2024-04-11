import spacy 

from emb_spacy import get_embedding
from input import count_examples_and_max_length, pad_sentences_from_file


def main():
    with open("train_corpus", "r", encoding="utf-8") as file:
        data = file.readlines()

    # Appel de la fonction pour compter les exemples et trouver la taille maximale
    num_examples, max_length = count_examples_and_max_length(data)

    # Affichage des résultats
    print("Nombre d'exemples :", num_examples) 
    print("Taille maximale de la phrase :", max_length)

    vec = pad_sentences_from_file("train_corpus", max_length)
    print("vecteur : ", vec[0])

    vector = []
    v = []
    i = 0 
    for sentence in vec:
        for word in sentence:
            i+=1
            if word:
                v.append(get_embedding(word))
            else:
                zero = [0] * max_length
                v.append(zero)
            print(i, "/", max_length*num_examples)
        vector.append(v)
    print(vector[0][0])



if __name__ == "__main__":
    main()
