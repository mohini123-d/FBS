with open("core python/Demos/File_handling/write.txt",'a+')as fp:
    print('cursor:',fp.tell())

    fp.seek(0,0)

    print('content:',fp.read())

    fp.write('\nThis is next line.')
    fp.seek(0,0)

    print('content:',fp.read())