n = 65
abc = 25
while abc != -2:
    while n != 91:
        c = chr(n)
        print(c,end="")
        n += 1
    print("")
    n -= abc
    abc -= 1
