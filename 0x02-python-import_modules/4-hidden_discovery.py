#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    all_dir = dir(hidden_4)
    for name in all_dir:
        if not name.startswith('_'):
            print(name)
