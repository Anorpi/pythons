# File: readline-example-1.py
 
file = open("E:\\tt.txt")
 
while 1:
    line = file.readline()
    print line
    if not line:
        break
    pass # do something
