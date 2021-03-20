import pandas as pd

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

ranking = pd.read_html('http://www.meccanismocomplesso.org/en/meccanismo-complesso-sito-2/classifica-punteggio/')

print(ranking[0])