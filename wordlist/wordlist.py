import os
import re

def init_check_is_split_wordlists(): # If the wordlist weren't initialized and split into fewer files
    if not os.path.exists('wl/') or not os.path.isdir('wl/'): os.makedirs('wl/')
    files = os.listdir('wl/')
    file_count = sum(1 for f in files if os.path.isfile(os.path.join('wl/', f)))
    if file_count < 10: return False
    return True

def split_sorting_wordlist(wordlist: str):
    pattern = re.compile(r'[a-zA-Z0-9]')

    file = open(wordlist, 'r')
    for line in file:
        line = line.strip()
        letter = line[0]
        if not re.search(pattern, letter): continue

        wl = open(f'wl/{letter}.txt', 'a')
        wl.write(line + '\n')

def find_word_vectors(word: str): # find word in a voccab
    letter = word[0]
    with open(f"wl/{letter}.txt", 'r') as file:
        for line in file:
            if line.startswith(word):
                return line.strip().replace("\n","")
