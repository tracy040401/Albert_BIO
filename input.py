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
        for line in file:
            if line.strip():  # Si la ligne n'est pas vide
                word = line.strip().split()[0]  # Prenez le premier élément de la ligne
                current_sentence.append(word)  # Ajoutez-le à la phrase actuelle
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

'''
dans train_corpus : 
Nombre d'exemples : 4039
Taille maximale de la phrase : 92
'''