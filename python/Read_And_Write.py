# ---------------------------------------------------------- #
#                                                            #
# Created by Flyxed (5182996)   -    Last Updated 03/12/2021 #
#                                                            #
# ReadWrite - Simple practice program to allow a user to     #
# input a students name and the score they received, which   #
# will be stored into a file and later can be read by user   #
# choice.                                                    #
#                                                            #
# Involves error checking through both the use of 'if'       #
# statements and 'try' and 'except' blocks.                  #
#                                                            #
#                                                            #
# ---------------------------------------------------------- #


# ------------------------ IMPORTS ------------------------- #

# Used for the 'sleep()' function.
from time import sleep 

# --------------------- END OF IMPORTS --------------------- #



# FUNCTIONS

def student_score():

    # Making 'name' and 'score' global variables so they are usable outside of this function.
    global name
    global score
    check = 0

    # Take the user input and store it as 'name'.
    name = input("Please insert the name of the student.\nNAME: ")

    # ERROR CHECKING - Ensuring inputs are only accepted if integers, and the integer is between 1-100.
    # Try statement has the check for being between 1-100 as this would be impossible to do with a string
    # value as we are converting 'score' to int.

    while check == 0:
        # Set check to 1 at the beginning as we are performing only invalidity checks. This will not stop the while loop
        # because while loops run the whole process, even if during the while loop the condition is changed to not be met.
        check = 1
        score = input("Please insert the score the student got.\nSCORE: ")
        # See if the program is able to perform the following if check, which is to see if the input, as an integer, is
        # between the values 1-100.
        try:
            # If 'score' is successfully converted to an integer value, and it is not between 1 and 100...
            if not 1 < int(score) < 101:
                # Print error message, set check to 0 so the while loop runs again.
                print("\nYou have input an invalid score. Scores must range from 1-100.\n")
                check = 0 
        # If we receive a ValueError (as 'score' cannot be set to integer)...
        except ValueError:
            # Print error message, set check to 0 so the while loop runs again.
            print("\nYou have inputted an invalid value. Make sure your input is solely numerical.\n")
            check = 0
    
    # Otherwise, the program will continue as no errors are met and therefore the input 

def user_choice():
    
    check = 0
    values = {'Y', 'N'}

    # ERROR CHECKING - Ensuring inputs are only accepted if the char 'y' or 'n'.
    # An if statement using 'choice.upper()' [converts the variable into it's uppercase equivalent, so 'y' turns into 'Y']
    # is used to check the users input to verify if they have used a valid character for their response.
    # If the user inputs an integer, string or invalid character, they will be forced back through the while loop until a
    # valid choice is made.

    while check == 0:
        choice = input("\nWould you like to read the file 'student_score.txt'? [Y/N]\nCHOICE: ")
        # If the user input is not 'Y' or 'N'...
        if choice.upper() not in values:
            #Output an error. Check is already 0 so no adjustment necessary.
            print("ERROR!\nYou have inputted an invalid choice. Please try again.")
        # If the user input is 'Y'...
        elif choice.upper() == 'Y':
            # Run 'read_file()' which is declared below, and set 'check' to 1 to break the while loop.
            print("Opening file...\n")
            check = 1
            read_file()
        # Otherwise, the user input must be 'N', therefore...
        else:
            # Close the program
            print("Closing...")
            check = 1

def append_file():

    # Show the user what process is currently undergoing.
    print("\nWriting to file 'student_score.txt'...")
    # Open the file 'student_score.txt' with permissions to append to it.
    f = open("student_score.txt", "a")
    # Print the name and score the student received in a readable format.
    # 'f' at the beginning of the string outside of the quotation marks allows us to use variables in the string
    # without the need of having to convert them to strings and use +'s and multiple quotation marks.
    # '\n' is a linebreak to keep the records in a line-by-line fashion.
    f.write(f"Name: {name} | Score: {score}\n")
    # Close the file.
    f.close()
    # Print a success message!
    print("Success!")

def read_file():

    # Open the 'student_score.txt' file with read permissions only.
    f = open("student_score.txt", "r")
    # Print the contents of the opened file.
    print(f.read())
    # Close the file.
    f.close()

def main():
# Creating a 'main' function which runs 'student_score', 'append_file' and 'user_choice' all through one function which we can call at a later point to run the program.
    student_score()
    append_file()
    user_choice()

main()
