#Skriv et program, der finder ud af om et element eksisterer i en liste.
burger = ['bolle','overbolle', 'mayonaise', 'ketchup', 'sennep', 'salat', 'pickles', 'tomat', 'bøf', 'underbolle']
fyld = input('Skriv noget du vil have i din bruger: ')


if fyld in burger:
    print(f'Det valgte fyld, {fyld.upper()}, er i burgeren')
    print()
elif fyld not in burger:
    print(f'Det valgte fyld, {fyld.upper()}, er ikke i burgeren')
