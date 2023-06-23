import pandas as pd

import gc

import seaborn as sns
import plotly.express as px

import numpy as np

import sqlite3
from sqlite3 import Error
import os
import re, string
from nltk.corpus import stopwords
import nltk
import matplotlib.pyplot as plt

import torch
#from transformers import AutoTokenizer, BertForSequenceClassification





nltk.download("stopwords")
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


import pandas as pd
import re, string


pd.options.display.max_columns = None

#from sentence_transformers import SentenceTransformer, util
#from transformers import *

import spacy


from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn import preprocessing




palabras = pd.read_csv('/content/PRIORIZAR/data/nombres.txt', delimiter='\t')

import spacy


###### lectura de STOP WORDS

palabras = pd.read_csv('/content/PRIORIZAR/data/nombres.txt', delimiter='\t')

palabras_unicas = palabras['acosta'].tolist()

# Read the Excel file
df = pd.read_excel('/content/PRIORIZAR/data/ListadoNombresApellidos.xlsx')

# Create a list from a specific column
nuevos_nombres = df['AARON'].str.lower().tolist()


    


sw_list = stopwords.words('spanish')
sw_list += list(string.punctuation)
sw_list += ["ion","cop","whast p","rox","in","mayerli","bermuda","feb","edwin","beymar","otalvaro","carmona","pablo",
"aguirre","pineda","noviembre","enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","diciembre"
"ap","twitter","whastapp","ciudadania","b","dg","ion","app","elmer","usuario","aaron"
"yohana poveda","dirar","ud","atar","jorge","alejandro","sterns","mogollon","edwin","beymar","otalvaro","carmona","ciudadania","ap","a","saaw"
"z","''", '""', '...', '``', '’', '“','’','nn','él','tú','septiembre','hra','agosto','mayo','junio','julio','octubre','diciembre','enero','febrero',
'marzo','abril','queda','bot','$','(','correo',"email" ,"f","id",'whats','sur','”','to','titular', 'in','nombre' ,'co','sr','bis','‘','sur in', 'ac',
'‘','lt','cl',"pi","hotmail","departamentobogota","ciudadbogota","'",'-','--' ,'@hotmail','demá','facebook','razón','cliente','tel','cel','dir','mdmpqr',
'—', '_','int','gmail','com','@','re','ok','from','min','reply','avg','max','time','manifiesta','ttl','bytes','seq','ms','Reportó','Descripcion','última','atención',
'a','su','línea','linea','Gracias','preferirnos','gracias','comunicación','en','la','que','cédula','cedula','aga','luego','número','documento','indica',
'sido','aclara','solo','encuentra','comunica','linar','direccion','whatsapp','what','dirección','dire ion','pqr','juan','jose','menjura','cortes','sra',
'angela','rf','ref','ipc','cc','etb','crm','ct','chat','megas','tec','ftth',"p"]


sw_list = sw_list +palabras_unicas

sw_list=sw_list+nuevos_nombres



print(len(sw_list))


sw_set = set(sw_list)




nlp = spacy.load('es_core_news_sm', disable=['tagger', 'parser', 'ner'])



def process_data(string):
    tokens = nltk.word_tokenize(string) # tokenization
    punctuation_removed = [token.lower() for token in tokens if token.lower() not in sw_set]
    return punctuation_removed





# Stemming
from nltk.stem import PorterStemmer,SnowballStemmer
ps = SnowballStemmer(language='english')




def stemming(text_list):
    stemmed_list = []
    for text in text_list:
        doc = nlp(text)
        stemmed_tokens = [token.lemma_ for token in doc]
        stemmed_text = ' '.join(stemmed_tokens)
        stemmed_list.append(stemmed_text)
    return stemmed_list




from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


####### WITH SPACY #################

def lemmatization(string):
    lemma_list=[]
    for token in string:
        doc=nlp(token)
        lemma_list.append(doc[0].lemma_)
        #print(lemma_list)
    return lemma_list

####### WITH SPACY #################



# Conbime all functions above and obtian cleaned text data 
def data_preprocessing(text_data):
    #tokenization, stop words removal, punctuation marks removel
    processed_string=list(map(process_data,text_data))
    # stemming
    
    stemming_string=list(map(stemming,processed_string))
    
    # lemmatization
    lemma_string=list(map(lemmatization,stemming_string))
    
    return lemma_string