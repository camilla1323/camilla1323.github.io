
# This program says hello and asks for my name

print ('Hello, world')
print ('What is your name?') # ask for their name

myName = input()

print ('It is good to meet you, ' + myName)

print ('The length of your name is: ')
print (len(myName))

print('What is your age?')    # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

print('What is your favourite color?') # ask for their favourite color
myFavouriteColor = input()
print(myFavouriteColor + ' is a lovely and wonderful color ' + myName)

print('What is your favourite cake?') # ask for their favourite cake
myFavouriteCake = input()
print('Such a wonderful choice ' + myName + '. ' + myFavouriteCake + ' is delicious.')
