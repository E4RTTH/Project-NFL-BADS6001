import xgboost as xgb
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot

clf = xgb.Booster({'nthread': 4})
clf.load_model('nfl.model')
qb_stats = pd.read_csv(r'D:\EARTH\NIDA\NFL Project\Project-NFL-BADS6001\Test_data.csv',encoding= 'UTF-8')


x = qb_stats.drop(columns = ['y'])
y = qb_stats['y']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=22)
ns_probs = [0 for _ in range(len(y_test))]
clf = xgb.XGBClassifier(missing=np.nan,n_estimators=1000, learning_rate=0.1,)
clf.fit(X_train, y_train)

lr_probs = clf.predict(X_test)
ns_auc = roc_auc_score(y_test, ns_probs)
lr_auc = roc_auc_score(y_test, lr_probs)

print('No Skill: ROC AUC=%.3f' % (ns_auc))
print('Xgboost: ROC AUC=%.3f' % (lr_auc))

ns_fpr, ns_tpr, _ = roc_curve(y_test, ns_probs)
lr_fpr, lr_tpr, _ = roc_curve(y_test, lr_probs)

pyplot.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
pyplot.plot(lr_fpr, lr_tpr, marker='.', label='Xgboost')


pyplot.xlabel('False Positive Rate')
pyplot.ylabel('True Positive Rate')


pyplot.legend()


pyplot.show()