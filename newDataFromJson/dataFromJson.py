import json



class DataFromJson():

    def __init__(self,filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.contents = data["content"]
        self.lables = data["labels"]
        self.connections = data["connections"]
        # print("len_contents:")
        # print(len(contents))


    #将json文件中的contents内容分为几句
    def makeContentsList(self):
        #以@ 为分割，分割出几段
        contentsList = self.contents.split('@')
        #去除最后一句规范中的  \n
        contentsList[-1] = contentsList[-1][:-1]
        del contentsList[0]
        for i in range(len(contentsList)):
            content = contentsList[i]
            content = '@'+content
            contentsList[i] = content
        return contentsList
    # contentsList = makeContentsList()
    # print(contentsList)


    #获取每句的  [开始索引，结束索引]
    def getSentencesIndex(self,contentsList):
        indexs = []
        beginIndex = 0
        for i in range(len(contentsList)):
            # print("len_"+str(i))
            # print(len(contentsList[i]))
            index = []
            index.append(beginIndex)
            endIndex = beginIndex + len(contentsList[i])
            index.append(endIndex)
            indexs.append(index)
            #更新下一个句子的初试位置
            beginIndex = endIndex
        return indexs

    # indexs = getSentencesIndex()
    # print(indexs)

    #寻找labels 中 与Id 对应id的单词索引
    def findIndex(self,Id):
        for i in range(len(self.lables)):
            if Id == self.lables[i]['id']:
                return i
            else:
                continue

    #找到每个词在句中的正确坐标
    def findCorrectIndex(self,startIndex,endIndex,indexs):
        for i in range(len(indexs)):
            index = indexs[i]
            indexBegin = index[0]
            indexEnd = index[-1]
            if startIndex>=indexBegin and startIndex <indexEnd:
                startIndex = startIndex - indexBegin
                endIndex = endIndex - indexBegin
                return startIndex,endIndex,i
            else:
                continue

    #make 单词
    def makeWordList(self,Id,indexs):

        Id = self.findIndex(Id)

        #单词的类别号
        labelCategoriesId = str(self.lables[Id]["categoryId"])
        startIndex = self.lables[Id]["startIndex"]
        endIndex = self.lables[Id]["endIndex"]
        #单词
        word = self.contents[startIndex:endIndex]

        #startIndex:起始位置 ，endIndex：终止位置 ， sentenceNum：句子序号（第几句）
        startIndex,endIndex,sentenceNum= self.findCorrectIndex(startIndex, endIndex,indexs)
        word_index_list = []
        word_index = []
        word_index.append(startIndex)
        word_index.append(endIndex-1)
        word_index_list.append(word_index)

        return word,labelCategoriesId,word_index_list,sentenceNum

    #make 每一个关系的例子 如{"t":["你好","Q953465",[[0,1]]],"h":["怎么","Q6016039",[[3,4]]],"tokens":["你","好","了","怎","么","办"]}
    def makeInstanceList(self,fromId,toId,indexs,contentsList):
        instance = {'t':[],'h':[],'tokens':[]}

        #add 't'
        t_word,t_labelCategoriesId,t_word_index_list,sentenceNum=self.makeWordList(fromId,indexs)
        instance["t"].append(t_word)
        instance["t"].append(t_labelCategoriesId)
        instance["t"].append(t_word_index_list)

        #add 'h'
        h_word, h_labelCategoriesId, h_word_index_list,sentenceNum = self.makeWordList(toId,indexs)
        instance["h"].append(h_word)
        instance["h"].append(h_labelCategoriesId)
        instance["h"].append(h_word_index_list)

        #add 'tokens'
        # print('tokens')
        # print(contentsList[sentenceNum])
        content = contentsList[sentenceNum]
        for word in content:
            instance["tokens"].append(word)

        return instance

    #从每个json文件中提取  数据（符合规范）
    def makeNewData(self,indexs,contentsList):
        new_data = {}
        for i in range(len(self.connections)):
            connectionCategoriesId = str(self.connections[i]["categoryId"])
            if connectionCategoriesId not in new_data:
                new_data[connectionCategoriesId] = []
            if connectionCategoriesId in new_data:
                fromId = self.connections[i]["fromId"]
                toId = self.connections[i]["toId"]

                instance = self.makeInstanceList(fromId,toId,indexs,contentsList)
                new_data[connectionCategoriesId].append(instance)
        return new_data
    # new_data = makeNewData()
    # print(len(new_data))


    # 将新输出数据与  output 合并
    def mergeOutDate(self,new_data):
        with open('output/output.json', 'r', encoding='utf-8') as f:
            out_data = json.load(f)
        for connectionId in new_data:
            if connectionId not in out_data:
                out_data[connectionId] = new_data[connectionId]
            else:
                instances = new_data[connectionId]
                for i in range(len(instances)):
                    out_data[connectionId].append(instances[i])
        return out_data
    # out_data = mergeOutDate(new_data)

    #将转换好格式的数据写到 json文件中
    def writeOutData(self,data):
        with open('output/output.json', 'w',encoding='utf-8') as f:
            json.dump(data,f,ensure_ascii=False)

    # writeOutData(out_data)



    #转换文件格式
    def forward(self):
        # 将json文件中的contents内容分为几句
        contentsList = self.makeContentsList()
        # 获取每句的  [开始索引，结束索引]
        indexs = self.getSentencesIndex(contentsList)
        # 从每个json文件中提取  数据（符合规范）
        new_data = self.makeNewData(indexs,contentsList)
        # 将新输出数据与  output 合并
        out_data = self.mergeOutDate(new_data)
        # 将转换好格式的数据写到 json文件中
        self.writeOutData(out_data)
