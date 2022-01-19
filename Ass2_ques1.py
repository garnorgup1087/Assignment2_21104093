str="Python is a case sensitive language."
#(a)finding length of string
print(len(str))
#(b)reverse order of string
print(str[::-1])
#(c)storing "a case sensitive" in new string using slice function
str1=str[10:26:]
print(str1)
#(d)replacing "a case sensitive" with"object oriented"
print(str.replace("a case sensitive","object oriented"))
#(e)finding index of substring a
print(str.find('a'))
#(f)removing white spaces in string
print(str.replace(" ",""))
