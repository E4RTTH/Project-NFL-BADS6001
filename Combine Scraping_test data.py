#Combine Scraping Data to CSV
import pandas as pd

url = 'https://www.pro-football-reference.com/draft/2020-combine.htm'
table = pd.read_html(url)
combine = table[0]


#Drop row header and Colledge column
combine.drop(combine[combine['Player'] == 'Player'].index, inplace = True)

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

combine.to_csv(r"D:\EARTH\NIDA\NFL Project\Project-NFL-BADS6001/combine 2020.csv", index = False)
