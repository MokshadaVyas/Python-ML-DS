import nltk
nltk.download('punkt')

from nltk import sent_tokenize
from nltk import word_tokenize

corpus="Hello, my name is Mokshada.I am a machine learning enthusiast! In this tutorial, we will explore the concept of tokenization."
print(corpus)
sentence = sent_tokenize(corpus)
print(sentence)

word=word_tokenize(corpus)
print(word)