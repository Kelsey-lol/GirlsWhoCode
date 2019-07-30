#imports the ability to get a random number (we will learn more about this later!)
from random import *
print ("Which fruit do you get?")
#Create the list of words you want to choose from.
aList = ["Strawberry", "Blueberry", "Resberry", "Cherry", "Apple","Banana","Grape", "Watermelon","None"]

#Generates a random integer.
aRandomIndex = randint(0, len(aList)-1)
print (aList [aRandomIndex])
