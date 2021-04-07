import numpy as np
import re
infile = open('../data/5-gram-yao.txt',"r", encoding="utf-8")
outfile = open('../input_data/yao.txt',"w", encoding="utf-8")
f = infile.readlines()

for line in f :
    line = line.replace("f_node_name","'f_node_name'").replace("f_node_label", "'f_node_label'")\
        .replace("relation_name", "'relation_name'").replace("l_node_name", "'l_node_name'")\
        .replace('"', "'").replace("/[1-9][0-9]*/","").replace(": Tuples ", "")
    # rule = "\d"
    new_line = re.sub('[\d]', '', line)

    # line = line.split("{", 1)
    # # del(line[0])

    print(new_line)
    outfile.write(str(new_line))