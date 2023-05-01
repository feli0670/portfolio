tekst = open("mytext.txt", "r", encoding="utf-8") #en txt fil importeres til læsning i tegnsætnings formatet utf-8
tekst = tekst.read() #filen læses af programmet og gemmes i en variabel som en string

# variablerne til LIX formlen angives her
O = len(tekst.split()) #ord, angiver længden af et array som dannes ved at splitte en string hver gang der er mellemrum
P = tekst.count('.') #punktum, tæller hvor mange punktummer der er i teksten
L = 0 #lange ord

if P==0:
  print('Det er en dårlig tekst hvis ikke du har sat punktum')
else:
  tekst_uKomma = tekst.replace(",","")
  tekst_uPunkt = tekst_uKomma.replace(".","")
  nyTekst = tekst_uPunkt
  nyTekst = nyTekst.split(" ")

  for word in nyTekst:
    if len(word)>=6:
      L+=1
      
  print(f'O: {O}') #variablen 'O' bliver printet son en string
  print(f'P: {P}') #variablen 'P' bliver printet son en string
  print(f'L: {L}') #variablen 'L' bliver printet son en string

  LIX = O/P + (L*100/O) #formlen for LIX-tallet er angivet og tildeles her
  LIX_rounded = round(LIX, 2) #værdien af LIX afrundes til 2 decimaler
  print(LIX_rounded) #det beregnede LIX-tal printes

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
