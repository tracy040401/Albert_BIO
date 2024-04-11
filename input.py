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
    labels = []
    with open(input_file, "r", encoding="utf-8") as file:
        current_sentence = []
        current_sentence_label = []
        for line in file:
            if line.strip():  # Si la ligne n'est pas vide
                word = line.strip().split()[0]  # Prend le premier élément de la ligne
                label = line.strip().split()[1] # Prend le deuxième élt de la ligne
                current_sentence.append(word)  # Ajout à la phrase actuelle
                current_sentence_label.append(label) # Ajout du label à la phrase 
            else:
                if current_sentence:  # Si la phrase actuelle n'est pas vide
                    sentences.append(current_sentence)  # Ajout à la liste des phrases
                    labels.append(current_sentence_label)
                    current_sentence = []  # Réinit la phrase/label actuelle
                    current_sentence_label = []

        if current_sentence:
            sentences.append(current_sentence)

        if current_sentence_label:
            labels.append(current_sentence_label)

        vectors_sentences = []
        vectors_labels = []
        for sentence, label in zip(sentences, labels):
            sentence = sentence + [0] * (SIZE - len(sentence))
            label = label + [0] * (SIZE - len(label))
            vectors_sentences.append(sentence)
            vectors_labels.append(label)

    return vectors_sentences, vectors_labels




'''
dans train_corpus : 
Nombre d'exemples : 4039
Taille maximale de la phrase : 92
'''