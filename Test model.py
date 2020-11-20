import xgboost as xgb
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
import seaborn as sns

clf = xgb.Booster({'nthread': 4})
clf.load_model('nfl.model')
qb_stats = pd.read_csv(r'D:\EARTH\NIDA\NFL Project\Project-NFL-BADS6001\Test_data.csv',encoding= 'UTF-8')

#model
x = qb_stats.drop(columns = ['y'])
y = qb_stats['y']
ns_probs = [0 for _ in range(len(y))]
lr_probs = clf.predict(x)
# print(lr_probs)
# ns_auc = roc_auc_score(y, ns_probs)
# lr_auc = roc_auc_score(y, lr_probs)

# #Confusion Metrix
# cfm = confusion_matrix(y, lr_probs)
# fscore = f1_score(y, lr_probs)
# print('F-score = %.3f'% fscore)
# sns.heatmap(cfm, annot=True)
# pyplot.show()

# #plot AUC
# print('No Skill: ROC AUC=%.3f' % (ns_auc))
# print('Xgboost: ROC AUC=%.3f' % (lr_auc))
# ns_fpr, ns_tpr, _ = roc_curve(y, ns_probs)
# lr_fpr, lr_tpr, _ = roc_curve(y, lr_probs)

# pyplot.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
# pyplot.plot(lr_fpr, lr_tpr, marker='.', label='Xgboost')
# pyplot.xlabel('False Positive Rate')
# pyplot.ylabel('True Positive Rate')
# pyplot.legend()
# pyplot.show()