#sort QB Data from Combine 2010 - 2019
import pandas as pd
combine = pd.read_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL--BADS6001-\combine 2010 - 2019.csv',encoding= 'UTF-8')
qb = combine["Pos"].isin(["QB"])
position_QB = combine[qb]

# Code for scraping colledge data QB
n = [i.lower().replace('.', '').replace("'",'').replace(' ', '-') for i in position_QB.Player] #clean name for web scraping
x = {}
college = {}
cl = 'https://www.sports-reference.com/cfb/players/{}-{}.html'

for i in n:
  for c in range(1,3):
    try:
      x['{}-{}'.format(i,c)] = pd.read_html(cl.format(i,c))
      college['{}-{}'.format(i,c)] = x['{}-{}'.format(i,c)][0]
    except:
      break

keys = list(college.keys())
for a in keys:
  df = college[a]
  position = df['Unnamed: 4_level_0']
  if position['Pos'].iloc[1] != 'QB':
    college.pop(a)

print(college)
print(len(college))