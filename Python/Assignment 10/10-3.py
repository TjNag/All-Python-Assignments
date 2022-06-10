metToCem = {'meter': 'm', 'centimeter': 'cm'}
cemToMet = {'centimeter': 'cm', 'meter': 'm'}

m = 6
cm = 750

metToCem['meter']=m
metToCem['centimeter']=metToCem['meter']*100

cemToMet['centimeter'] = cm
cemToMet['meter'] = cemToMet['centimeter']/100

print(metToCem)
print(cemToMet)