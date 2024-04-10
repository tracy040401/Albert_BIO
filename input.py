def count_examples_and_max_length(data):
    num_examples = 0
    max_length = 0

    current_length = 0
    for line in data:
        if line.strip():  # Check if the line is not empty
            current_length += 1
        else:
            num_examples += 1
            max_length = max(max_length, current_length)
            current_length = 0
    
    # Handle the case if the last example doesn't end with an empty line
    if current_length > 0:
        num_examples += 1
        max_length = max(max_length, current_length)

    return num_examples, max_length

def pad_sentences_from_file(input_file, SIZE):
    sentences = []
    with open(input_file, "r", encoding="utf-8") as file:
        current_sentence = []
        i = 0 
        for line in file:
            if line.strip() and i < 3 :  # Si la ligne n'est pas vide
                print(line)
                word = line.strip().split()[0]  # Prenez le premier élément de la ligne
                print("word : ", word)
                current_sentence.append(word)  # Ajoutez-le à la phrase actuelle
                print(current_sentence)
                i+=1
            else:
                if current_sentence:  # Si la phrase actuelle n'est pas vide
                    sentences.append(current_sentence)  # Ajoutez-la à la liste des phrases
                    current_sentence = []  # Réinitialisez la phrase actuelle

        # Assurez-vous de traiter la dernière phrase si elle n'est pas suivie d'une ligne vide
        if current_sentence:
            sentences.append(current_sentence)

    padded_vectors = []
    for sentence in sentences:
        padded_sentence = sentence + [0] * (SIZE - len(sentence))
        padded_vectors.append(padded_sentence)
    
    return padded_vectors

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


if __name__ == "__main__":
    main()

'''
dans train_corpus : 
Nombre d'exemples : 4039
Taille maximale de la phrase : 92
'''