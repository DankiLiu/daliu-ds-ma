import nltk

sentence = nltk.word_tokenize("Please put the milk in the fridge")
tagged = nltk.pos_tag(sentence)
print(tagged)