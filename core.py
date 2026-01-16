import wordlist.wordlist as wl
import numpy as np
import sys

if not wl.init_check_is_split_wordlists():
    wl.split_sorting_wordlist('words.txt')

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
    words = list(map(wl.find_word_vectors, phrase.split(" ")))
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


phrase_1 = sys.argv[1]
phrase_2 = sys.argv[2]

vec_1 = vectorize_phrase(phrase_1)
vec_2 = vectorize_phrase(phrase_2)

print(cosine_similarity(vec_1, vec_2))
