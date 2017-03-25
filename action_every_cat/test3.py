from numpy import *
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

def loadTrainFeat():
    fs1 = open('../user_action_cat/action_buy_num.txt')
    fs2 = open('../user_action_cat/catid_unique.txt')
    fs3 = open('../user_action_cat/action_day_11.txt')
    fs4 = open('../user_action_cat/user.txt')
    fs5 = open('../user_action_cat/action_click_num.txt')
    fs6 = open('../user_action_cat/action_collect_num.txt')

    data = []; everyCat = dict()
    abn = [line.strip().split(',')[1] for line in fs1]; fs1.close()
    abnn = [line.strip().split(',')[1] for line in fs5]; fs5.close()
    abnnn = [line.strip().split(',')[1] for line in fs6]; fs6.close()
    cu = [line.strip().split(',')[1] for line in fs2]; fs2.close()
    ad = [line.strip().split(',')[1] for line in fs3]; fs3.close()
    labels = [int(line.strip().split(',')[1])-1 for line in fs4]; fs4.close()
    fs4 = open('../user_action_cat/user.txt')
    user_id = [line.strip().split(',')[0] for line in fs4]; fs4.close()

    for line in open('../every_cat/every_cat_train.txt'):
        line = line.strip().split(' ')
	everyCat[line[0]] = map(int,line[1:])

    m = len(user_id)
    for i in range(m):
        data.append([int(abn[i]),int(abnn[i]),int(abnnn[i]),int(cu[i]),int(ad[i])])
        data[i].extend(everyCat[user_id[i]])

    return data,labels

def train(data,labels):
    clf = RandomForestClassifier(n_estimators=100)
    data = preprocessing.minmax_scale(data,feature_range=(0,1))
    #clf = svm.SVC(decision_function_shape='ovr')
    clf.fit(data,labels)
    return clf

def loadTestFeat():
    fs1 = open('../user_action_cat/action_buy_num_test.txt')
    fs2 = open('../user_action_cat/catid_unique_test.txt')
    fs3 = open('../user_action_cat/action_day_11_test.txt')
    fs4 = open('../user_action_cat/user_test.txt')
    fs5 = open('../user_action_cat/action_click_num_test.txt')
    fs6 = open('../user_action_cat/action_collect_num_test.txt')
    testData = []; everyCat = dict()
    abn = [line.strip().split(',')[1] for line in fs1]; fs1.close()
    abnn = [line.strip().split(',')[1] for line in fs5]; fs5.close()
    abnnn = [line.strip().split(',')[1] for line in fs6]; fs6.close()
    cu = [line.strip().split(',')[1] for line in fs2]; fs2.close()
    ad = [line.strip().split(',')[1] for line in fs3]; fs3.close()
    user_id = [line.strip().split(',')[0] for line in fs4]; fs4.close()

    for line in open('../every_cat/every_cat_test.txt'):
        line = line.strip().split(' ')
	everyCat[line[0]] = map(int,line[1:])

    m = len(user_id)
    for i in range(m):
        testData.append([int(abn[i]),int(abnn[i]),int(abnnn[i]),int(cu[i]),int(ad[i])])
        testData[i].extend(everyCat[user_id[i]])

    return testData,user_id

def predictResult(clf,testData,user_id):
    testData = preprocessing.minmax_scale(testData,feature_range=(0,1))
    dataArr = clf.predict(testData)
    dataList = list(dataArr)
    data = map(float,dataList)
    fs = open('everyCat_meiyouguiyi.txt','w+')
    m = len(user_id)
    for i in range(m):
        fs.write(user_id[i]+","+str(data[i]+1)+"\n")
    fs.close()














