import random
if __name__ == '__main__':

    name = r'E:\workspace\PycharmProjects\BIO_mark_data\information_safty_data_mark\data\origin.txt'
    with open(name, 'r', encoding='utf-8') as f:
        lines = f.readlines()#获取所有行
        sum = 0
        list = []
        for line in lines:#第i行
            #找到第一个空格
            list.append(line)
            # for j in range(len(line)):
            #     if line[j].isspace() == True:
            #         a = line[:j]
            #         # if a not in list:
            #         list.append(a)
            #         sum += 1


    with open('E:\workspace\PycharmProjects\BIO_mark_data\information_safty_data_mark\divide\divide_data\dev.txt', 'w', encoding='utf-8') as g:
        a = random.sample(list, 30)#随机抽取100行 sample(list, k)返回一个长度为k新列表，新列表存放list所产生k个随机唯一的元素
        for i in a:
            g.write(i)
f.close()
g.close()
# print(sum)
