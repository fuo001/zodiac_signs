#!/usr/bin/env python3


import requests
import json
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import zodiac_sign
import time
import os

def main():

	os.system('cls')
	zs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

	print("What Party do Zodiac Signs align with?")
	time.sleep(2)
	print("Let's Find Out...")
	time.sleep(1)
	print(*zs, sep="\n")
	time.sleep(1)

	while(True):
		print("Enter a Zodiac Sign from above:")
		zodiac = input().lower().capitalize()

		while zodiac not in zs:
			print("\n")
			print("Not a Zodiac Sign")
			print("Enter a Zodiac Sign:")
			zodiac = input().lower().capitalize()

		print("Enter a Chamber (house or senate)")
		chamber = input().lower()

		while((chamber != "house") and (chamber != "senate")):
			print("\n")
			print("Enter either house or senate")
			chamber = input().lower()

		if(chamber == "house"):
			print("Enter a number from 102-155")
			congress = input().lower()
			while int(congress) not in range(102,156):
				print("\n")
				print("Enter a number from 102-155")
				congress = input()
		else:
			print("Enter a number from 80-115")
			congress = input()
			while int(congress) not in range(80,116):
				print("\n")
				print("Enter a number from 80-115")
				congress = input()

		headers = {"X-API-Key": "WWSGHLJjWxC2m9tznYILCKy1xtmkvnxxdo8nEBt8"}
		url = "https://api.propublica.org/congress/v1/{}/{}/members.json".format(congress,chamber)
		members = requests.get(url, headers=headers).json()

		results = members['results'][0]['members']

		while (not results):
			print("Sorry, the number you enter didn't bring any results.")
			print("Enter a different number from 102-155")
			congress = input()

			url = "https://api.propublica.org/congress/v1/{}/{}/members.json".format(congress,chamber)
			members = requests.get(url, headers=headers).json()
			results = members['results'][0]['members']

		demo = 0
		repub = 0

		for member in results:
			sign = zodiac_sign.sign(member['date_of_birth'])
			if (sign.lower().capitalize() == zodiac):
				if(member['party'] == 'D'):
					demo = demo + 1
				if(member['party'] == 'R'):
					repub = repub + 1

		ax = plt.figure().gca()
		ax.yaxis.set_major_locator(MaxNLocator(integer=True))
		plt.bar(['Democrat','Republican'], [demo,repub])
		plt.xlabel('Party')
		plt.ylabel('Number of Members')
		plt.title(zodiac.capitalize())
		plt.show()

		print("\nInteresting Right? Try again and see what you find out.")
		print("Hit Crtl + C then Enter to exit the program at anytime")
		time.sleep(1)


if __name__ == '__main__':
    main()
