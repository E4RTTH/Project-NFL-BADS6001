#sort QB Data from Combine 2010 - 2019
import pandas as pd
combine = pd.read_csv(r'D:\EARTH\NIDA\NFL Project\Project-NFL-BADS6001\combine 2010 - 2019.csv',encoding= 'UTF-8')
qb = combine["Pos"].isin(["QB"])
position_QB = combine[qb]
# position_QB.to_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL--BADS6001-\NameQB.csv',index=False)

# Code for scraping colledge data QB
n = [i.lower().replace('.', '').replace(' ', '-') for i in position_QB.Player]
x = {}
college = {}
cl = 'https://www.sports-reference.com/cfb/players/{}-1.html'

for i in n:
  for c in range(1,2):
    cl.replace('1',str(c))
    try:
      x['{}'.format(i)] = pd.read_html(cl.format(i))
      college['{}'.format(i)] = x['{}'.format(i)][0]
    except:
      break

# print(college['nick-fitzgerald'])
# print(type(college['nick-fitzgerald']))
# print(college['nick-fitzgerald'].shape)
# print(college['nick-fitzgerald'].columns)