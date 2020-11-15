#sort QB Data from Combine 2010 - 2019
import pandas as pd
combine = pd.read_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL--BADS6001-\combine 2010 - 2019.csv',encoding= 'UTF-8')
qb = combine["Pos"].isin(["QB"])
position_QB = combine[qb]
position_QB.to_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL--BADS6001-\NameQB.csv',index=False)

n = []

for i in position_QB.Player:
  n.append(i.lower().replace('.', '').replace(' ', '-'))
x = {}
college = {}

cl = 'https://www.sports-reference.com/cfb/players/{}-1.html'

for c in range(20):
  cl.replace('1',str(c))
  for i in n:
    try:
      x['{}'.format(i)] = pd.read_html(cl.format(i))
      college['{}'.format(i)] = x['{}'.format(i)][0]
    except:
      pass