#write in file
f=open('files/day7.txt','w')
f.write("hello hi")
f.close()

#append in a file
f=open('files/day7.txt','a')
f.write(" \nMy name is sudip.")
f.close()

#read from file
''' by using with keyword you do not need to close the file '''
with  open ('files/day7.txt', 'r') as f:
    text=f.read()
    print(text) 
