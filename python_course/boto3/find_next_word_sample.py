import re

def char_index(sentence, word_index): 
    sentence = re.split('(\s)',sentence) #Parentheses keep split characters 
    return len(''.join(sentence[:word_index*2]))

def print_secure_message(msg):
    secure_words = ['password', 'pass', 'Pass']
    cpy_msg = msg.split()
    for word in secure_words:
        # Getting index of the word's first characters
        t = re.search(word, msg)
        if t:
            # Getting index of the next word of the searched word's
            word_index = cpy_msg.index(word)+1;
            cpy_msg[word_index]='****'
    print(''.join(msg))

print_secure_message('aaa bbb pass 123 Pass 567')