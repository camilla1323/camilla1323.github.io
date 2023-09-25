
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

print('Which country do you live in?') # ask what country they are from
myCountry = input()
print('What a lovly country you live in ' + myName + '. ' + myCountry + ' is a beautiful country.')

print('What city do you live in?') # ask what city they live in
myCity = input()
print('Sounds like a lovely city to live in.')

print('Name one thing you like to do in ' + myCity + '.') # ask what they like to do in their city
myFun = input()
print('That sounds like a fun activity to do in ' + myCity + '.')

print('How long can you hold your breath?') # ask how long they can hold their breath
myBreath = input()
print('That was not very long ' + myName + '. I can hold it for so much longer than YOU!!')

print('Guess you did not expect that, did you?')
myAnswer = input()
print('I feel sorry for you ' + myName + '. ' + myBreath + ' is not a very long time to hold your breath! Loser.')

print('Want to tell me something?')
myYes=input()
print('Loser.')

print('What is your favourite number?')
myNumber = input()
print('What a cool number, mine is ' + str(int(myNumber) + 11) + ' .')
