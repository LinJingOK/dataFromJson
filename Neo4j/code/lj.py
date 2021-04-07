
#coding:utf-8
from itertools import islice
from py2neo import Graph,Node,Relationship
#py2neo 4.3

##连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474',username='neo4j',password='1')

#{'f_node_name':'计算机网络概述','f_node_label':'概念','relation_name':'包含','l_node_name':'计算机网络定义','l_node_label':'概念'}

def create(filename):
    with open(filename,'r',encoding='utf-8') as fr:
        for line in fr:
            if line != '':
                dic=eval(line)
                f_node=Node(str(dic.get('f_node_label',0)),name=str(dic.get('f_node_name',0)))
                l_node=Node(str(dic.get('l_node_label',0)),name=str(dic.get('l_node_name',0)))
                relation=Relationship(f_node,str(dic.get('relation_name',0)),l_node)
                graph.merge(f_node,'label','name') #str(dic.get('f_node_label', 0)
                graph.merge(l_node,'label','name')
                graph.create(relation)
                # graph = Graph()
                # tx = graph.begin()
                # tx.merge(f_node, str(dic.get('f_node_label',0)), 'name') #node label primary
                # tx.merge(l_node, str(dic.get('l_node_label',0)), 'name')
                # tx.merge(relation)
                # tx.commit()
            else:
                break

# create('example.txt')
create('../input_data/dataAll.txt')

#清除图谱
#graph.delete_all()



