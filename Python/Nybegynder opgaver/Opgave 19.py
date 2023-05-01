#Print multiplikationstabellen fra 1 til 10.
print('\t\t\tMultiplication Tables \n')
for x in range (1,11):
     print(x, end='\t')
print()
print('__________________________________________________________________________\n')
for x in range (1,11):
    for y in range (1,11):
        print(x*y, end='\t')
    print('\n')