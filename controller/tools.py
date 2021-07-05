from controller import clear as clr
import re

def check_range(input_name, ranger):
    while input_name not in range(ranger):
        clr.screen()
        ranger = ranger-1
        print(f"Enter a number between 1{ranger} please")
        break
    
def int_input(input_name):

    while True:
        try:
            input_name = int(input("\n\nOption : "))
            return input_name
        except ValueError:
            print("\nInvalid Input, Please enter a number")

def str_input(input_name):

    while True:
        try:
            input_name = input(f"\n\nPlease Enter {str(input_name.capitalize())} : ")
            if not re.match("[A-Z][a-z]", input_name):
                print("\nInvalid Input, Please enter only letters and capitalized name (a-z)")
            else:
                return input_name
        except TypeError:
            print("\nInvalid Input, Please enter only letters (a-z)")

def gender_input(input_name):

    pass    

def date_input(input_name):

    while True:
        try:
            input_name = str(input(f"\n\nPlease Enter {input_name.capitalize()} in DD-MM-YYYY Format : "))
            return input_name
        except ValueError:
            print(f"\n\n Invalid Input, Please enter a date (dd/mm/yyyy)")

def check_date(input):
    pass