# -*- coding: utf-8 -*-
"""NLPD3_assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e4Gr7KGvIzasdst8YOq9oDoMahHIlnC7
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_20newsgroups

news = fetch_20newsgroups(subset='train')

len(news.data)

news_data = pd.Series(news.data)
print(news_data[15])

news_data.str.extract(r'(?<=From: )(.+)(?=\()')

news_data.isnull().sum() #이게 제일 근사한것 같읍니다..

print(news_data[0][13])

