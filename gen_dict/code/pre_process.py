# -*- coding: utf-8 -*-

#给词典标记类型



f2=open('E:\workspace\PycharmProjects\BIO_mark_data\gen_dict\data_set\proprietary_entity.txt','r',encoding="utf-8")
lines_a=f2.readlines()

f3=open(r'E:\workspace\PycharmProjects\BIO_mark_data\gen_dict\data_set\abstract_entity.txt','r',encoding="utf-8")
lines_b=f3.readlines()

f4=open(r'E:\workspace\PycharmProjects\BIO_mark_data\gen_dict\data_set\attribute_value.txt','r',encoding="utf-8")
lines_c=f4.readlines()

f5=open(r'E:\workspace\PycharmProjects\BIO_mark_data\gen_dict\data_set\rule_name.txt','r',encoding="utf-8")
lines_d=f5.readlines()

out_file = open(r'E:\workspace\PycharmProjects\BIO_mark_data\gen_dict\result\word_dict.txt','w')

for line in lines_a:
    str = "%s PRO\n"% (line[:-1])  #专有名词
    out_file.write(str)
for line in lines_b:
    str = "%s ABS\n" % (line[:-1]) #抽象名词
    out_file.write(str)
for line in lines_c:
    str = "%s ATT\n" % (line[:-1])  # 属性值
    out_file.write(str)
for line in lines_d:
    str = "%s NORM\n" % (line[:-1])  # 规范名
    out_file.write(str)


#关闭文件
f2.close()
f3.close()
f4.close()
f5.close()