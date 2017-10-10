from sklearn import model_selection, svm, metrics
import matplotlib.pyplot as plt
import pandas as pd

tbl = pd.read_csv("bmi.csv")

label = tbl["label"]

# 0..1の範囲に正規化
w = tbl["weight"] / 100 # 100kb
h = tbl["height"] / 200 # 200cm

wh = pd.concat([w, h], axis=1)

data_train, data_test, label_train, label_test = model_selection.train_test_split(wh, label)
 
# 学習
clf = svm.LinearSVC()
clf.fit(data_train, label_train)

# 予測
predict = clf.predict(data_test)

# report
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("正解率=", ac_score)
print("レポート=\n", cl_report)