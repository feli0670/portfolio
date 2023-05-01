#Brug en while-løkke til at skrive de lige tal mellem 1 og 100 ud på skærmen.
max=100
i=1
while i<=max:
    if i%2==0:
        print(str(i))
    i+=1