# Text based adventure game

Move through rooms, talk to friends and defeat enemies.

## Play the game
Run main.py in python. In a given room, you have the following options. All commands are typed in the console:

a) move to a neighboring room, e.g. by typing `north`

b) type `talk` to talk to a character

c) Fight with a character by typing `fight`. You will be asked to type an item to fight.
Type an item, you have previously collected and you think is a weakness of your enemy.
You automatically collect items by visiting rooms. 

You win if you beat 2 opponents. You loose as soon as you loose one fight.

## Build your own game
You can build your own version of the game by writing your main method.
This repository contains the Character, Enemy, Friend, Item and Room classes.
These classes can be used to build up a simple, text-based adventure game. 
A documentation for each class can be found in the corresponding html files.

In case you do not immediately know how to reference the classes, I recommend having a look at the imports of my main method.

## Prerequisites

Runs under Python 2 and 3.

## Authors

* **Johannes Birk** - [Johannes Birk](https://github.com/Johannes1803)

## Acknowledgments
I wrote this code during the MOOC [Object-oriented Programming in Python: Create Your Own Adventure Game](https://www.futurelearn.com/courses/object-oriented-principles) 
on futurelearn.com. It was developed by the Rasberry Pi foundation and in particular lead instructor
Laura Sach.  