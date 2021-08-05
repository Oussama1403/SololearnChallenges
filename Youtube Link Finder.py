import re

pattern =(r"https://www.youtube.com/watch\?v=|https://youtu.be/")
stri = input()
newstr = re.sub(pattern,"",stri)

print(newstr)
