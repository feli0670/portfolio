#Bed brugeren om at indtaste en alder og fortæl brugeren om vedkommende er myndig eller ej (18 eller derover)
alder=input('Skriv din alder: ')

if int(alder)>=18:
    print('Du er myndig')
else:
    print('Du er et barn!')