{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1b284f76",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "import seaborn as sns\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "98dd88c5",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pd' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m df_final \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_csv(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata/stocks.csv\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m      2\u001b[0m                      sep \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m,\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m      3\u001b[0m                       decimal \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m.\u001b[39m\u001b[38;5;124m'\u001b[39m) \u001b[38;5;241m.\u001b[39mdrop([\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mUnnamend: 0\u001b[39m\u001b[38;5;124m'\u001b[39m], axis \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m1\u001b[39m)\n\u001b[0;32m      4\u001b[0m df_final\u001b[38;5;241m.\u001b[39mdropna(inplace \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'pd' is not defined"
     ]
    }
   ],
   "source": [
    "df_final = pd.read_csv(\"data/stocks.csv\",\n",
    "                     sep = ',',\n",
    "                      decimal = '.') .drop(['Unnamend: 0'], axis = 1)\n",
    "df_final.dropna(inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2688d1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_graph_long= pd.melt(\n",
    "df_final,\n",
    "id_vars = 'date',\n",
    "var_name = 'stock',\n",
    "value_name = 'value')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc0cad5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "px.line(df_final,\n",
    "       x ='Date'\n",
    "       y = ['AAPL', 'GOOG','META','MSFT'],\n",
    "       lables = {'value': 'Dollar',\n",
    "                'Date': 'Zeit',\n",
    "                'variable': ' Aktie'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14eb1aac",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_pc = df_final.set_index(\"Date\").pct_change().resert_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d205f442",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'sns' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mnumpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mnp\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m sns\u001b[38;5;241m.\u001b[39mheatmap(df_pc\u001b[38;5;241m.\u001b[39mselect_dtypes(include \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39mnumber)\u001b[38;5;241m.\u001b[39mcorr(), annot \u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'sns' is not defined"
     ]
    }
   ],
   "source": [
    "\n",
    "sns.heatmap(df_pc.select_dtypes(include = np.number).corr(), annot =True);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "73f59f0b",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df_pc' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[5], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m df_pc\n",
      "\u001b[1;31mNameError\u001b[0m: name 'df_pc' is not defined"
     ]
    }
   ],
   "source": [
    "df_pc_long = pd.melt(\n",
    "df_pc,\n",
    "id_vars = 'Date',\n",
    "var_name = 'stock',\n",
    "value_name ='value',\n",
    ")\n",
    "\n",
    "px.line(df_pc_long,\n",
    "       x =' Date',\n",
    "       y='value',\n",
    "       color ='stock',\n",
    "       lables = {'value': 'Rendite',\n",
    "                'Date': 'zeit',\n",
    "                'stock': 'Aktie'\n",
    "                })"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ddd08a93",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df_pc' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[6], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m px\u001b[38;5;241m.\u001b[39mhistogram(df_pc\u001b[38;5;241m.\u001b[39mselect_dtypes(include \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39mnumber),\n\u001b[0;32m      2\u001b[0m             lables \u001b[38;5;241m=\u001b[39m{\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m'\u001b[39m:\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mwert\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m      3\u001b[0m                     \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mvariable\u001b[39m\u001b[38;5;124m'\u001b[39m: \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mAktie\u001b[39m\u001b[38;5;124m'\u001b[39m},\n\u001b[0;32m      4\u001b[0m             title \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m Vertreilung der Aktienrendite\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'df_pc' is not defined"
     ]
    }
   ],
   "source": [
    "px.histogram(df_pc.select_dtypes(include = np.number),\n",
    "            lables ={'value':'wert',\n",
    "                    'variable': 'Aktie'},\n",
    "            title = ' Vertreilung der Aktienrendite')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bd3cd4a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_pc.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21d8fffe",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_cret = df_pc.dropna()\n",
    "df_cumulative_returns = df_cret.set_index('date').apply(\n",
    "lambda x : (1+x).cumprodu()-1).reset_index()\n",
    "df_cumulative_returns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c463515d",
   "metadata": {},
   "outputs": [],
   "source": [
    "px.line(df_cumulative_returns,\n",
    "       x ='Date',\n",
    "       y=['AAPL','GOOG','META', 'MSFT'],\n",
    "       lables = {\n",
    "           'value':'Kummulierte Rendite'\n",
    "           'Date': 'zeit',\n",
    "           'variable': 'stock'\n",
    "       }\n",
    "       title = 'Kummulierte Rendite')\n",
    "px.line"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
