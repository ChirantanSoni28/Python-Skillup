import random
wordfile = "words.txt"

def pwd_words(file):
    word_list = []
    with open(file) as words:
        for w in words:
            word = w.strip().lower()
            if 3 < len(word) < 8:
                word_list.append(word)
    return word_list

def password_generator(list):
    word = random.choices(list,k=3)
    return "".join(word)

print(password_generator(pwd_words(wordfile)))
