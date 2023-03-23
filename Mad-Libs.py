"""
Description: Mad Libs word game, short stories with blank spaces that a player can fill in.
Author: Zuriel
"""

# The template for the story
#
#STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."
#
#print "Mad Libs has started."
#
#name = raw_input("Enter a name: ")
#adjective1 = raw_input("Enter adjective 1: ")
#adjective2 = raw_input("Enter adjective 2: ")
#adjective3 = raw_input("Enter adjective 3: ")
#
#verb1 = raw_input("Enter verb 1: ")
#
#noun1 = raw_input("Enter noun 1: ")
#noun2 = raw_input("Enter noun 2: ")
#
#animal = raw_input("Enter a animal: ")
#food = raw_input("Enter a food: ")
#fruit = raw_input("Enter a fruit: ")
#superhero = raw_input("Enter a superhero: ")
#country = raw_input("Enter a country: ")
#dessert = raw_input("Enter a dessert: ")
#year = raw_input("Enter a year: ")
#
#print (STORY % (name,adjective1,adjective2,animal,food,verb1,noun1,fruit,adjective3,name,superhero,name,country,name,dessert,name,year,noun2,))


# re written for Python 3 - to run in VScode
STORY = "This morning {name} woke up feeling {adj1}. 'It is going to be a {adj2} day!' Outside, a bunch of {animals} were protesting to keep {food} in stores. They began to {verb} to the rhythm of the {noun1}, which made all the {fruit} very {adj3}. Concerned, {name} texted {superhero}, who flew {name} to {country} and dropped {name} in a puddle of frozen {dessert}. {name} woke up in the year {year}, in a world where {noun2} ruled the world."

print("Mad Libs has started.")

name = input("Enter a name: ")
adj1 = input("Enter adjective 1: ")
adj2 = input("Enter adjective 2: ")
adj3 = input("Enter adjective 3: ")

verb = input("Enter verb 1: ")

noun1 = input("Enter noun 1: ")
noun2 = input("Enter noun 2: ")

fruit = input("Enter a fruit: ")

animals = input("Enter a animal: ")
food = input("Enter a food: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")

print(STORY.format(name=name, adj1=adj1, adj2=adj2, animals=animals, food=food, verb=verb, noun1=noun1, fruit=fruit, adj3=adj3, superhero=superhero, country=country, dessert=dessert, year=year, noun2=noun2))










