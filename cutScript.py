import random

def split_sentences(input_file, output_file1, output_file2, split_ratio=0.8):
    with open(input_file, 'r', encoding='utf-8') as f:
        sentences = f.readlines()

    random.shuffle(sentences)
    split_index = int(len(sentences) * split_ratio)

    sentences_train = sentences[:split_index]
    sentences_test = sentences[split_index:]

    with open(output_file1, 'w', encoding='utf-8') as f:
        f.writelines(sentences_train)

    with open(output_file2, 'w', encoding='utf-8') as f:
        f.writelines(sentences_test)

if __name__ == "__main__":
    input_file = "atis.train"
    output_file1 = "train_corpus"
    output_file2 = "test_corpus"
    split_ratio = 0.8  # 80% pour l'entraînement, 20% pour les tests

    split_sentences(input_file, output_file1, output_file2, split_ratio)