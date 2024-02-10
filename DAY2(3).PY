
#string method
a="sUdep! neupane!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))    #removes the trailing character
print(a.replace("sudeep","ronny")) #replaces all           occurences of a string with another string
print(a.split(" ")) #splits the string by space " "
print(a.capitalize())  #first character capital and all other strings small
print(a.center(25))
print(a.count("e"))
str1="my name is sudeep"
str2="SudiP"
print(str1.find("is"))
print(str2.isalnum()) #checks if alphanumeric or not
print(str2.isalpha()) #checks if alphabetic or not
print(str2.islower())
print(str2.isprintable()) #\n is not printable
print(str1.isspace()) #checks if string contains space
print(str1.title()) 