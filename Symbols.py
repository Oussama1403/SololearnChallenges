import re

pattern = r"[""#$%&€'()*+,-./:;<=>?@[\]^_`{|}~""]"
stri = input()
newstr = re.sub(pattern, "", stri)

print(newstr)
