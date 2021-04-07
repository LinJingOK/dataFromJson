# dataFromJson
从json文件中读取实体和关系标注的数据
主要是生成实体和实体标签文件  关系和关系标签  以及图数据库所需要的五元组数据

有两部分：
1.pw写的，以及我的文件夹中补充
2.自己用js写的读取json文件数据

newDataFromJson 文件夹是pw的，其中linjing是自己的
jsReadJson 自己写的js读取json文件数据
Neo4j  将抽取的五元组的数据文本存储在neo4j的图数据库中
