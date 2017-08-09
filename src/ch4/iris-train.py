from sklearn import svm, metrics
import random, re

# dta read
csv = []
with open('src/ch4/iris.csv', 'r', encoding='utf-8') as fp:
    for line in fp:
        line = line.strip()
        cols = line.split(',')
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n
        csv.append(list(map(fn, cols)))

# remove hearder
del csv[0]

# shuffle
random.shuffle(csv)

# 学習用とテスト用に分割
total_len = len(csv)
train_len = int(total_len * 2 / 3)
train_data = []
train_label = []
test_data = []
test_label = []
for i in range(total_len):
    data = csv[i][0:4]
    label = csv[i][4]
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)

# 学習
clf = svm.SVC()
clf.fit(train_data, train_label)

# 予想

pre = clf.predict(test_data)
ac_score = metrics.accuracy_score(test_label, pre)
print("正答率=", ac_score)