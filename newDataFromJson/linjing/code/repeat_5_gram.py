from pandas import read_csv

#去掉五元组中重复的

#1.pandas的去重 失败
# df = read_csv('../output/dataAll.txt')
# newDF = df.drop_duplicates()
# print(newDF)
# f2 = open("../output/dataAll(Norepeat).txt","w",encoding = "utf-8")
# f2.write(str(newDF) + '\n')


#2.遍历数据
file_list = set() #初始化空的无序集合
# f1 = open("../output/dataAll.txt","r",encoding="utf-8")
# f2 = open("../output/dataAll(Norepeat).txt","w",encoding = "utf-8")

f1 = open("../output/summaryNum(redundancy).txt","r",encoding="utf-8")
f2 = open("../output/summaryNum(888888888).txt","w",encoding = "utf-8")

lines = f1.readlines()
for line in lines:
    if line not in file_list:
        f2.write(line)
        file_list.add(line)
f1.close()
f2.close()


