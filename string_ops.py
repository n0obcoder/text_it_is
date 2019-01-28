a= 'i am gonna use a #hash'

#USE OF LAMBDA
#convert_to_upper = lambda x: x.upper()
#print(convert_to_upper(a))
#I AM GONNA USE A #HASH

#USE OF LAMBDA WITH MAP
#print(map(lambda x: x.upper(), a.split()))
#['I', 'AM', 'GONNA', 'USE', 'A', '#HASH']

#USE OF LAMBDA WITH MAP
#l = map(lambda x: x.upper(), a.split())
#print(l)
#['I', 'AM', 'GONNA', 'USE', 'A', '#HASH']

#REMOVAL OF NUMBER
#newstring = 'i am gonna use a0 #ha33sh 3456'
#string = ''.join([c for c in a if newstring not in "1234567890"])
#print(string)
#i am gonna use a #hash


#REMOVAL OF NUMBER AGAIN
#import re
#def test(str):
    #string_no_numbers = re.sub("\d+", " ", str)
    #print(string_no_numbers)
#test('abc123') #prints abc

#REMOVAL OF NUMBER YET AGAIN
#'2'.isdigit()
#True
