#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    value = 0
    for suma in range(len(sys.argv) - 1):
        value += int(sys.argv[suma + 1])
    print("{}".format(value))
