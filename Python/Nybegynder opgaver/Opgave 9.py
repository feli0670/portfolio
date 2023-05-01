#Skriv et program til at finde summen af de lige tal fra 1 til 100.
max = 100
sum = 0

for number in range(1, max+1):
    if(number % 2 == 0):
        print(number)
        sum+= number

print(f"'Summen af alle lige tal fra 1 til {max} = {sum}")