def split_sentences(input_file, train_output_file, test_output_file, split_ratio=0.8):
    with open(input_file, 'r', encoding='utf-8') as f:
        sentences = f.readlines()

    split_index = int(len(sentences) * split_ratio)

    train_sentences = sentences[:split_index]
    test_sentences = sentences[split_index:]

    with open(train_output_file, 'w', encoding='utf-8') as f:
        f.writelines(train_sentences)

    with open(test_output_file, 'w', encoding='utf-8') as f:
        f.writelines(test_sentences)

if __name__ == "__main__":
    input_file = "atis.train"  # Remplacez par le chemin de votre fichier contenant les phrases
    train_output_file = "train_corpus"
    test_output_file = "test_corpus"
    split_ratio = 0.8  # 80% pour l'entraînement, 20% pour les tests

    split_sentences(input_file, train_output_file, test_output_file, split_ratio)