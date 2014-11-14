#!/usr/bin/env python
import sys

if __name__ == '__main__':
    files = []
    for f in sys.argv[1:]:
        if f == '-':
            files.append(f)
        else:
            fp = open(f, 'w')
            files.append(fp)

    text = raw_input()
    while text:
        print(text)
        for f in files:
            if f == '-':
                print(text)
            else:
                f.write(text)
        text = raw_input()

    for f in files:
        if not f == '-':
            f.close()
