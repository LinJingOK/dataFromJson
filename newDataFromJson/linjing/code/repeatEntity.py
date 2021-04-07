from collections import OrderedDict


#3.取出所有实体，挑出重复的实体
def getEntity(lines):

    for line in lines:
        line = line.strip('\n')
        line1 = line.split(',',4)
        entity1 = line1[0].split(':')[1].replace("'","")
        label1 = line1[1].split(':')[1].replace("'","")
        arr = {}
        arr[entity1] = label1
        f2.write(str(arr) + '\n')

        line2 = line.split(':', 5)
        entity2 = line2[4].split(',')[0].replace("'","")
        label2 = line2[5].replace("}","").replace("'","")   #问题错的是 line2写成了line1
        print(label2)
        brr = {}
        brr[entity2] = label2
        f2.write(str(brr) + '\n')
    return arr



#对arr数组进行去重
def remove(arr):
    excess = []
    only = []
    for i in arr:
        # print(i)
        if i not in only:
            f3.write(i)
            only.append(i)
        else:
            f4.write(i)
            excess.append(i) # 重复的词
    return excess



# 将标记错误的实体取出来
def errorEntity(lines):
    file_list = set()  # 初始化空的无序集合
    for line in lines:
        # print(line)
        line = line.split(':')[0].replace('{','')
        if line not in file_list:
            file_list.add(line)
        else:
            outFile.write(line + '\n')


#将标记错误的实体 按格式  实体,类别1,类别2，类别3...实体,类别1,类别2，类别3...格式整理出来
def neaten(only1):
    label = {}
    for line1 in only1:
        first = line1.split(':')[0].replace('{','')
        last = line1.split(':')[1].replace('}','')
        if first not in label:
            value_list = [last]
            # print(type(value_list))
            label[first] = value_list
        else:
            if last not in label[first]:
                label[first].append(last)
    for key in label:
        outfile.write(key + ':' + str(label[key]) + '\n')
    return label

def neaten1(only1):
    label = {}
    for line1 in only1:
        line1 = line1.strip('\n')
        # print(line1)
        line1 = line1.split(':', 1)
        first = line1[0].replace('{', '').replace('"', '')
        # print(first)
        last = line1[1].replace('}','').replace('"', '')
        print(last)
        if first not in label:
            value_list = [last]
            # print(type(value_list))
            label[first] = value_list
        else:
            if last not in label[first]:
                label[first].append(last)
    for key in label:
        outfile.write(key + ':' + str(label[key]) + '\n')
    return label

def sort(lines):
    sortFile = open("../output/sortResult.txt","w",encoding="utf-8")
    lines.sort()
    print(lines)
    lines = lines.split(',', ' ')
    sortFile.write(lines)
    sortFile.write('\n')

# 以下每一部分在运行时需要注释其他

#第一部分 ：将所有实体和标签抽取出来
# f1 = open("../output/test1.txt","r",encoding="utf-8") #两个f1注释一个
# f1 = open("../output/dataAll(Norepeat).txt","r",encoding="utf-8")
# f2 = open("../output/allEntity.txt","w",encoding = "utf-8")
# f2 = open("../output/test1Result.txt","w",encoding = "utf-8")
# lines = f1.readlines()
# getEntity(lines)


# 第二部分：将实体和类型不重复的抽取出来  包含实体相同 类别不同的
# f = open("../output/allEntity.txt","r",encoding = "utf-8")
# f3 = open("../output/dataAll(onlyentity).txt","w",encoding = "utf-8")
# f4 = open("../output/dataAll(excess).txt","w",encoding = "utf-8")
# allines = f.readlines()
# remove(allines)

# 第三部分：将实体相同 类别不同的实体抽取出来
# inputFile = open("../output/dataAll(onlyentity).txt","r",encoding = "utf-8")
# outFile = open("../output/errorEntity.txt","w",encoding = "utf-8")
# elines = inputFile.readlines()
# errorEntity(elines)

# 第四部分：将标记错误的实体 按格式  实体,类别1,类别2，类别3...格式整理出来
# input1= open("../output/test2.txt","r",encoding = "utf-8")
# input1= open("../output/dataAll(onlyentity).txt","r",encoding = "utf-8")
# outfile = open("../output/summary.txt","w",encoding = "utf-8")
# olines = input1.readlines()
# neaten(olines) #整理

input1= open("../output/num.txt","r",encoding = "utf-8")
outfile = open("../output/summaryNum.txt","w",encoding = "utf-8")
olines = input1.readlines()
neaten1(olines) #整理

