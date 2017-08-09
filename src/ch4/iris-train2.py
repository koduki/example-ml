import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# data read
csv = pd.read_csv('src/ch4/iris.csv')
csv_data = csv[["SepalLength", "SepalWidth", "PetalLength","PetalWidth"]]
csv_label = csv["Name"]


# 学習用とテスト用に分割
train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)

# 学習
clf = svm.SVC()
clf.fit(train_data, train_label)

# 予想
pre = clf.predict(test_data)
ac_score = metrics.accuracy_score(test_label, pre)
print("正答率=", ac_score)