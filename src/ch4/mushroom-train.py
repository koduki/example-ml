from sklearn import model_selection, metrics, ensemble,svm
import pandas as pd

mr = pd.read_csv("mushroom.csv", header=None)
label = []
data = []
attr_list = []

for row_index, row in mr.iterrows():
    label.append(row.ix[0])
    row_data = []
    for v in row.ix[1:]:
        row_data.append(ord(v))
    data.append(row_data)

# 学習用データとテストデータに分類
data_train, data_test, label_train, label_test = model_selection.train_test_split(data, label)

# データの学習
#clf = ensemble.RandomForestClassifier()
clf svm.SVM()
clf.fit(data_train, label_train)

# 予測
predict = clf.predict(data_test)

# 精度確認
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)

print("正解率=", ac_score)
print("レポート\n", cl_report)