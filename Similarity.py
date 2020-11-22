#load data
import pandas as pd
import numpy as np
qb_stats = pd.read_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL-BADS6001\Train_data1.csv',encoding= 'UTF-8')
img = pd.read_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL-BADS6001\img.csv',encoding= 'UTF-8')

#Similarity
from scipy.spatial.distance import euclidean,pdist,squareform
user_input = {'userinput from website'}
qb_drafted = qb_stats[qb_stats['y']==1].fillna(0)
similarity = {}

for i in range(0,len(qb_drafted.index)):
    similarity[qb_drafted.iloc[i][0]] = euclidean(user_input,qb_drafted.iloc[i][1:])
                                                  
url_img = img[min(similarity)] 

