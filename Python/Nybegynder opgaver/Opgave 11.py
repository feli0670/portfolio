#Skriv et program der udregner løsningen til udtrykket (x+y)*(x-y) hvor du selv sætter x og y til bestemte værdier
x=int(input('Skriv et tal: '))
y=int(input('Skriv endnu et tal: '))
result=(x+y)*(x-y)
print(f'({x}+{y})*({x}-{y})={result}')