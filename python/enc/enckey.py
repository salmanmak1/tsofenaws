import string
import random

def new_enc_key():
    letters = string.ascii_letters
    letters_list = list(letters)
    random.shuffle(letters_list)
    shuffled = ''.join(letters_list)
    dict_enc = {letters[i]:shuffled[i] for i in range(len(letters))}
    dict_dec = {shuffled[i]:letters[i] for i in range(len(letters))}
    return dict_enc,dict_dec

def do_enc(enc_key ,plain_file1, cipher_file2):
    cipher_letters = ""
    with open (plain_file1, "r") as f1:
        file_content = f1.read()
        letters_list=list(file_content)
        for letter in letters_list:
            cipher_letters += enc_key[letter]
    
    with open (cipher_file2, "w") as f2:
        f2.write(cipher_letters)