#!/usr/bin/python3
def uppercase(s):
    s = list(s)
    for i in range(len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            s[i] = chr(ord(s[i]) - 32)
            print("{}".format(("").join(s)))
