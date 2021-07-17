# import cPickle as pickle
import codecs
import _pickle as cPickle
f = codecs.open(r'E:\workspace\PycharmProjects\BIO_mark_data\show_file\data\word2id.pkl','rb',encoding='utf-8')
info = cPickle.load(f)
print(info)   #show file