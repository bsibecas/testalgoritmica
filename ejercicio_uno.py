#!/usr/bin/python3

from sys import argv

def is_pair(numero):
    while numero >= 0:
        if numero % 2 == 0:
            print(numero)
        numero -= 1

def is_odd(numero):
    while numero >= 1:
        if numero % 2 != 0:
            print(numero)
        numero -= 1

def try_int(nb):
    try:
        int(nb)
    except ValueError:
        return False
    else:
        return True

def error_handling(argv):
    if len(argv) != 2:
        print ("Error: One argument expected")
        return (84)
    if try_int(argv[1]) == False:
        print ("Error: Number expected")
        return (84)

def main():
    if error_handling(argv) == 84:
        return 84
    numero = int(argv[1])
    if numero % 2 == 0:
        is_pair(numero)
    else:
        is_odd(numero)

if __name__ == '__main__':
    exit(main())