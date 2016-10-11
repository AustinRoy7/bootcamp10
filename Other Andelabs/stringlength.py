def string_length(my_string):
  #initialize empty list to hold output
  my_list = []
  #check if string input and adds string length to output list
  if type(my_string) == str:
    length = len(my_string)
    my_list.append(length)
  #check if list input and adds length of strings in the list to ouput list
  elif type(my_string) == list:
    for string in my_string:
      length = len(string)
      my_list.append(length)
  #returns output list
  return my_list