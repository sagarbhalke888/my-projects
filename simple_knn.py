from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
import pandas as pd

data=pd.read_csv('loands.csv')

data['LoanAmount'].fillna(data['LoanAmount'].mean(),inplace=True)
data['Credit_History'].fillna(data['Credit_History'].mean(),inplace=True)

x=data.iloc[:,[8,10]].values
y=data['Loan_Status']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

classifier=KNeighborsClassifier(n_neighbors=3)

classifier.fit(x_train,y_train)
pred= classifier.predict(x_test)

print(metrics.accuracy_score(y_test,pred))
