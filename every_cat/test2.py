#coding=gbk
from numpy import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score

'''
huo qu mei ge yong hu gou mai de mei zhong shang pin de zhong lei shu.
'''

def getFeatDict():
    featDict = {};
    #for line in open(r'/home/bike5/Ali/data/testData1/log_test1.csv'):
    for line in open(r'/home/bike5/Ali/data/trainData/log_train.csv'):
        line = line.strip().split(',')
        if line[0] not in featDict:
            cat = {}
            cat[line[2]] = cat.get(line[2],0)+1
            featDict[line[0]] = cat
        else:
            cat[line[2]] = cat.get(line[2],0)+1
    return featDict

def staCat():
    cat_id={}
    #for line in open(r'/home/bike5/Ali/data/testData1/log_test1.csv'):
    for line in open(r'/home/bike5/Ali/data/trainData/log_train.csv'):
        line = line.strip().split(',')
        cat_id[line[2]] = cat_id.get(line[2],0) + 1
    return cat_id

def loadTestUser():
    user = {}
    for line in open('/home/bike5/Ali/data/trainData/info_train.csv'):
    #for line in open('/home/bike5/Ali/data/testData1/info_test1.csv'):
        line = line.strip().split(',')
        user[line[0]] = line[1]
    print "ccc....."
    return user

def getFeat(featDict,cat_id,user):
    #fs = open('every_cat_test.txt','w+')
    #fr = open('every_cat_test_label.txt','w+')
    fs = open('every_cat_train.txt','w+')
    fr = open('every_cat_train_label.txt','w+')
    for iD in featDict:
        if iD in user:
            fs.write(iD+' ')
            for i in cat_id:
                fs.write(str(featDict[iD].get(i,0))+' ')
            fs.write('\n')
            fr.write(iD+' '+user[iD]+'\n')
            print "dddd.."
    fs.close()
    fr.close()
    #return feats

def loadCatFeat():
    fs = open('every_cat_train.txt')
    fr = open('every_cat_train_label.txt')
    data = [map(int,line.strip().split(' ')[1:]) for line in fs]
    data = array(data)
    labels = [int(line.strip().split(' ')[1])-1 for line in fr]
    labels = array(labels)
    return data,labels

def loadCatTestFeat():
    fs = open(r'every_cat_test.txt')
    fr = open(r'every_cat_test_label.txt')
    data = [map(int,line.strip().split(' ')[1:]) for line in fs]
    data = array(data)
    user_id = [line.strip().split(' ')[0] for line in fr]
    return data,user_id

def train(data,labels):
    clf = RandomForestClassifier(n_estimators=100)
    #clf = svm.SVC(decision_function_shape='ovr')
    clf.fit(data,labels)
    return clf

def predictResult(clf,testData,user_id):
    #testData = preprocessing.minmax_scale(testData,feature_range=(0,1))
    dataArr = clf.predict(testData)
    dataList = list(dataArr)
    data = map(float,dataList)
    fs = open('test_meiyouguiyi.txt','w+')
    m = len(user_id)
    for i in range(m):
        fs.write(user_id[i]+","+str(data[i]+1)+"\n")
    fs.close()

def cross(data,labels):
    k_range = [10,30,50,70,90,110,130]
    k_scores = []
    for k in k_range:
        clf = RandomForestClassifier(n_estimators=k)
        scores = cross_val_score(clf,data,labels,cv=5,scoring='accuracy')
        k_scores.append(scores.mean())
    return k_scores








