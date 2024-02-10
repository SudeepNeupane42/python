def convertToList(msg):
  list=[]
  for i in msg:
    list.append(i)
  return list


def convertToString(list):
  string=""
  for i in list:
    string+=i
  return string
  
#encode
def encode(msg):
  if len(msg)<3:
    msg.reverse()
    return msg
  else:
    msg.append(msg[0])
    msg.remove(msg[0])
    li=["jsg","pjd"]
    msg.extend(li[0])
    for i in li[1]:
      msg.insert(0,i)
    
    return msg
    
def decode(msg):
  if len(msg)<3:
    msg.reverse()
    return msg
  else:
    msg=msg[3:-3]
    a=msg.pop(-1)
    msg.insert(0,a)
    return msg
  
while(1):
  a=int(input("\nWhat do you want to do? \n1.encode \n2.decode\n3.Exit\n"))
  match a:
    case 1:
      msg=input("\nenter the message to be encoded: ")
      list=convertToList(msg)
      list= encode(list)
      msg=convertToString(list)
      print("The encoded message is:",msg)
      
    case 2:
      msg=input("\nenter the message to be decoded: ")
      list=convertToList(msg)
      list= decode(list)
      msg=convertToString(list)
      print("The decoded message is:",msg)
  
    case 3:
      print("\nThank you for using this program")
      exit()
  
    case _:
      print("Please enter a valid input")

