import pickle

fp = open('core python/Demos/File_handling/write.pkl','rb')

obj = pickle.load(fp)

print(obj)