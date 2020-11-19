import pandas as pd
import numpy as np

#Load data from combine & college stats
combine = pd.read_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL--BADS6001-\NameQB.csv',encoding= 'UTF-8')
college = pd.read_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL--BADS6001-\QB_college stats.csv',encoding= 'UTF-8')

#Clean combine data
combine.drop(columns = ['Pos','School','College'],inplace = True)
combine['y'] = combine['Drafted (tm/rnd/yr)'].fillna(0)
combine['y'] = np.where(combine['y'] == 0,0,1)
combine.drop(columns = ['Drafted (tm/rnd/yr)'],inplace = True)
name = [i.lower().replace('.', '').replace("'",'').capitalize() for i in combine.Player]
combine['Player'] = name


#join data
qb_stats = combine.set_index('Player').join(college.set_index('Player'))
qb_stats = qb_stats[['School','Ht_cm','Wt_kg','40yd','Vertical','Bench','Broad Jump','3Cone','Shuttle','G','Cmp', 'Att', 'Pct', 'Yds', 'Y/A',
       'AY/A', 'TD', 'Int', 'Rate','y']]
qb_stats.drop(columns = ['School'],inplace = True)
qb_stats.to_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL--BADS6001-\Before_train.csv',index=False)