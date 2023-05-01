tekst = 'HEJ Lukas du spiller cookie clicker'

O = len(tekst.split())
P = tekst.count('.')
L = 0

if P==0:
  print('Det er en dårlig tekst, hvis ikke du har sat punktum')
else:
  tekst_uKomma = tekst.replace(",","")
  tekst_uPunkt = tekst_uKomma.replace(".","")
  nyTekst = tekst_uPunkt.split()

  for word in nyTekst:
    if len(word)>6:
      L+=1

  print(f'O: {O}')
  print(f'P: {P}')
  print(f'L: {L}')

  LIX = O/P + (L*100/O)
  LIX_rounded = round(LIX, 2)
  print(LIX_rounded)

  if LIX>=55:
    print('Meget svær, faglitteratur på akademisk niveau, lovtekster.')
  elif LIX >=45:
    print('Svær, f.eks. saglige bøger, populærvidenskabelige værker, akademiske udgivelser.')
  elif LIX >=35:
    print('Middel, f.eks. dagblade og tidsskrifter.')
  elif LIX >=25:
    print('Let for øvede læsere, f.eks. ugebladslitteratur og skønlitteratur for voksne.')
  elif LIX<25:
    print('Let tekst for alle læsere, f.eks. børnelitteratur.')
