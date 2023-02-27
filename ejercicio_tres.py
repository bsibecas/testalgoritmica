#!/usr/bin/python3

from sys import argv

def try_float(nb):
    try:
        float(nb)
    except ValueError:
        return False
    else:
        return True

def error_handling(horas, tarifa):
    if try_float(horas) == False or try_float(tarifa) == False:
        print ("Error: Number expected")
        return (84)

def calculate_extra_time(horas, tarifa):
    valor = (tarifa * 50) / 100
    return (valor * horas)

def calculate_salary(horas_trabajadas, tarifa):
    if horas_trabajadas <= 40:
        total = horas_trabajadas * tarifa
    else:
        total = 40 * tarifa + calculate_extra_time(horas_trabajadas - 40, tarifa)
    print("El salario de este trabajador sera de %2.f" % total)


def main():
    HORASTRABAJADAS = input("Indique las horas trabajadas:")
    TARIFA = input("Indique la tarifa: ")
    if error_handling(HORASTRABAJADAS, TARIFA) == 84:
        return (84)
    calculate_salary(float(HORASTRABAJADAS), float(TARIFA))

if __name__ == '__main__':
    exit(main())