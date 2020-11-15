#Combine Scraping Data to CSV
import pandas as pd

years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
s = 'https://www.pro-football-reference.com/draft/{}-combine.htm'
table = {}
df_combine = {}

for year in years:
    table['table{}'.format(year)] = pd.read_html(s.format(year))
    df_combine['combine{}'.format(year)] = table['table{}'.format(year)][0]

lst = [df_combine['combine{}'.format(year)] for year in years]
combine = pd.concat(lst,ignore_index=True,)

#Drop row header and Colledge column
combine.drop(combine[combine['Player'] == 'Player'].index, inplace = True)
#combine.drop('College', axis=1, inplace = True)

#Change Ht from foot-inche to cm.
height_cm = []
for k in combine['Ht']:
    a = k.split('-')
    height_cm.append((int(a[0])*30)+(int(a[1])*2.5))

combine.insert(loc=3, column='Ht_cm', value=height_cm)
combine.drop(columns = 'Ht', inplace = True)

#Change Wt from Ib to Kg.
weight_kg = []
for b in combine['Wt']:
    weight_kg.append(int(b)*0.45)

combine.insert(loc=4, column='Wt_kg', value=weight_kg)
combine.drop(columns = 'Wt', inplace = True)

combine.to_csv("d:/NIDA/Intro BADS/Project BADS6001/Project-NFL--BADS6001-/combine 2010 - 2019.csv", index = False)