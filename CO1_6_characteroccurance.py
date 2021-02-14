#character occurance
Astr=input("Enter the string\n")
char=input("Enter the character\n")
print("Given string:",Astr)
print("Given character",char)
res=0
for i in range(len(Astr)):
    if(Astr[i]==char):
        res=res+1
print("no of time character is present in the string is\n",res)
