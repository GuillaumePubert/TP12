def reverseString(s, i = 0) :
    if i == len(s):
       return ""
    else:
        print(s[-i-1],end="")
        return reverseString(s, i+1)

#print(reverseString("")) # ""
print(reverseString("bonjour")) # ruojnob
print(reverseString("ressasser")) # ressasser
