import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


columns = ['Overall Qual', 'SalePrice']

df = pd.read_csv('http://jse.amstat.org/v19n3/decock/AmesHousing.txt', usecols=columns, sep='\t')
columns = ['Overall Qual', 'SalePrice']

df.plot('Overall Qual', 'SalePrice')
plt.title("Comparison of how Quality affects the Sale Price")
plt.xlabel("Overall Quality")
plt.ylabel("Sale Price")
plt.xlim(0, 10.5)
plt.ylim(0,800000.5)
plt.show()

