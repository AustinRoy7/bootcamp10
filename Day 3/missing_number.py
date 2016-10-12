def find_missing(list1,list2):
  #initialize variable absent meant to hold absent digit to zero
	absent = 0
	#find and  display missing number if first list is smaller
	if len(list1) < len(list2):
		miss = (set(list2) - set(list1))
		absent = miss.pop()
		return absent
	#find and  display missing number if second list is smaller
	if len(list2) < len(list1):
		miss = (set(list1) - set(list2))
		absent = miss.pop()
		return absent
	#default statement
	else:
	  return 0
	
