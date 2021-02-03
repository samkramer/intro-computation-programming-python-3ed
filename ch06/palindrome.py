# Chapter 6.2 Palindromes
# Figure 6-4, 6-5: Palindrome testing

def is_palindrome(s):
   """Assumes s is a str
      Returns True if s is a palindrome; False otherwise.
       Punctuation marks, blanks, and capitalization are ignored."""
   
   def to_chars(s):
      s = s.lower()
      letters = ''
      for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            letters = letters + c
      return letters

   def is_pal(s):
      print('  is_pal called with', s)
      if len(s) <= 1:
         print('  About to return True from base case')
         return True
      else:
         answer = s[0] == s[-1] and is_pal(s[1:-1])
         print('  About to return', answer, 'for', s)
         return answer
         
   return is_pal(to_chars(s))

if __name__ == "__main__":
    print('Try radar')
    print(is_palindrome('radar'))
    
    print()
    
    print('Try dogGod')
    print(is_palindrome('dogGod'))
    
    print()
    
    print('Try doGood')
    print(is_palindrome('doGood'))