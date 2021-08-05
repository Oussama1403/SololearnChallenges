from re import search

def is_vpw(inp):
    if len(inp) >= 7:
        return all(search(i, inp) for i in tests)
    return False

tests = r"[0-9]{2,}", r"[!@#$%&*]{2,}"

inp = input()

print("Strong" if is_vpw(inp) else "Weak")
