#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        return str[:n] + str[n+1:]
     elif abs(n) <= len(str):
          return str[:n] + str[n+1:]
       else:
           raise ValueError("Index out of range")
