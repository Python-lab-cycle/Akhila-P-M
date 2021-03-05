list1=['shee','lee','reshi']
print("The ordinal list:\n"+str(list1))
res=[ord(ele)for sub in list1 for ele in sub]
print("the ascii list is:\n"+str(res))
