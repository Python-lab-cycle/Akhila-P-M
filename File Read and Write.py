line="Akhila P M"
f1=open("test2.txt","w")
f1.write(line)
f1.close()
f1=open("test2.txt","r")
line=f1.read()
print("Line:",line)
f1.close()
