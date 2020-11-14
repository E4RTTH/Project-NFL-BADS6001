#sort QB Data from Combine 2010 - 2019
import pandas as pd
combine = pd.read_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL--BADS6001-\combine 2010 - 2019.csv',encoding= 'UTF-8')
qb = combine["Pos"].isin(["QB"])
position_QB = combine[qb]
position_QB.to_csv(r'D:\NIDA\Intro BADS\Project BADS6001\Project-NFL--BADS6001-\NameQB.csv',index=False)