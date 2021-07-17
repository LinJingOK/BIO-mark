
from sklearn.model_selection import train_test_split


filename = r'E:\workspace\PycharmProjects\BIO_mark_data\yao\data\data.txt'


with open(filename, 'r') as f:#with语句自动调用close()方法
    lines = f.readlines()
    data = []
    for line in lines:
        data.append(line)
        # print(data)

train_data, test_data = train_test_split(data, train_size=0.8, test_size=0.2)
with open(r"E:\workspace\PycharmProjects\BIO_mark_data\yao\divide_data\train.txt",'w',encoding='utf-8') as train_outfile:
        for line in train_data:
            train_outfile.write(line)

with open(r"E:\workspace\PycharmProjects\BIO_mark_data\yao\divide_data\test.txt", 'w',
          encoding='utf-8') as test_outfile:
    for line in test_data:
        test_outfile.write(line)
