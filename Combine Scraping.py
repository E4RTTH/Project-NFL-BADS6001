import pandas as pd

years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
s = 'https://www.pro-football-reference.com/draft/{}-combine.htm'
table = {}
df_combine = {}

for year in years:
    table['table{}'.format(year)] = pd.read_html(s.format(year))
    df_combine['combine{}'.format(year)] = table['table{}'.format(year)][0]
    print(df_combine['combine{}'.format(year)].shape)