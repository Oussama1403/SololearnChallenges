dic = {
    
    "Rawr": "Tiger",
    "Grr": "Lion",
    "Ssss": "Snake",
    "Chirp": "Bird",
    }
x = input()
split = x.split()
lst=[]

for sound in split:
    for key, value in dic.items():
        if sound == key:
            lst.append(value)
            o = " ".join(lst)
            
print(o)  dic = {
    
    "Rawr": "Tiger",
    "Grr": "Lion",
    "Ssss": "Snake",
    "Chirp": "Bird",
    }
x = input()
split = x.split()
lst=[]

for sound in split:
    for key, value in dic.items():
        if sound == key:
            lst.append(value)
            o = " ".join(lst)
            
print(o)  
