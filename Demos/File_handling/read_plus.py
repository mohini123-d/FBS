with open("core python/Demos/File_handling/write.txt",'r+')as fp:
    print('courser position:',fp.tell())
    fp.seek(0,0) #0:beg 1:current 2:end

    content =fp.read()
    print('content:',content)

    print('coursor position:',fp.tell())

    fp.write('Abc')
    print('corser position:',fp.tell())

    #fp.seek(0,0)

    contenet = fp.read()
    print('content:',content)         