def ascii_ch(string):
    code=ord(string)
    if code>=65 and code<=90:
     print("uppercase",string)
    elif code>=97 and code<=122:
     print("lowercase",string)
    elif code>=48 and code<=57:
     print("special character",string)
ascii_ch("r")   