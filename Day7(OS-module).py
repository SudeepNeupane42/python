import os 
''' to create a folder'''
if not os.path.exists(("Data")):
 os.mkdir("Data")

'''to create files inside that Data folder'''
# for i in range(1,100):
#     os.mkdir(f"Data/day{i}")

'''To rename the files inside Data folder'''
# for i in range (1,101):
#     os.rename(f"Data/days{i}", f"Data/day{i}")

'''To Know what files are inside a folder'''
know=os.listdir("Data")
# print(know)
know.sort() 
for i in know:
    print(i)  #prints the files inside the foder
    print(os.listdir(f"data/{i}"))   #prints whats inside the file which are inside folder
print(os.getcwd( ))                  #this will give you your current working directory
print("The above printed path is the current working directory\n")
