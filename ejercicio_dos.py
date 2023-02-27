#!/usr/bin/python3

from sys import argv

def get_people():
    x = 0
    personas = []
    persona = []

    max = int(input("Numero de personas:"))

    for i in range(max):
        persona.append(input("Introduce el nombre de la persona:"))
        persona.append(input("Introduce el sexo de la persona con M o H:"))
        persona.append(input("Introduce la edad de la persona:"))
        personas.append(persona)
        persona = []
        x += 1
    return personas

def calcul_porcent(total, mas18, mujeres):
    print("%d porcentaje de mayores de edad" % (mas18 * 100) / total)
    print("%d porcentaje de mujeres" % (mujeres * 100) / total)

def verify_info(personas):
    x = 0
    mas18 = 0
    h_mas18 = 0
    m_menos18 = 0
    mujeres = 0

    while x < personas.size():
        if int(personas[x][3]) >= 18:
             mas18 += 1
             if personas[x][2] == "H":
                h_mas18 += 1
        else:
            if personas[x][2] == "M":
                m_menos18 += 1
        if personas[x][2] == "M":
            mujeres += 1
        x += 1
    menos18 = personas.size() - mas18
    print("%d personas tienen 18 o más" % mas18)
    print("%d personas tienen menos de 18" % menos18)
    print("%d personas tienen 18 o más y son hombre" % h_mas18)
    print("%d personas tienen menos de 18 y son mujeres" % m_menos18)
    calcul_porcent(personas.size(), mas18, mujeres)
        

def main():
   PERSONAS = get_people()
   verify_info(PERSONAS)

if __name__ == '__main__':
    exit(main())