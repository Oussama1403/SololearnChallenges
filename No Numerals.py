x = input()

dic = {
    "10": "ten",
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

for key, value in dic.items():
    x = x.replace(key, value)

print(x)
