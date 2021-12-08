"""
⚝ COURSE: ICT 2130 | PYTHON PROGRAMMING | FALL 2021
⚝ Instructor: Mr. Fru Emmanuel

*******************************************************
⚝ ASSIGNMENT: PRINTING STAR PATTERNS
*******************************************************

⚝ AUHTOR: BAIMAM BOUKAR JEAN JEAN JACQUES
⚝ MATRICULE: ICTU20201685
⚝ EMAIL: baimamboukar@gmail.com
⚝ GITHUB: github.com/baimamboukar
⚝ WHATSAPP: wa.me/+237690535759

*******************************************************
DESCRIPTION: This program is written to print star patterns using nested loops
"""

# [FUNCTION DEFINITION]


def star_pattern(n):

    # This first loop handles the number of rows that will be printed
    for i in range(0, n):
        # The second loop handles the number of stars that will be printed in each row
        # Note that the values are changing according to the first loop
        for j in range(0, i + 1):
            # printing stars
            print(" * ", end="")

        # this statement ends line after each row
        print()


# This is another easier way to print star patterns
def print_star_pattern(n):
    for i in range(0, n):
        print("*" * i)


# [ DRIVER CODE ]: The programm starts here

n = int(input("Enter the number of rows: "))
star_pattern(n)
