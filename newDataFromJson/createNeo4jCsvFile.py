import json
import csv
with open('output/output.json', 'r', encoding='utf-8') as f:
    # 将 JSON 对象转换为 Python 字典
    data = json.load(f)


# entitys： key:唯一标识符，value:实体名称
entitys = {}

#创建实体表
def createEntity():
    i = 0
    # 对 data 按key 进行排序 sorted(entitys)
    for key in sorted(data):
        # 遍历每类关系下的 所有示例
        # item 代表 关系类别key 下所有的样例
        item = data.get(key)
        for index in range(len(item)):
            #遍历 当前 关系类别key 下的 第i个样本，将其添加至集合中
            hEntity = item[index]['h'][0]
            tEntity = item[index]['t'][0]
            if hEntity not in entitys.values():
                entitys[i]=hEntity
                i +=1
            if tEntity not in entitys.values():
                entitys[i]=tEntity
                i +=1
    # entity.csv 实体表
    with open('neo4jFile/entity.csv', 'w', encoding='utf-8',newline='') as f:
        # 实体表
        entityCsv = csv.writer(f)
        # 实体表的两个字段名，eid：唯一标识符，ename:实体名
        entityCsv.writerow(['eid', 'ename'])
        # 对 entitys 按key 进行排序 sorted(entitys)
        for key in sorted(entitys):
            entityCsv.writerow([key,entitys[key]])

# createEntity()


#实体类型表： key: id  value:实体类型 例：# entityType = {0:"建筑",1:"空间",2:"物理施工元素"}
entityType = {}
with open('data/姚_标记数据/103_1013_tagged.json', 'r', encoding='utf-8') as f:
    # 将 JSON 对象转换为 Python 字典
    fixdata = json.load(f)
    for i in range(len(fixdata["labelCategories"])):
        entityType[fixdata["labelCategories"][i]["id"]] = fixdata["labelCategories"][i]["text"]

#创建实体类型表
def createEntityType():
    # entity.csv 实体表
    with open('neo4jFile/entityType.csv', 'w', encoding='utf-8',newline='') as f:
        # 实体表
        entityTypeCsv = csv.writer(f)
        # 实体表的两个字段名，eid：唯一标识符，ename:实体名
        entityTypeCsv.writerow(['etid', 'etname'])
        # 对 entitys 按key 进行排序 sorted(entitys)
        for key in sorted(entityType):
            entityTypeCsv.writerow([key,entityType[key]])

# createEntityType()


#关系is 实体-类型表
def createEntityRType():

    # entityRType.csv 实体表  实体表的两个字段名，eid：唯一标识符，ename:实体名
    with open('neo4jFile/entityRType.csv', 'w', encoding='utf-8', newline='') as f:
        # 实体表
        entityRTypeCsv = csv.writer(f)
        # 实体表的两个字段名，eid：唯一标识符，ename:实体名
        entityRTypeCsv.writerow(['ename', 'etname'])

        # 对 data 按key 进行排序 sorted(entitys)
        for key in sorted(data):
            # 遍历每类关系下的 所有示例
            # item 代表 关系类别key 下所有的样例
            item = data.get(key)
            for index in range(len(item)):
                # 遍历 当前 关系类别key 下的 第i个样本，将其添加至集合中
                hename = item[index]['h'][0]
                hEtype = item[index]['h'][1]
                hetname = entityType.get(int(hEtype))

                tename = item[index]['t'][0]
                tEType = item[index]['t'][1]
                tetname = entityType.get(int(tEType))
                #ename:实体名   etname:实体类型
                entityRTypeCsv.writerow([hename,hetname])
                entityRTypeCsv.writerow([tename,tetname])

# createEntityRType()




#实体类型表： key: id  value:实体类型 例：# entityType = {0:"建筑",1:"空间",2:"物理施工元素"}
relationType = {}
with open('data/姚_标记数据/103_1013_tagged.json', 'r', encoding='utf-8') as f:
    # 将 JSON 对象转换为 Python 字典
    fixdata = json.load(f)
    for i in range(len(fixdata["connectionCategories"])):
        relationType[fixdata["connectionCategories"][i]["id"]] = fixdata["connectionCategories"][i]["text"]

#关系表
def createRelationCsv():
    # 对 data 按key 进行排序 sorted(entitys)
    for key in sorted(data):
        relationName = relationType.get(int(key))
        csvFile = 'neo4jFile/'+relationName+'.csv'
        # 关系表
        with open(csvFile, 'w', encoding='utf-8', newline='') as f:
            # 实体表
            relationCsv = csv.writer(f)
            # 实体表的两个字段名，eid：唯一标识符，ename:实体名
            relationCsv.writerow(['ename1', 'ename2'])
            # 遍历每类关系下的 所有示例
            # item 代表 关系类别key 下所有的样例
            item = data.get(key)
            for index in range(len(item)):
                # 遍历 当前 关系类别key 下的 第i个样本，将其添加至集合中
                hename = item[index]['h'][0]
                tename = item[index]['t'][0]
                relationCsv.writerow([hename,tename])

# createRelationCsv()