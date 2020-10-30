

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BUAFY-EZXhaXvkFUBd5e0cznTD2csEzX
"""

import pandas as pd
import numpy as np

!pip install xlrd

df.iloc[:, 9:43].head()

df.rename(columns = { 'OdName' : 'Country', 'AreaName' : 'Continent', 'RegName' : 'Region'}, inplace = True)
df_canada = df.set_index('Country') #set index as one of the columns
df_canada['Total'] = df_canada.iloc[:, 8:42].sum(axis = 1)
df_canada.drop(['Type', 'Coverage', 'AREA', 'REG', 'DEV'], axis =1, inplace = True)
df_canada.head()

# Commented out IPython magic to ensure Python compatibility.
import matplotlib as npl
import matplotlib.pyplot as plt
# %matplotlib inline

years = list(range(1980, 2014))
df_canada.loc['Haiti', years].plot(kind = 'line')
df_canada.drop(['Type', 'Coverage', 'AREA', 'REG', 'DEV'], axis =1, inplace = True)
plt.title('Immigrations from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()
df_canada.loc['Haiti', years].head()

df_canada.sort_values(['Total'], ascending = False, axis = 0, inplace = True)
df_canada.head()

df_top5 = df_canada.head()
df_top5 = df_top5[years].transpose()
df_top5

df_top5.plot(kind = 'area')
plt.title('Immigration trend of top 5 countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()

count, bin_edges = np.histogram(df_canada[2013])
df_canada[2013].plot(kind = 'hist', xticks = bin_edges)
plt.title('Immigration in year 2013')
plt.ylabel('Number of Countries')
plt.xlabel('Frequency of Immigrants')

plt.show()

df_iceland = df_canada.loc['Iceland', years]
df_iceland.plot(kind = 'bar')
plt.title('Icelandic Immigrants to Canada from 1980 to 2013')
plt.ylabel('Number of Immigrants')
plt.xlabel('Year')

plt.show()

df_continent = df_canada.groupby('Continent', axis = 0).sum()

df_continent['Total'].plot(kind = 'pie')
plt.title('Immigration to Canada by Continent (1980-2013)')
plt.show()

df_japan = df_canada.loc['Japan', years]
df_japan.plot(kind = 'box')
plt.title('Box plot of Japanese Immigrants from 1980-2013')
plt.ylabel('Number of Immigrants')
plt.show()

df_canada

df_total = pd.DataFrame(df_canada.iloc[:,3:42].sum(axis = 0))
df_total = df_total.reset_index()
df_total.drop(index = 34, axis = 0, inplace = True)
df_total.columns = ['Years', 'Total']
df_total['Years'] = df_total['Years'].astype('int64')
df_total

df_total.plot(kind = 'scatter', x = 'Years', y = 'Total')
plt.title('Immigrants Year Wise')
plt.xlabel('years')
plt.ylabel('No. of Immigrants')
plt.show()

import seaborn as sns
ax = sns.regplot( x = 'Years', y = 'Total', data = df_total)

!pip install folium

import folium
world_map = folium.Map( 
    location = [56.130, -106.35], 
    zoom_start = 4, 
    titles = 'Mapbox Bright'
)
world_map

ontario = folium.map.FeatureGroup()
ontario.add_child(
    folium.CircleMarker(
    [51.25, -85.32], radius = 5,
     color = 'red', fill_color = 'Red'
     )
)

world_map.add_child(ontario)

folium.Marker([51.25, -85.32],
             popup = 'Ontario').add_to(world_map)

world_map