
def count_palindromes(s):
    s=s.split(" ")
    count=0
    palindrome_exist=False
    for i in range(len(s)):
      if s[i][::-1]==s[i]:
        palindrome_exist=True
        count+=1
        
        # print("palindromes exist")
        
        
    if palindrome_exist ==False:
        print("palindromes doesnt exist")
    return count
    
s="my family consists of amma akka nana anna"
count_palindromes(s)
print("there are",count_palindromes(s),"palindromes")