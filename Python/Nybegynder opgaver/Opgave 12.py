#Skriv et program der løser en andengradsligning og finder toppunktet
from math import *

#variabler og ligning
try:
    a=int(input('Indtast a-værdi: '))
    b=int(input('Indtast b-værdi: '))
    c=int(input('Indtast c-værdi: '))
    print(f'\nAndengradsligningen:\n{a}x^2+{b}x+{c}')

    #diskriminant
    d=(b**2)-(4*a*c)
    print(f'\nDiskriminanten:\nd = {d}')

    #løsning
    if d>=0:
        x=(((-b)+(sqrt(d))))/(2*a)
        x2=((-b)-(sqrt(d)))/(2*a)
        if d==0:
            l1='Der er en løsning'
        if d>0:
            l1='Der er to løsninger'
        print(f'\n{l1}:\nx = {x}\nx2 = {x2}')
    else:
        print('\nDer er ingen løsning på ligningen')

    #toppunkt
    tx=(-b/(2*a))
    ty=(-d/(4*a))
    print(f'\nToppunktets koordinater:\ntx = {tx}\nty = {ty}')
except ZeroDivisionError:
    print('Du kan ikke dividere med 0')