from spellchecker import SpellChecker
from unidecode import unidecode
import pandas as pd
# Load the Spanish dictionary
spell = SpellChecker(language='es')


## prueba

print("hola")

skip_words = {"hbo", "winsport", "svas", "directv","etb","facturados","paramount"}


def correct_sentence(sentence):
    words = sentence.split()
    corrected_words = []
    
    corrected_words = [word if word in skip_words else unidecode(spell.correction(word) or word) for word in words]

    corrected_sentence = ' '.join(corrected_words)
    
    return corrected_sentence