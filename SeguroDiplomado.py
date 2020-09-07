import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Temp/SeguroUploadAzure.csv") 

df = pd.DataFrame(data,columns= ['InArea','SavBal', 'Ins'])

X = df[['InArea', 'SavBal']]

y = df['Ins']

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.3, random_state=0)

logistic_regression= LogisticRegression()

logistic_regression.fit(X_train,y_train)

y_pred=logistic_regression.predict(X_test)

confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])

sn.heatmap(confusion_matrix, annot=True, fmt='g')

print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))

plt.show()
