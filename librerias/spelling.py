from spellchecker import SpellChecker
from unidecode import unidecode
import pandas as pd
# Load the Spanish dictionary
spell = SpellChecker(language='es')

# Set of words to skip correction
<<<<<<< Updated upstream
## prueba



skip_words = {"hbo", "winsport", "svas", "directv"}
=======
skip_words = {"hbo", "winsport", "svas", "directv","etb","facturados"}
>>>>>>> Stashed changes

def correct_sentence(sentence):
    words = sentence.split()
    corrected_words = []
    
    corrected_words = [word if word in skip_words else unidecode(spell.correction(wrd) or word) for word in words]

    corrected_sentence = ' '.join(corrected_words)
   
    return corrected_sentence