#Dette program veksler dkk til euro
# 1dkk = 0,13 euro
# 7,5 dkk = 1 euro
# Kan ikke veksle fra 3 dkk og ned
# dkk*0.13*1.02

while True:
  print("Hello, want some information about currency? Dkk to euro. You can only say 'Yes'.")
  Yes = input()
  if Yes != 'Yes':
    break
  
  print('1.0. dkk = 0.13 euro, 7.5 dkk = 1 euro')
  while True:
    print('How many dkk do you wish to exchange to euro?')
    dkk = float(input())
    if dkk <= float(3.0):
        print('hello')
        break
    else:
       print(float(dkk) *0.13*1.02 )
       print('Enjoy your money.')
       break





