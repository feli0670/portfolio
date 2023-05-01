#Herunder nogle små opgaver hvor du skal skrive en funktioner, der løser problemet. Løs så mange du kan (nå):
#1. Skriv en funktion der finder det største tal af tre givne tal som argumenter.
def maxTal(a:int,b:int,c:int):
  if a > b and a > c:
    return a
  elif b > c:
    return b
  return c

print(maxTal(10,10,6))
print(maxTal(8,5,2))

#2 Skriv en funktion der summer alle tal i en liste.
from typing import List

def Sum(list: List[int]):
  sum=0
  for n in list:
    sum+=n
  return sum
Sum([11,32,42,2])

#3 Skriv en funktion, der bytter om på rækkefølgen i en given liste.
def flyt(list):
  newList = list[-1:]+list[:-1]
  print(newList)
flyt([1,2,3,4])

# #4 Skriv en funktion, der undersøger om et tal er indenfor et givent interval.
def interval(N):
  if 5 < N < 42:
    print(f"tallet {N} er inden for intervallet")
  else:
    print(f"tallet {N} er ikke inden for intervallet")

interval(6)

#5 Skriv en funktion, der tager en liste af tal og returnerer en ny liste der består af de unikke tal fra den liste.
from typing import List
def new_list(list: List[int]):
  list2=list
  return list2
new_list([1,2,3,4])

#6 Skriv en funktion, der givet en liste kun printer de lige tal.
from typing import List
def even_numbers(list):
  for n in list:
    if n%2==0:
      print(n)
even_numbers([20,21,22,23])