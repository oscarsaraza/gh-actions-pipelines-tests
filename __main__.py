import sys

from app import add

if __name__ == '__main__':
    if add(1, 2) != 3:
        sys.exit(1)

    print('OK')
