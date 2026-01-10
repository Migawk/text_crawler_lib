import numpy as np

def find_word_vectors(word: str): # find word in a voccab
    with open("words.txt", 'r') as file:
        for line in file:
            if line.startswith(word):
                return line.strip().replace("\n","")

def word_spliter(line: str): # split result from vocab into [word, vectors[]]
    word, *numbers = line.strip().split()

    into_float = lambda x: float(x)

    return list(map(into_float, numbers))

def normalize_vector(v):
    magnitude = np.linalg.norm(v)
    if magnitude == 0:
        return v
    return v / magnitude

def average_vectors(vectors):
    return np.mean(vectors, axis=0)

def vectorize_phrase(phrase: str):
    words = list(map(find_word_vectors, phrase.split(" ")))
    filtered_words = [w for w in words if w is not None]
    vectors = list(map(word_spliter, filtered_words))
    vectors_n = list(map(normalize_vector, vectors))

    return average_vectors(vectors_n)

def cosine_similarity(A, B):
    dot_product = np.dot(A, B)
    magnitude_A = np.linalg.norm(A)
    magnitude_B = np.linalg.norm(B)
    if magnitude_A == 0 or magnitude_B == 0:
        return 0
    return dot_product / (magnitude_A * magnitude_B)

def euclidean_distance(A, B):
    return np.linalg.norm(A - B)
