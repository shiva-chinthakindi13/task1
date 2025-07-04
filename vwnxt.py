def word(name):
 secret=" "
 for i in range(len(name)):
  code=ord(name[i])
  if name[i]=="a" or name[i]=="e" or name[i]=="i" or name[i]=="o" or name[i]=="u":
   secret+=chr(code+1)
  else:
   secret+=name[i]

 print(secret)
 
word("python")




