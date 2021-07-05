from controller import clear as clr
import re
import datetime

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
            if not re.match("[a-zA-ZÀ-ÿ-. ]", input_name):
                print("\nInvalid Input, Please enter only letters (a-z)")
            else:
                return input_name
        except TypeError:
            print("\nInvalid Input, Please enter only letters (a-z)")

def gender_input(input_name):
    print(""" \n[1] Female \n[2] Male """)
    input_name = int_input(f"\n\n Please Choose {input_name}")
    while input_name > 0:
        if input_name == 1:
            return 'Female'
            break
        elif input_name == 2:
            return 'Male'
            break
        else:
            check_range(input_name, 1-2)
            gender_input(input_name)
            break 

def date_input(input_name):
    input_name = input(f"\n\nPlease Enter {str(input_name.capitalize())} (dd/mm/yy) : ")
    while True:
        try:
            datetime.datetime.strptime(input_name, "%d/%m/%y")
            return input_name
            break
        except ValueError:
            print("\nThis is the incorrect date format. It should be DD/MM/YY")

            return date_input('birthday')

def rank_input(input_name):

    while True:
        try:
            input_name = int(input(f"\nPlease Enter {input_name} Number : "))
            return input_name
        except ValueError:
            print("\nInvalid Input, Please enter a number")