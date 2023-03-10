#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_len = (len(argv) - 1)
    if argv_len == 0:
        print(argv_len)
    else:
        count = 0
        for i in range(1, argv_len+1):
            try:
                count += int(argv[i])
            except ValueError:
                print(f"Argument {i} is not an integer: {argv[i]}")
                continue
            print(count):wq1
