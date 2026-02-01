def palidrome(r):
    e = len(r)-1
    s = 0
    while s < e:
        if r[s]!=r[e]:
            return False
        s += 1
        e -= 1
    return True
r = (9,8,7,7,8,9)
if palidrome(r):
    print("palindrome")
else:
    print("not palindrome")