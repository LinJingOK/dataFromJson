import os
import re
import json
import random

# from dataFromJson import DataFromJson

#创建图谱输入五元组
def create_5_gram_tuples(data):
    arr = []
    arrAll = []
    # data是个字典  键为关系类型，值为标记数据
    for key in data:
        # print("key", key)

        # print(data[key][1])
        # 遍历data 得到关系对应的值item
        for item in data[key]:
            dict = {}
            # print(item)
            # item是一个字典，三个键  值为数组   t：[实体，实体类型，实体位置]   tokens: [句子的每个字符]  h：[实体，实体类型，实体位置]
            for tag in item:
                if (tag == 'tokens'):
                    pass
                else :
                    if (tag == 't'):
                        e1 = item[tag][0]
                        ec1 = item[tag][1]
                        dict['f_node_name'] = e1
                        dict['f_node_label'] = ec1
                        dict['relation_name'] = key
                    if (tag == 'h'):
                        e2 = item[tag][0]
                        ec2 = item[tag][1]
                        dict['l_node_name'] = e2
                        dict['l_node_label'] = ec2

                    arr.append(dict)

    arrAll.append(arr)
    return arrAll

#将五元组中的类别id换成文字
def replaceLabel(line):
    # print(line)
    id2name = {'0': '建筑', '1': '空间', '2': '物理施工元素', '3': '抽象施工元素', '4': '文件工作成果', '5': '物理工作成果', '6': '进程工作成果',
               '7': '行为(机器行为、人类行为)', '8': '专有名词',
               '9': '组织角色', '10': '工具', '11': '材质', '12': '属性名', '13': '效用(充当形容词)', '14': '空间位置', '15': '环境条件',
               '16': '属性值', '17': '文件名', }
    id2relation = {'0': '集合(X,Y)', '1': '修饰限定(X,Y)', '2': '领属(X,Y)', '3': '设置(X,Y)', '4': '满足(X,Y)', '5': '为(X,Y)', '6': '利用(X,Y)',
               '7': '具有(X,Y)', '8': '数值限定(X,Y)','9': '位置(X,Y)', '10': '11.实体-起源Entity-Origin(X,Y)', '11': '12.实体-目的地Entity-Destination(X,Y)', '12': '其他(X,Y)', '13': '实体条件(X,Y)'}
    for key in line:
        # print(key)
        if (key == 'f_node_name' or key == 'l_node_name'):
            pass
        elif(key == 'f_node_label'):
            for label in id2name:
                if (line[key] == label):
                    line[key] = id2name[label]
        elif (key == 'relation_name'):
            for label in id2relation:
                if (line[key] == label):
                    line[key] = id2relation[label]
        elif (key == 'l_node_label'):
            for label in id2name:
                if (line[key] == label):
                    line[key] = id2name[label]
        else:
            pass
        # print(key)
    # line.replace("'f_node_label': '3' "," 'f_node_label': '888888888' ")
    return line


with open('../data/output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
arrAll = create_5_gram_tuples(data)

output = open('../output/dataAll.txt', 'w', encoding='utf-8')

count = 0
#一个关系的所有五元组
for lines in arrAll:
    #一个关系的所有五元组中的一条五元组
    for line in lines:
        count += 1
        line = replaceLabel(line)
        output.write(str(line) + '\n')
print(count)




