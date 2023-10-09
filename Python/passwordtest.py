while True:
  print('Hello, please enter your username.')
  username = input()
  if username != 'Camilla':
    continue
  
  while True:
    print('Hello Camilla, please enter the password. (It is the name of your cats)')
    password = input()
    if password == 'Mussi and Felix':
      print('Access granted, welcome back Camilla!')
    break

  