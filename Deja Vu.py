inp = input()

for letters in inp:
    if inp.count(letters) > 1:
        print("Deja Vu")
        break
else:
    print("Unique")
        
