# Skriv et program, der beregner porto for et brev. Input data er brevets vægt (i gram). 
# Output data er prisen, for at sende det som A-post i Danmark. 
# 1g = 0,24 dkk
# 50 g = 12 dkk
# Input = det brevet vejer
# Output er prisen for at sende

print('Tak, fordi du vælger at sende dit brev med os.')
print('Hvad vejer dit brev i gram?')
gram = input()
vand = float(gram) *0.24
print('Dit brev koster ' + str(vand) + ' dkk at sende.')