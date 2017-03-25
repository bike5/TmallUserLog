#coding=gbk
from numpy import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score

'''

'''
def splitFileAction():
    fs1 = open('log_click_train.txt','w+')
    fs2 = open('log_buy_train.txt','w+')
    fs3 = open('log_collect_train.txt','w+')
    for line in open(r'/home/bike5/Ali/data/trainData/log_train.csv'):
    #for line in open(r'/home/bike5/Ali/data/testData1/log_test1.csv'):
        line1 = line.strip().split(',')
        if line1[-1]=='0' :
            fs1.write(line)
        if line1[-1]=='2' :
            fs2.write(line)
        if line1[-1]=='3' :
            fs3.write(line)
    fs1.close();fs2.close();fs3.close()

def splitFileTest():
    fs1 = open('log_click_Test.txt','w+')
    fs2 = open('log_buy_Test.txt','w+')
    fs3 = open('log_collect_Test.txt','w+')
    #for line in open(r'/home/bike5/Ali/data/trainData/log_train.csv'):
    for line in open(r'/home/bike5/Ali/data/testData1/log_test1.csv'):
        line1 = line.strip().split(',')
        if line1[-1]=='0' :
            fs1.write(line)
        if line1[-1]=='2' :
            fs2.write(line)
        if line1[-1]=='3' :
            fs3.write(line)
    fs1.close();fs2.close();fs3.close()
def getFeatTest():
    featDictClick = {}; featDictBuy = {}; featDictCollect = {};
    #for line in open(r'/home/bike5/Ali/data/testData1/log_test1.csv'):
    cat = {}
    for line in open('log_click_Test.txt'):
        line = line.strip().split(',')
        if line[0] not in featDictClick:
            cat = {}
            cat[line[2]] = cat.get(line[2],0) + 1
            featDictClick[line[0]] = cat
        else:
            cat[line[2]] = cat.get(line[2],0) + 1
    cat = {}
    for line in open('log_buy_Test.txt'):
        line = line.strip().split(',')
        if line[0] not in featDictBuy:
            cat = {}
            cat[line[2]] = cat.get(line[2],0) + 1
            featDictBuy[line[0]] = cat
        else:
            cat[line[2]] = cat.get(line[2],0) + 1
    cat = {}
    for line in open('log_collect_Test.txt'):
        line = line.strip().split(',')
        if line[0] not in featDictCollect:
            cat = {}
            cat[line[2]] = cat.get(line[2],0) + 1
            featDictCollect[line[0]] = cat
        else:
            cat[line[2]] = cat.get(line[2],0) + 1
    return featDictClick,featDictBuy,featDictCollect

def getFeatDict():
    featDictClick = {}; featDictBuy = {}; featDictCollect = {};
    #for line in open(r'/home/bike5/Ali/data/testData1/log_test1.csv'):
    cat = {}
    for line in open('log_click_train.txt'):
        line = line.strip().split(',')
        if line[0] not in featDictClick:
            cat = {}
            cat[line[2]] = cat.get(line[2],0) + 1
            featDictClick[line[0]] = cat
        else:
            cat[line[2]] = cat.get(line[2],0) + 1
    cat = {}
    for line in open('log_buy_train.txt'):
        line = line.strip().split(',')
        if line[0] not in featDictBuy:
            cat = {}
            cat[line[2]] = cat.get(line[2],0) + 1
            featDictBuy[line[0]] = cat
        else:
            cat[line[2]] = cat.get(line[2],0) + 1
    cat = {}
    for line in open('log_collect.txt'):
        line = line.strip().split(',')
        if line[0] not in featDictCollect:
            cat = {}
            cat[line[2]] = cat.get(line[2],0) + 1
            featDictCollect[line[0]] = cat
        else:
            cat[line[2]] = cat.get(line[2],0) + 1
    return featDictClick,featDictBuy,featDictCollect

def loadUser():
    user = {}
    #for line in open('/home/bike5/Ali/data/trainData/info_train.csv'):
    for line in open('/home/bike5/Ali/data/testData1/info_test1.csv'):
        line = line.strip().split(',')
        user[line[0]] = line[1]
    print "ccc....."
    return user

def staCat():
    cat_id={}
    for line in open(r'/home/bike5/Ali/data/testData1/log_test1.csv'):
    #for line in open(r'/home/bike5/Ali/data/trainData/log_train.csv'):
        line = line.strip().split(',')
        cat_id[line[2]] = cat_id.get(line[2],0)+1
    return cat_id

def getFeat(featDictClick,featDictBuy,featDictCollect,cat_id,user):
    fs = open('every_cat_test.txt','w+')
    fr = open('every_cat_test_label.txt','w+')
    #fs = open('every_cat_train.txt','w+')
    #fr = open('every_cat_train_label.txt','w+')
    for iD in user:

        for i in cat_id:
            if iD in featDictClick:
                a = featDictClick[iD].get(i,0)
            
            else:
                a = 0
            
            if iD in featDictBuy:
                b = featDictBuy[iD].get(i,0)
            else:            
                b = 0
            if iD in featDictCollect:
                c = featDictCollect[iD].get(i,0)
            else:            
                c = 0
            fs.write(str(0.1*a+0.7*b+0.3*c)+' ')
        fs.write('\n')
        fr.write(iD+' '+user[iD]+'\n')
        print 'aaaaa...'
    fs.close()
    fr.close()
    #return feats

def loadCatFeat():
    fs = open('every_cat_train.txt')
    fr = open('every_cat_train_label.txt')
    '''
    data=[]
    for line in fs:
        line = line.strip().split(' ')
        map(float,line)
    data = array(data)
    '''
    labels = [int(line.strip().split(' ')[1])-1 for line in fr]
    labels = array(labels)
    return labels

def loadCatTestFeat():
    fs = open(r'every_cat_test.txt')
    fr = open(r'every_cat_test_label.txt')
    data = [map(float,line.strip().split(' ')) for line in fs]
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








