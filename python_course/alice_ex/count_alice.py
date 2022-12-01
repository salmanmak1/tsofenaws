print("most frequent word:")

f = open("Alice.txt", "r")
alice_txt = f.read()
f.close()
alice_words = alice_txt.split()
alice_dict = dict() #create empty dictionary

for word in alice_words:
    if word not in alice_dict:
        alice_dict[word]=1
    else:
        alice_dict[word]+=1

max_word=max(alice_dict, key=alice_dict.get) #find key with max value
print(max_word, " ", alice_dict[max_word])