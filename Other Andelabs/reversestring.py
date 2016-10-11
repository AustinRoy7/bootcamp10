def reverse_string(string):
  #check and account for empty string returning None
  if string =="":
    return None
  else:
    #reverses string and assigns variable rev to this reverse 
    rev = string [::-1]
    #return true for palindromes
    if rev == string:
      return True
    #return string reverse
    else:
      return rev
