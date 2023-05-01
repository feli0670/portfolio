tekst = ['Der var engang', 'en mand som', 'boede i en spand. Spanden var af ler']


###sammenkæd de tre tekststrenge via variablerne
print(tekst[0], tekst[1], tekst[2])

###bestem længden af hver af dem.
t = int(len(tekst))
for i in range (t):
    print(len(tekst[i]))

###undersøg det andet bogstav i hver af dem
for i in range (t):
    print(tekst[i][1])

###undersøg om to af variablerne er det samme
print(tekst[0] == tekst[1])

###skriv hele teksten som versaler
tekst_str = ''.join(tekst)
tekst_versal = tekst_str.upper()
print(tekst_versal)

###lav en ny variable der er en delstreng af en af variablerne.
substring = tekst[2][-1]
print(tekst[2][18:])

###sammenflet de tre variabler så det første bog stav er fra den første variable, den anden fra den anden osv.
tekst_ny = [tekst[0][0], tekst[1][0], tekst[2][0]]


###undersøg hvor mange forekomster af e der er i teksten.
print(tekst_str.count('e'))