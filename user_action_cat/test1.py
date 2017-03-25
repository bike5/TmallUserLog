#coding=utf-8
from numpy import array
from sklearn import svm
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier

def loadTrainData():
    trainData = []; 
    #infoReader = open('/home/bike5/Ali/data/trainData/info_train.csv')
    #logReader = open('/home/bike5/Ali/data/trainData/log_train.csv')
    for line in open('/home/bike5/Ali/data/trainData/log_train.csv'):
        line = line.strip().split(',')
        trainData.append(line)
    print "bbb....."
    return trainData

'''
def ll(trainData):
    buy = 0; collect = 0; click = 0
    for line in trainData:
        if line[-1]=='0':
            click += 1
        if line[-1]=='2':
            buy += 1
        if line[-1]=='3':
            collect += 1
    return click,buy,collect
'''

def loadTrainUser():
    user = {}
    for line in open('/home/bike5/Ali/data/trainData/info_train.csv'):
        line = line.strip().split(',')
        user[line[0]] = line[1]
    print "aaa....."
    return user 

def loadTestData():

    TestData = []
    for line in open('/home/bike5/Ali/data/testData1/log_test1.csv'):
        line = line.strip().split(',')
        TestData.append(line)
    print "ddd....."
    return TestData

def loadTestUser():
    user = {}
    for line in open('/home/bike5/Ali/data/testData1/info_test1.csv'):
        line = line.strip().split(',')
        user[line[0]] = line[1]
    print "ccc....."
    return user

def getTrainFeat(dataSet,user):
    fs1 = open('action_buy_num.txt','w+')
    fs2 = open('catid_unique.txt','w+')
    fs3 = open('action_day_11.txt','w+')
    fs4 = open('user.txt','w+')
    fs5 = open('action_click_num.txt','w+')
    fs6 = open('action_collect_num.txt','w+')
    user_id = 0
    action_buy_num=0; action_click_num=0; action_collect_num=0; catid_unique=0; action_day_11=0;cat_id_set = set()
    for line in dataSet:
        if user_id != line[0]:
            if user_id in user:
                fs1.write(user_id+','+str(action_buy_num)+'\n')
                fs2.write(user_id+','+str(catid_unique)+'\n')
                fs3.write(user_id+','+str(action_day_11)+'\n')
                fs4.write(user_id+','+user[str(user_id)]+'\n')
                fs5.write(user_id+','+str(action_click_num)+'\n')
                fs6.write(user_id+','+str(action_collect_num)+'\n')
            action_buy_num=0; action_click_num=0; action_collect_num=0; catid_unique=0; action_day_11=0;cat_id_set = set()
            user_id = line[0]
        if line[-1]=='0':
            action_click_num += 1
        if line[-1]=='2':
            action_buy_num += 1
        if line[-1]=='3':
            action_collect_num += 1
        if line[-2]=='185':
            action_day_11 += 1
        cat_id_set.add(line[2])
        catid_unique = len(cat_id_set)
    if str(user_id) in user:
        fs1.write(user_id+','+str(action_buy_num)+'\n')
        fs2.write(user_id+','+str(catid_unique)+'\n')
        fs3.write(user_id+','+str(action_day_11))
        fs4.write(user_id+','+user[str(user_id)])
        fs5.write(user_id+','+str(action_click_num)+'\n')
        fs6.write(user_id+','+str(action_collect_num)+'\n')
    fs1.close()
    fs2.close()
    fs3.close()
    fs4.close()
    fs5.close()
    fs6.close()



