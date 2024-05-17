# def split_sentences(input_file, train_output_file, test_output_file, split_ratio=0.8):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         sentences = f.readlines()

#     split_index = int(len(sentences) * split_ratio)

#     train_sentences = sentences[:split_index]
#     test_sentences = sentences[split_index:]

#     with open(train_output_file, 'w', encoding='utf-8') as f:
#         f.writelines(train_sentences)

#     with open(test_output_file, 'w', encoding='utf-8') as f:
#         f.writelines(test_sentences)

# if __name__ == "__main__":
#     input_file = "atis.train"  # Remplacez par le chemin de votre fichier contenant les phrases
#     train_output_file = "train_corpus"
#     test_output_file = "test_corpus"
#     split_ratio = 0.8  # 80% pour l'entraînement, 20% pour les tests

#     split_sentences(input_file, train_output_file, test_output_file, split_ratio)
import random

def read_phrases(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    phrases = []
    current_phrase = []

    for line in lines:
        if line.strip():  # Si la ligne n'est pas vide
            current_phrase.append(line)
        else:
            if current_phrase:
                phrases.append(current_phrase)
                current_phrase = []
    
    if current_phrase:
        phrases.append(current_phrase)

    return phrases

def split_phrases(phrases, split_ratio=0.8):
    random.shuffle(phrases)
    split_index = int(len(phrases) * split_ratio)
    train_phrases = phrases[:split_index]
    test_phrases = phrases[split_index:]
    return train_phrases, test_phrases

def write_phrases(output_file, phrases):
    with open(output_file, 'w', encoding='utf-8') as f:
        for phrase in phrases:
            f.writelines(phrase)
            f.write('\n')  # Ajout d'une ligne vide après chaque phrase

if __name__ == "__main__":
    input_file = "atis.train"  # Remplacez par le chemin de votre fichier contenant les phrases
    train_output_file = "train_corpus.txt"
    test_output_file = "test_corpus.txt"
    split_ratio = 0.8  # 80% pour l'entraînement, 20% pour les tests

    phrases = read_phrases(input_file)
    train_phrases, test_phrases = split_phrases(phrases, split_ratio)
    write_phrases(train_output_file, train_phrases)
    write_phrases(test_output_file, test_phrases)