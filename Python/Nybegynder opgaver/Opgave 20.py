#Lav et program der givet et tal n først printer n stjerner (*) og på næste linje n-1 osv.
n=int(input('skriv et tal: '))
for x in range(n):
    print('*' * n)
    n-=1
