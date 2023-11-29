#Biblioteca de pré-processamento de dados de texto
import nltk
from nltk.stem import PorterStemmer

import json
import pickle 
import numpy as np

#tokenizer divide um texto em uma lista de frases 
nltk.download('punkt')

#Objeto da classe PorterStemmer
stemmer = PorterStemmer()


words=[]
classes = []
word_tags_list = []
ignore_words = ['?', '!',',','.', "'s", "'m"]

#Leia arquivo json

#Carregue aquivo json

#função para anexar palavras-tronco
def get_stem_words(words, ignore_words):
    #Coloque aqui seu código


#Crie laço for para as seguintes tarefas
    
        # Adicione todas as palavras dos padrões à lista
       
        # Adicione todas as tags à lista classes

#Faça o teste usando prints

#Crie o corpus de palavras para o chatbot