def getTestFeat(dataSet,user):
    fs1 = open('action_buy_num_test.txt','w+')
    fs2 = open('catid_unique_test.txt','w+')
    fs3 = open('action_day_11_test.txt','w+')
    fs4 = open('user_test.txt','w+')
    fs5 = open('action_click_num_test.txt','w+')
    fs6 = open('action_collect_num_test.txt','w+')
    user_id = 0
    action_buy_num=0; action_click_num=0; action_collect_num=0; catid_unique=0; action_day_11=0;cat_id_set = set()
    for line in dataSet:
        if user_id != line[0]:
            if user_id in user:
                fs1.write(user_id+','+str(action_buy_num)+'\n')
                fs2.write(user_id+','+str(catid_unique)+'\n')
                fs3.write(user_id+','+str(action_day_11)+'\n')
                fs4.write(user_id+','+user[str(user_id)]+'\n')
                fs5.write(user_id+','+str(action_click_num)+'\n')
                fs6.write(user_id+','+str(action_collect_num)+'\n')
            action_buy_num=0; action_click_num=0; action_collect_num=0; catid_unique=0; action_day_11=0;cat_id_set = set()
            user_id = line[0]
        if line[-1]=='0':
            action_click_num += 1
        if line[-1]=='2':
            action_buy_num += 1
        if line[-1]=='3':
            action_collect_num += 1
        if line[-2]=='185':
            action_day_11 += 1
        cat_id_set.add(line[2])
        catid_unique = len(cat_id_set)
    if str(user_id) in user:
        fs1.write(user_id+','+str(action_buy_num)+'\n')
        fs2.write(user_id+','+str(catid_unique)+'\n')
        fs3.write(user_id+','+str(action_day_11))
        fs4.write(user_id+','+user[str(user_id)])
        fs5.write(user_id+','+str(action_click_num)+'\n')
        fs6.write(user_id+','+str(action_collect_num)+'\n')
    fs1.close()
    fs2.close()
    fs3.close()
    fs4.close()
    fs5.close()
    fs6.close()



def loadTrainFeat():
    fs1 = open('action_buy_num.txt')
    fs2 = open('catid_unique.txt')
    fs3 = open('action_day_11.txt')
    fs4 = open('user.txt')
    fs5 = open('action_click_num.txt')
    fs6 = open('action_collect_num.txt')
    data = []
    abn = [line.strip().split(',')[1] for line in fs1]
    abnn = [line.strip().split(',')[1] for line in fs5]
    abnnn = [line.strip().split(',')[1] for line in fs6]
    cu = [line.strip().split(',')[1] for line in fs2]
    ad = [line.strip().split(',')[1] for line in fs3]
    labels = [int(line.strip().split(',')[1])-1 for line in fs4]
    fs1.close()
    fs2.close()
    fs3.close()
    fs4.close()
    fs5.close()
    fs6.close()
    m = len(abn)
    for i in range(m):
        data.append([int(abn[i]),int(abnn[i]),int(abnnn[i]),int(cu[i]),int(ad[i])])
    return data,labels

def train(data,labels):
    clf = RandomForestClassifier(n_estimators=100)
    #clf = svm.SVC(decision_function_shape='ovr')
    #data = preprocessing.minmax_scale(data,feature_range=(0,1))
    clf.fit(data,labels)
    return clf

def loadTestFeat():
    fs1 = open('action_buy_num_test.txt')
    fs2 = open('catid_unique_test.txt')
    fs3 = open('action_day_11_test.txt')
    fs4 = open('user_test.txt')
    fs5 = open('action_click_num_test.txt')
    fs6 = open('action_collect_num_test.txt')
    testData = []
    abn = [line.strip().split(',')[1] for line in fs1]
    abnn = [line.strip().split(',')[1] for line in fs5]
    abnnn = [line.strip().split(',')[1] for line in fs6]
    cu = [line.strip().split(',')[1] for line in fs2]
    ad = [line.strip().split(',')[1] for line in fs3]
    user_id = [line.strip().split(',')[0] for line in fs4]
    fs1.close()
    fs2.close()
    fs3.close()
    fs4.close()
    fs5.close()
    fs6.close()
    m = len(abn)
    for i in range(m):
        testData.append([int(abn[i]),int(abnn[i]),int(abnnn[i]),int(cu[i]),int(ad[i])])
    return testData,user_id


def predictResult(clf,testData,user_id):
    #testData = preprocessing.minmax_scale(testData,feature_range=(0,1))
    dataArr = clf.predict(testData)
    dataList = list(dataArr)
    data = map(float,dataList)
    fs = open('result_action_day_cat_meiyouguiyihua.txt','w+')
    m = len(user_id)
    for i in range(m):
        fs.write(user_id[i]+","+str(data[i]+1)+"\n")
    fs.close()
        
    







    
                
