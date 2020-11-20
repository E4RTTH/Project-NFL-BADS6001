import pandas as pd
import numpy as np

#Load data from combine & college stats
combine_train = pd.read_csv(r'D:\EARTH\NIDA\NFL Project\Project-NFL-BADS6001\NameQB.csv',encoding= 'UTF-8')
college_train = pd.read_csv(r'D:\EARTH\NIDA\NFL Project\Project-NFL-BADS6001\QB_college stats.csv',encoding= 'UTF-8')
combine_test = pd.read_csv(r'D:\EARTH\NIDA\NFL Project\Project-NFL-BADS6001\NameQB(test).csv',encoding= 'UTF-8')
college_test = pd.read_csv(r'D:\EARTH\NIDA\NFL Project\Project-NFL-BADS6001\QB_college stats(test).csv',encoding= 'UTF-8')

#Clean combine data
def clean_df(combine):
       combine.drop(columns = ['Pos','School','College'],inplace = True)
       combine['y'] = combine['Drafted (tm/rnd/yr)'].fillna(0)
       combine['y'] = np.where(combine['y'] == 0,0,1)
       combine.drop(columns = ['Drafted (tm/rnd/yr)'],inplace = True)
       name = [i.lower().replace('.', '').replace("'",'').capitalize() for i in combine.Player]
       combine['Player'] = name

       return combine

#join data
def join_df(combine,college):
       qb_stats = combine.set_index('Player').join(college.set_index('Player'))
       qb_stats = qb_stats[['School','Ht_cm','Wt_kg','40yd','Vertical','Bench','Broad Jump','3Cone','Shuttle','G','Cmp', 'Att', 'Pct', 'Yds', 'Y/A',
              'AY/A', 'TD', 'Int', 'Rate','y']]
       qb_stats.drop(columns = ['School'],inplace = True)

       return qb_stats

#Over Sampling
def overs(data):
       max_size = data['y'].value_counts().max()
       lst = [data]
       for class_index, group in data.groupby('y'):
              lst.append(group.sample(max_size-len(group), replace=True))
       frame_new = pd.concat(lst)
       data = frame_new

       return data

#train data
train = clean_df(combine_train)
train_df = join_df(train,college_train)
final_train = overs(train_df)
final_train.to_csv(r'D:\EARTH\NIDA\NFL Project\Project-NFL-BADS6001\Train_data.csv',index=False)

#test data
test = clean_df(combine_test)
test_df = join_df(test,college_test)
final_test = overs(test_df)
final_test.to_csv(r'D:\EARTH\NIDA\NFL Project\Project-NFL-BADS6001\Test_data.csv',index=False)