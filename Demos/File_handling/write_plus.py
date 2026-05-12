with open("core python/Demos/File_handling/write.txt",'w+')as fp:
    print('courser:',fp.tell())
   
    fp.write('This is first line..')
   
    fp.seek(0, 0)
   
    content  = fp.read()