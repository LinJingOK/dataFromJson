input1= open("../output/allEntity.txt","r",encoding = "utf-8")
outputFile = open("../output/num.txt","w",encoding = "utf-8")

lines = input1.readlines()
counts = {}
for line in lines:
    line = line.strip('\n')
    if line in counts:
        counts[line] += 1
    else:
       counts[line] = 1
print(counts)
outputFile.write(str(counts))