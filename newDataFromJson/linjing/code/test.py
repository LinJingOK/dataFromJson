
# dict = {
#     'a': 2,
#     'b': 1
# }
#
# if 'a' in dict:
#     print(dict['a'])


#2.遍历数据
file_list = set()
f1 = open("../output/summaryNum.txt","r",encoding="utf-8")
f2 = open("../output/summaryNum(redundancy).txt","w",encoding = "utf-8")

lines = f1.readlines()
for line in lines:
    length = len(line.split(','))
    if (length > 1):
        f2.write(line)
    else:
        pass

f1.close()
f2.close()