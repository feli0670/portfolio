#1. Redegør kort for hvad strenge er og hvordan man opererer på dem (eksempelvis sammensætte to strenge, finder længden osv).
#Strenge er en datatype for tekst og består derfor af en række forskellige tegn.
# - Det er muligt at sammenkæde to strenge ved at bruge '+' 
# - Man kan også formatere en anden datatype ind i en string bl.a. vha. 'f'
# - Versaler eller Majuskel
# - Længde af string
# - Substrings
# - Opdele eller samle 
# - Sammenligne

#2. Vis hvordan man kan indsætte nyt tegn i en streng, slette et eksisterende samt finde ud af om et tegn indgår i strengen.
str1 = 'Hello World'

print(f"Vi har strengen: '{str1}'\n")

print(f"Vi indsætter udråbstegn...")
str2 = 'Hello World'+'!'
print(f"Og har nu strengen: '{str2}'\n")

print("Vi vil nu fjerne udråbstegn igen")
str3=str2.replace('!','')
print(f"Vi har nu strengen: '{str3}'\n")
print('Man kan også bruge translate')
str4=str2.translate({ord('!'): None})
print(f"Vi har nu strengen: '{str4}'\n")

character = '!'
find4=str4.find('!')
find2=str2.find('!')

if character in str4:
    print(f"'{character}' er i strengen, '{str4}', På index, {find2}" )
else:
    print(f"Tegnet,'{character}', er ikke i strengen, '{str4}'")

if character in str2:
    print(f"'{character}' er i strengen, '{str2}'. På index, {find2}")
else:
    print(f"Tegnet,'{character}', er ikke i strengen, '{str2}'")

#3. I bilag ses noget prosa som beskriver en algoritme, der som input tager en streng og som output returnerer sand eller falsk. Forklar med ord hvad du mener algoritmen gør.
#Programmet tjekker om der er mere end et tegn i strengen, hvis den er tom eller kun besstår af et tegn returnerer den sandt,
# ellers tjekker den det forreste og bagerste tal. Hvis de er ens fjerne programmet begge tegn fra strengen. Algoritmen sørger altså for at en streng ikke kan starte eller slutte med samme tal

#4. Kan du implementere i pseudokode eller evt rigtig kode en version af algoritmen i punkt?

def bogstav(text):
    print(text)
    if len(text)<=1:
        return True

    else:
        if text[0]!=text[-1]:
            return False
        return(bogstav(text[1:-1]))
text=input('Skriv et ord: ')
print(bogstav(text))