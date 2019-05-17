# zodiac_signs
This program allows you to see the number of congress members in a specific party who have a specific zodiac sign.

To run this program, make sure to have project.py and zodiac_sign.py int he same folder.

When you run the program, it will give you a list of zodiac sign to choose from.
If you type in something that is not there it will tell you that is not a zodiac sign and ask again until a sign from the list is given. It is not case sensitive, so whether all caps or random capatilization, it will take it as long as the sign is spelled correctly.

Then it will ask for you to type in a chamber, either house or senate. Same as above, it will only take either house or senate and can handle any type of casing.

Depending on whether house or senate is typed in you will type in a number within the range given. If it is outside of the range it will ask again until it get a nuber with the range. It can only take numbers, strings will cause the program to crash. 

Depending on the number you type in, it will take that number and the chamber you selected and make a request to propublica and get back a dictionary of all members. There are some numbers that cause the dictionary of members to be empty so if it is empty the program will tell you that and have you retype in a number. (102 is the best number to use for house) 

The program will then go through each member and look at there date of birth and call a function from the zodiac_sign program to determine their zodiac sign. if that sign matches the one selected from before, that member's party affilication will be checked and that member will be counted for either Democrat of Republican. There are some member who's date of birth are not noted so the zodiac_sign program ignores them.

Then a bar graph of how many of a zodiac sign is a Democrat or Republican will be printed.

After closing the window of the bar graph the program will prompt you continue which starts the program over again.

To exit, hit ctrl + c and then hit enter.
