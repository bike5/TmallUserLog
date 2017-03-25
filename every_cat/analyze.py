#coding=gbk

def staUser():
    user_id = {}
    for line in open(r'F:\学习\机器学习\Ali杯\数据\训练数据\log_train.csv'):
        line = line.strip().split(',')
        user_id[line[0]] = user_id.get(line[0],0) + 1
    return user_id

def staItem():
    item_id={}
    for line in open(r'F:\学习\机器学习\Ali杯\数据\训练数据\log_train.csv'):
        line = line.strip().split(',')
        item_id[line[1]] = item_id.get(line[1],0) + 1
    return item_id

def staCat():
    cat_id={}
    #for line in open(r'/home/bike5/Ali/data/testData1/log_test1.csv'):
    for line in open(r'/home/bike5/Ali/data/trainData/log_train.csv'):
        line = line.strip().split(',')
        cat_id[line[2]] = cat_id.get(line[2],0) + 1
    return cat_id

def staSeller():
    seller_id={}
    for line in open(r'F:\学习\机器学习\Ali杯\数据\训练数据\log_train.csv'):
        line = line.strip().split(',')
        seller_id[line[3]] = seller_id.get(line[3],0) + 1
    return seller_id

def staBrand():
    brand_id={}
    for line in open(r'F:\学习\机器学习\Ali杯\数据\训练数据\log_train.csv'):
        line = line.strip().split(',')
        brand_id[line[4]] = brand_id.get(line[4],0) + 1
    return brand_id

def staTime():
    time_stamp={}
    for line in open(r'F:\学习\机器学习\Ali杯\数据\训练数据\log_train.csv'):
        line = line.strip().split(',')
        time_stamp[line[5]] = time_stamp.get(line[5],0) + 1
    return time_stamp

def staAct():
    action_type={}
    for line in open(r'F:\学习\机器学习\Ali杯\数据\训练数据\log_train.csv'):
        line = line.strip().split(',')
        action_type[line[6]] = action_type.get(line[6],0) + 1
    return action_type

