import pandas as pd
import numpy as np

data = pd.read_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL--BADS6001-\Before_train.csv',encoding= 'UTF-8')

#Over Sampling
max_size = data['y'].value_counts().max()
lst = [data]
for class_index, group in data.groupby('y'):
    lst.append(group.sample(max_size-len(group), replace=True))
frame_new = pd.concat(lst)
data = frame_new

data.to_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL--BADS6001-\Train_data.csv',index=False)