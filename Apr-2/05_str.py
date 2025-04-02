my_string = "akashtiwari@1214.gmail.com"

my_int = "•♬•♫ ₴ⱧØɄ₦₳₭₮ł₩₳Ɽł •♬•♫"

encode_method = my_string.encode()

encode_insta = my_int.encode()


print("Encoded string : ",encode_method)
print("Encoded string : ",encode_insta)


'''
error : 

''backslashreplace'	- uses a backslash instead of the character that could not be encoded
'ignore'	- ignores the characters that cannot be encoded
'namereplace'	- replaces the character with a text explaining the character
'strict'	- Default, raises an error on failure
'replace'	- replaces the character with a questionmark
'xmlcharrefreplace'	- replaces the character with an xml character'

'''