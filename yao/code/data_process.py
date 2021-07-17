


infile = open("../data/test_result.txt", "r", encoding="utf-8")
# dict_file = open("../output/dict.txt", "w", encoding="utf-8")
dict_file = open("../output/dict.txt", "r", encoding="utf-8")
dict_file1 = open("../data/test_data.txt", "r", encoding="utf-8")
unlabel_file = open("../output/unlabel_test.txt", "w", encoding="utf-8")




#简单的处理了原来数据文件的格式   一个实体 一个字符  生成BIO标记词典
# lines = infile.readlines()
# for line in lines:
#     line = line.replace('),', '\n').replace('[','').replace(']','').replace('(','').replace(')','').replace("'",'').replace(",",'')
#     print(line)
#     dict_file.write(line)


#取消行首的空格
# lines = dict_file.readlines()
# for line in lines:
#     line = line.strip()
#     print(line)
#     dict_file1.write(line + '\n')


# 生成未标注实体的文件
def unlabelFile():
    lines1 = dict_file1.readlines()
    for line1 in lines1:
        line1 = line1.strip().split(' ',1)[0]
        print(line1)

        unlabel_file.write(line1.replace('。','。\n'))
unlabelFile()


