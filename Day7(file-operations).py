
f=open("files/day7.txt","r")
while True:
    text=f.readline()
    print(text)
    if not text:
      break
f.close()

#seek moves to the nth position in file
with open('files/seektell.txt','r+') as f:
    f.write("apple boy cat and a big dog")
    f.seek(10)
    # tell gives you the current position  of the pointer
    print(f.tell())
    text=f.read(5)
    print(text)
    print(f.tell())
    # f.truncate(7)  using function you can limit the bytes/size of the input you want to write in a file
    