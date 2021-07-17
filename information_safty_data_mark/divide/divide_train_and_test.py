
from sklearn.model_selection import train_test_split


filename = r'E:\workspace\PycharmProjects\BIO_mark_data\information_safty_data_mark\data\origin.txt'


with open(filename, 'r',encoding='utf-8') as f:#with语句自动调用close()方法
    lines = f.readlines()
    data = []
    for line in lines:
        data.append(line)
        # print(data)

train_data, dev_data = train_test_split(data, train_size=0.7, test_size=0.3)
with open(r"E:\workspace\PycharmProjects\BIO_mark_data\information_safty_data_mark\divide\test_divid\train.txt",'w',encoding='utf-8') as train_outfile:
        for line in train_data:
            train_outfile.write(line)

with open(r"E:\workspace\PycharmProjects\BIO_mark_data\information_safty_data_mark\divide\test_divid\test.txt", 'w',
          encoding='utf-8') as test_outfile:
    for line in dev_data:
        test_outfile.write(line)
