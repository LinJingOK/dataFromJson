
id2name = {'0': '建筑', '1': '空间', '2': '物理施工元素', '3': '抽象施工元素', '4': '文件工作成果', '5': '物理工作成果', '6': '进程工作成果',
           '7': '行为(机器行为、人类行为)', '8': '专有名词',
           '9': '组织角色', '10': '工具', '11': '材质', '12': '属性名', '13': '效用(充当形容词)', '14': '空间位置', '15': '环境条件',
           '16': '属性值', '17': '文件名', }

inputfile = open('../../neo4jFile/entityRType.csv','r', encoding='utf-8')
f = inputfile.readlines()
outputfile = open('../output/entitySum.txt', 'w', encoding='utf-8')

count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for line in f:
    line = line.strip("\n")
    item = line.split(',', 1)[1]
    # print(item)
    if (item == '建筑') :
        count[0] += 1
    elif(item == '空间'):
        count[1] +=1
    elif (item == '物理施工元素'):
        count[2] += 1
    elif (item == '抽象施工元素'):
        count[3] += 1
    elif (item == '文件工作成果'):
        count[4] += 1
    elif (item == '物理工作成果'):
        count[5] += 1
    elif (item == '进程工作成果'):
        count[6] += 1
    elif (item == '行为(机器行为、人类行为)'):
        count[7] += 1
    elif (item == '专有名词'):
        count[8] += 1
    elif (item == '组织角色'):
        count[9] += 1
    elif (item == '工具'):
        count[10] += 1
    elif (item == '材质'):
        count[11] += 1
    elif (item == '属性名'):
        count[12] += 1
    elif (item == '效用(充当形容词)'):
        count[13] += 1
    elif (item == '空间位置'):
        count[14] += 1
    elif (item == '环境条件'):
        count[15] += 1
    elif (item == '属性值'):
        count[16] += 1
    elif (item == '文件名'):
        count[17] += 1
    else:
        print("其他")
print(count)
outputfile.write(str(count))
