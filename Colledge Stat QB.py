#sort QB Data from Combine 2010 - 2019
import pandas as pd
combine = pd.read_csv(r'D:\EARTH\NIDA\NFL Project\Project-NFL-BADS6001\combine 2000 - 2019.csv',encoding= 'UTF-8')
qb = combine["Pos"].isin(["QB"])
position_QB = combine[qb]
# position_QB.to_csv(r'D:\EARTH\NIDA\NFL Project\Project-NFL-BADS6001\NameQB.csv',index = False)

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

for qb1 in college.keys():
      df1 = college[qb1]
      df1.columns.get_level_values(1)
      g = df1['G'].sum()
      df2 = df1['Year']
      new_df = df1[df2 == 'Career']
      name = qb1[:-1].replace('-', ' ').rstrip()
      new_df.insert(loc = 0, column = 'Player', value = name.capitalize() )
      # new_df.replace


#concad DataFrame QB_college stats
# lst = [college[qb_data] for qb_data in college.keys()]
# college_stats = pd.concat(lst,ignore_index=True)