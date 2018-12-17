import itertools
def isPalindrome(w):
   for i in range((len(w))/2):
      if w[i] != w[-i-1]:
         return False
   return True

if __name__ == "__main__":
   word = "civic"
   print "Is %s palindrome ? %s"  %(word, isPalindrome(word))
   #for w in itertools.permutations(word):
   #   word = "".join(w)
   #   print "Is %s palindrome ? %s"  %(word, isPalindrome(word))
   
   word = "xyyx"
   print "Is %s palindrome ? %s"  %(word, isPalindrome(word))
   #for w in itertools.permutations(word):
   #   word = "".join(w)
   #   print "Is %s palindrome ? %s"  %(word, isPalindrome(word))
