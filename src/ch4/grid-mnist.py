import pandas as pd
from sklearn import svm, metrics
from sklearn.grid_search import GridSearchCV

def load_csv(fname):
    labels = []
    images = []
    with open(fname, "r") as f:
        for line in f:
            cols = line.split(",")
            if len(cols) < 2: continue
            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)
    return {"labels":labels, "images":images}

# 読込み
train_csv = pd.read_csv("./mnist/train.csv")
test_csv = pd.read_csv("./mnist/t10k.csv")

train_label = train_csv.ix[:, 0]
train_data = train_csv.ix[:, 1:577]
test_label = test_csv.ix[:, 0]
test_data = test_csv.ix[:, 1:577]
print("学習データ数=", len(train_label))

# グリッドサーチのパラメータを指定
params = [
    {"C": [1,10,100,1000], "kernel":["linear"]},
    {"C": [1,10,100,1000], "kernel":["rbf"], "gamma":[0.001, 0.0001]}
]

# 学習
clf = GridSearchCV(svm.SVC(), params, n_jobs=1)
clf.fit(train_data, train_label)

# 予測
predict = clf.predict(test["images"])

# 結果があってるか確認
ac_score = metrics.accuracy_score(test["labels"], predict)
print("正解率=", ac_score)
