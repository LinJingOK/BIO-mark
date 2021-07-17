

infile1 = open("../data/test_data.txt", "r", encoding="utf-8")  #原来标记的
# dict_file = open("../output/dict.txt", "w", encoding="utf-8")
infile2 = open("../output/labeled_test.txt", "r", encoding="utf-8") # 预测标记的
only_label = open("../data/only_label.txt", "r", encoding="utf-8") # 读
# only_label = open("../data/only_label.txt", "w", encoding="utf-8") #写
outfile = open("../data/merge.txt", "w", encoding="utf-8")



#将预测文件中的预测标签提取出来
def getLabel():
    lines2 = infile2.readlines()
    for line2 in lines2:
        line2 = line2.strip()
        if len(line2) > 0:
            line2 = line2.split(' ',1)
            print(line2)
            line2 = line2[1]
            only_label.write(line2 + '\n')
# getLabel()

# 合并两个文件的标签
def merge():
    lines1 = infile1.readlines()
    # lines2 = only_label.readline()
    # print(lines2)
    for line1 in lines1:
        line1 = line1.strip()
        if len(line1) > 0:
            outfile.write(line1.strip('\r\n') + ' ')
            outfile.write(only_label.readline())
        # outfile.write(line2)
merge()

