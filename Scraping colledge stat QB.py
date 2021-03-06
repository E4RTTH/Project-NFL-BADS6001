#sort QB Data from Combine 2010 - 2019
import pandas as pd
import numpy as np
combine = pd.read_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL-BADS6001\combine 2000 - 2019.csv',encoding= 'UTF-8')
combine2020 = pd.read_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL-BADS6001\combine 2020.csv',encoding= 'UTF-8')

# Code for scraping colledge data QB
def scrap_college(combine):
  qb = combine["Pos"].isin(["QB"])
  position_QB = combine[qb]
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

  keys = list(college.keys())
  for z in keys:
    if len(college[z].columns) == 15:
      college[z].columns = ['Year','School','Conf','Class','Pos','G','Cmp','Att','Pct','Yds','Y/A','AY/A','TD','Int','Rate'] 
    else:
      college.pop(z)

  for qb1 in college.keys():
    df1 = college[qb1]
    g = df1['G'].sum()
    df2 = df1['Year']
    new_df = df1[df2 == 'Career']
    name = qb1[:-1].replace('-', ' ').rstrip()
    new_df.insert(loc = 0, column = 'Player', value = name.capitalize() )
    new_df.replace({'G':np.nan},g,inplace = True)
    college[qb1] = new_df

  return college

# concad DataFrame QB_college stats
def concat(college):
  lst = [college[qb_data] for qb_data in college.keys()]
  college_stats = pd.concat(lst,ignore_index=True)
  college_stats.drop(columns = ['Year','Conf','Class','Pos'], inplace = True)

  return college_stats


#train data
train = scrap_college(combine)
train_df = concat(train)
train_df.to_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL-BADS6001\QB_college stats.csv', index = False)
qb1 = combine["Pos"].isin(["QB"])
position_QB1 = combine[qb1]
position_QB1.to_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL-BADS6001\NameQB.csv', index = False)

#test data
test = scrap_college(combine2020)
test_df = concat(test)
test_df.to_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL-BADS6001\QB_college stats(test).csv', index = False)
qb2 = combine2020["Pos"].isin(["QB"])
position_QB2 = combine2020[qb2]
position_QB2.to_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL-BADS6001\NameQB(test).csv', index = False)