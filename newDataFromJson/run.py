
import os
import re

from newDataFromJson.dataFromJson import DataFromJson

filePath = './data'
# files = os.listdir(filePath)
# print(files)

findFile=os.walk(filePath)
for dirpath,dirnames,filenames in findFile:
    if '董林靖_2020.5' in dirpath:
        for i in range(len(filenames)):
            filename = filenames[i]
            if re.search(r'\d.json', filename) != None:
                # print(file)
                dirpath = dirpath.replace('\\','/')
                filepath = dirpath+'/' + filename
                filepath = filepath[2:]
                # print(filepath)
                dataFromJson = DataFromJson(filepath)
                dataFromJson.forward()
    else:
        for i in range(len(filenames)):
            filename = filenames[i]
            if re.search(r'tagged.json', filename) != None:
                # print(file)
                dirpath = dirpath.replace('\\','/')
                filepath = dirpath+'/' + filename
                filepath = filepath[2:]
                # print(filepath)
                dataFromJson = DataFromJson(filepath)
                dataFromJson.forward()


