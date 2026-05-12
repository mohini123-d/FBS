import pickle
di = {'id':'103', 'Name':'Mohini', 'sal':'70000','dept':'IT'}

fp = open('core python/Demos/File_handling/write.pkl','wb')

pickle.dump(di, fp, protocol = pickle.HIGHEST_PROTOCOL)

fp.close()