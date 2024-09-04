# Information from the user #
#**Learning objectives**
#
#After this section:
#
#* You will know how to write a program which uses input from the user
#* You will know how to use variables to store input and print it out
#* You will be able to combine strings



## Live Demo ##
#
# Input from user
#name = input("What is your name? ")
#print("Hi there, " + name)
#
#
# Talk about Variables
#   * Note python is untyped and loose
#
#
# Reference a Var
#name = input("What is your name? ")
#print("Hi, ")
#print(name)
#print("!")
#print(name + " is quite a nice name.")
#
#
# Concat w/ +
#name = input("What is your name? ")
#print("Hi " + name + "! Let me make sure: your name is " + name + "?")
#
#
# Multiple Input
#name = input("What is your name? ")
#email = input("What is your email address? ")
#nickname = input("What is your nickname? ")
#print("Let's make sure we got this right")
#print("Your name: " + name)
#print("Your email address: " + email)
#print("Your nickname: " + nickname)
#
#
# Overriding Input
#name = input("What is your name? ")
#print(name)
#name = input("What is another name? ")
#print(name)






## Problem 1 ##
#Please write a script that: 
# - Asks for the user's name and then prints it twice, on two consecutive lines.

name = input ("Hey! What's your name?\n")

print ("Hey "+name+", nice to meet you!")
print (name+" is a cool name.")



## Problem 2 ##
#Please write a script that: 
# - Asks for the user's name
# - Prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, 
# - another between the two names and a third one at the end of the line.

name = input ("Hi, tell me your name!\n")
print ("!"+name+"!"+name+"!")



## Problem 3 ##
#Please write a script that: 
# - Asks for the user's name and address. 
# - The program should also print out the given information, as follows:
#   - Sample output
#   - First name: Steve
#   - Last name: Sanders
#   - Street address: 91 Station Road
#   - City and postal code: Folsom CA, 95630

name = input ("Hey, sorry, tell me your name again?\n")
address = input ("And tell me your adress?")

print (name + "\n" + address + ", Folsom CA, 95630")



## Problem 4 ##
#Please write a script that: 
# - Asks for 3 words 
# - Puts the words together with dashes and print that out

word1 = input ("Give me a word.\n")
word2 = input ("Give me another.\n")
word3 = input ("Give me one more.\n")

print (word1 + "-" + word2 + "-" + word3)



## Problem 5 ##
#Please write a script that: 
# - Asks for a name and a year
# - Prints out a short story that uses that information
# Sample output:
#Please type in a name: Mary
#Please type in a year: 1572
# ----------------------------------------------
#Mary is a valiant knight, born in the year 1572. 
#One morning Mary woke up to an awful racket: a dragon was approaching the village. 
#Only Mary could save the village's residents.

Askforaname = input ("Give me a name\n")
Askforacity = input ("Give my the name (whether fake or real) of a city\n")

print ("In the city of " + Askforacity + " lived a girl named " + Askforaname + ".")
print (Askforaname + " decided to uncover the truth about the mystery about the murder " + "\n" +  "that happened five years ago in " + Askforacity + ".")
print ("So, " + Askforaname + " and her friend found out the truth, yay")