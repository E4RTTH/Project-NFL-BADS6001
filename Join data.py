import pandas as pd
import numpy as np

#Load data from combine & college stats
combine = pd.read_csv(r'D:\EARTH\NIDA\NFL Project\Project-NFL-BADS6001\NameQB.csv',encoding= 'UTF-8')
college = pd.read_csv(r'D:\EARTH\NIDA\NFL Project\Project-NFL-BADS6001\QB_college stats.csv',encoding= 'UTF-8')
print(np.where(combine['Drafted (tm/rnd/yr)'] is not np.nan))

#Clean combine data
# combine.drop(columns = ['Pos','School','College'],inplace = True)
# combine['y'] = np.where(combine['Drafted (tm/rnd/yr)'] is object,1,0)
# combine.drop(columns = ['Drafted (tm/rnd/yr)'],inplace = True)
# name = [i.lower().replace('.', '').replace("'",'').capitalize() for i in combine.Player]
# combine['Player'] = name
# print(combine)
# print(combine['y'].value_counts())

#join data
# qb_stats = combine.set_index('Player').join(college.set_index('Player'))
# qb_stats = qb_stats[['School','Ht_cm','Wt_kg','40yd','Vertical','Bench','Broad Jump','3Cone','Shuttle','G','Cmp', 'Att', 'Pct', 'Yds', 'Y/A',
#        'AY/A', 'TD', 'Int', 'Rate','y']]