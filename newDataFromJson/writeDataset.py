import json
import random
with open('output/output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


def takeSecond(elem):
    return elem[1]

#(关系类别，该关系内包含的 例子数) ，按样例数量 降序排列
#关系数量统计 [('2', 1044), ('4', 672), ('1', 580), ('11', 318), ('3', 267), ('0', 240), ('6', 236), ('10', 181), ('8', 169), ('13', 165), ('7', 147), ('9', 121), ('5', 57), ('12', 18)]
idAndLens = []
for i in data:
    idAndLen = (i,len(data[i]))
    idAndLens.append(idAndLen)
idAndLens.sort(key=takeSecond,reverse=True)
print(idAndLens)



# train_wiki.json
def writeData(filename,data):
    with open('output/'+filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def data_split(full_list, shuffle=True):
    """
    数据集拆分: 将列表full_list按比例6:2:2（随机）划分为3个子列表sublist_1(训练集)与sublist_2（验证集）与sublist_3（测试集）
    :param full_list: 数据列表
    :param ratio:     划分的比例
    :param shuffle:   是否进行将序列的所有元素随机排序。
    :return:
    """
    n_total = len(full_list)
    #int() 对于小数向下取整
    offset1 = int(n_total * 0.6)
    offset2 = int(n_total * 0.2)+offset1;
    if n_total == 0 or offset1 < 1 or offset2<1:
        #列表中包含样本的数量不足1
        return full_list,[],[]
    if shuffle:
        random.shuffle(full_list)
    sublist_1 = full_list[:offset1]
    sublist_2 = full_list[offset1:offset2]
    sublist_3 = full_list[offset2:]
    return sublist_1, sublist_2, sublist_3

#（共14类关系）  每类中随机抽取60%作为训练集，20%作为验证集，20%作为测试集

trainData = {}
valData = {}
testData = {}

for idAndLen in idAndLens:
    # connectionId 类的类别号
    connectionId = str(idAndLen[0])
    #调用函数data_split 实现按比例6:2:2（随机）划分为3个子列表，trainList,valList,testList
    trainList,valList,testList=data_split(data[connectionId])

    if connectionId not in trainData:
        trainData[connectionId] = trainList
    else:
        trainData[connectionId] += trainList

    if connectionId not in valData:
        valData[connectionId] = valList
    else:
        valData[connectionId] += valList

    if connectionId not in testData:
        testData[connectionId] = testList
    else:
        testData[connectionId] += testList



writeData(filename='train_wiki.json',data=trainData)
writeData(filename='val_wiki.json',data=valData)
writeData(filename='test_wiki.json',data=testData)

# i=0
# for idAndLen in idAndLens:
#     connectionId = str(idAndLen[0])
#     if i>=7 and i < 10:
#         if connectionId not in trainData:
#             trainData[connectionId]=data[connectionId]
#             i+=1
#     elif i>=10 and i <12:
#         if connectionId not in valData:
#             valData[connectionId]=data[connectionId]
#             i+=1
#     elif i>=12 and i <14:
#         if connectionId not in valData:
#             testData[connectionId]=data[connectionId]
#             i+=1
#     else:
#         i = i+1
#
#
# writeData(filename='train_wiki_small.json',data=trainData)
# writeData(filename='val_wiki_small.json',data=valData)
# writeData(filename='test_wiki_small.json',data=testData)

# 测试
# def testDataId(data):
#     for Id in data:
#         print(Id)
# testDataId(trainData)
# testDataId(valData)
# testDataId(testData)
# print(len(trainData))
# print(len(valData))
# print(len(testData))
