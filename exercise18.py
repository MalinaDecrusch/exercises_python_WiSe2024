# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:03:13 2024

@author: s_decrusch22
"""
import pandas as pd
import matplotlib as plt
import seaborn as sns
import plotly.express as px
url = "https://api.db.nomics.world/v22/series/AMECO/UDGG.csv?dimensions=%7B%22freq%22%3A%5B%22a%22%5D%2C%22unit%22%3A%5B%22percentage-of-gdp-at-current-prices-excessive-deficit-procedure%22%5D%2C%22geo%22%3A%5B%22deu%22%2C%22ita%22%2C%22fra%22%2C%22esp%22%5D%7D&limit=1000"

df_debt = pd.read_csv(url)

df_debt.to_csv('data/df_debt.csv', sep = ",", index = False)


df_p2= df[df.country == 'china'][['year', 'lifeExp']].rename(columns = {'lifeExp':'china'})
df_p2

df_graph = df_p1.merge(df_p2,how = 'inner', on = '')

.reset_index()

#from wide to long
df_graph_long = pd.melt(
    df_graph,
    id_vers = 'year', 
    var_name = 'variable',
    value_name ='value'
    )

df_graph_long

px.line(df_graph_long,
        x ='year',
        y = 'value',
        color = 'variable'
        )