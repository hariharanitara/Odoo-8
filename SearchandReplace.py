filein = '/home/hari/hari_python_test_code/sample.txt'  ##file path
fileout = '/home/hari/hari_python_test_code/sample.txt'  ###file path
f = open(filein,'r')
filedata = f.read()
f.close()

newdata = filedata.replace("good","bad")

f = open(fileout,'w')
f.write(newdata)
f.close()

