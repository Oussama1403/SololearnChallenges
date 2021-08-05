import re
pattern = r"[""#$%&'()*+,-./:;<=>?@[\]^_`{|}~""0-9]"

stri = input()
newstr = stri[::-1]
newstr = re.sub(pattern, "", newstr)

print(newstr)
