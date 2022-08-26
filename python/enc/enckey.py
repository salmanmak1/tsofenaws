from curses import keyname
import string
import random
import json
import sys

original_stdout = sys.stdout

def new_enc_key():
    letters = string.ascii_letters + ' ' + '\n'
    letters_list = list(letters)
    random.shuffle(letters_list)
    shuffled = ''.join(letters_list)
    dict_enc = {letters[i]:shuffled[i] for i in range(len(letters))}
    dict_dec = {shuffled[i]:letters[i] for i in range(len(letters))}
    return dict_enc,dict_dec

def do_enc(enc_key, plain_file1, cipher_file2):
    cipher_letters = ""
    with open (plain_file1, "r") as f1:
        file_content = f1.read()
        letters_list=list(file_content)
        for letter in letters_list:
            cipher_letters += enc_key[letter]
    with open (cipher_file2, "w+") as f2:
        sys.stdout = f2
        f2.write(cipher_letters)
        sys.stdout = original_stdout

def do_dec(dec_key, cipher_file1, plain_file2):
    plain_letters = ""
    with open (cipher_file1, "r") as f1:
        file_content = f1.read()
        letters_list=list(file_content)
        for letter in letters_list:
            plain_letters += dec_key[letter]
    with open (plain_file2, "w+") as f2:
        sys.stdout = f2
        f2.write(plain_letters)
        sys.stdout = original_stdout

def do_save(enc_dec_keys, keys_file_name):
    with open (keys_file_name, "w+") as f1:
        sys.stdout = f1
        f1.write(json.dumps(enc_dec_keys))
        sys.stdout = original_stdout

def do_load(keys_file_name):
    with open (keys_file_name, "r") as f1:
        sys.stdout = f1
        enc_dec_keys = json.loads(f1.read())
        sys.stdout = original_stdout
        return enc_dec_keys

def do_info(enc_dec_keys):
    print(f"Current key: {enc_dec_keys['key_name']}")
    print("Encryption:")
    print("".join(key for key in enc_dec_keys['enc_key']))
    print("".join(enc_dec_keys['enc_key'][value] for value in enc_dec_keys['enc_key']))
    print("Decryption:")
    print("".join(key for key in enc_dec_keys['dec_key']))
    print("".join(enc_dec_keys['dec_key'][value] for value in enc_dec_keys['dec_key']))