#!/usr/bin/env python3
'''Oh, so that's what docstrings are!!!
So, the user (you) will pick a number and
keep it in your head. The computer will guess
what your number is, and you will tell it
whether its guess was too high, too low, or
if the computer got it right. The commands
are documented in-game.'''

import random


def init():
	global lower, upper, i, user
	print('''The way this game works, you will think of a number.
The computer (me) will then try to guess that number.
After I guess, please tell me whether I was too high (type 'high'),
too low (type 'low'), or correct (type 'correct').
This program uses a binary search algorithm.

C)2023 Seth Wilding, Released under the MIT Open Source License''')


	print('Pick a number, Mr. User!')
	input('Press enter when you have thought of a number.')

	print('Okay, good. Your number should be between one and a power of ten.')
	lower=1
	print('Which power of ten is it less than? (e.g. 100 or 10000)')
	upper=int(input())
	i=0
	user=''
	return 0

def brokerules():
	print('Hey!')
	print('You were trying to trick me, weren\'t you!')
	print('Well, the joke is on you, because I am too smart for that!')
	print('Now, let\'s try this again from the beginning!')
	init()

def celebrate(i):
	print('Let\'s go! I\'m a genius!!!')
	print('And it only took me %d guesses!'%d)
	print('')
	print('Either that, or you cheated a little...')

#main
init()
while user!='correct':
	if lower>=upper:
		brokerules()
	guess=int(lower+(upper-lower)/2)
	print('I guess %d.'% guess)
	user=input()
	if user=='high':
		upper=guess
	elif user=='low':
		lower=guess
	elif user=='correct':
		celebrate(i)
	else:
		times=0
		while user!='correct' and user!='high' and user!='low':
			print('''I'm sorry, I don't understand that input.
If my guess was too high, type 'high'.
If my guess was too low, type 'low'.
If it was the right number, type 'correct'.''')
			print('My guess was %d.' % guess)
			if times>=5:
				print('Come on, was it really that hard to follow instructions?')
			user=input()
			times+=1
	i+=1

print('Thank you for playing! Please give me a good grade on this assignment!')
