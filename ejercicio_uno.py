#!/usr/bin/python3

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

def error_handling(input_nb):
    if try_int(input_nb) == False:
        print ("Error: Number expected")
        return (84)

def main():
    input_nb = input("LEER NUMERO:")
    if error_handling(input_nb) == 84:
        return 84
    NUMERO = int(input_nb)
    if NUMERO % 2 == 0:
        is_pair(NUMERO)
    else:
        is_odd(NUMERO)

if __name__ == '__main__':
    exit(main())