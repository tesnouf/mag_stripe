
import sys
import datetime
from csv import writer
import os
from pathlib import Path

# import getpass
## not using getpass so we can see when the string has been fully read

os.system('cls')

full_date = datetime.datetime.now()
short_date = full_date.strftime('%Y%m%d')
print(short_date)
print("Program to save Gift Card numbers to spreadsheet.")
print("swipe cards through reader and press enter to confirm")
print("types exit to quit the program.  your results will be saved to the desktop.")
print('------------------------------------------------------------------------------')

# def set_instructor_value():
#     ## set up a variable for the instructor


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def check_values(card_string_1, card_string_2, employee_id):
    c1 = card_string_1
    c2 = card_string_2
    if (c1 != c2):
        print('sorry please swipe again -> I didn\'t quite get that.....')
    else:
        print(f"successfully extracted card number: {c1}")
        c1 = '`'+ c1 ## numbers are too big for excel add ` infront to force conversion to text just in case
        card_list = [employee_id]
        card_list.append(c1)
        append_list_as_row(todays_file,card_list)

def parse_gc(gift_card_string):
    GC = gift_card_string
    card_split = GC.split('~')
    card_1_r= card_split[1].split('^')
    card_1 = card_1_r[0][1:]
    card_2 = card_split[2].split('=')[0]

    check_values(card_1 , card_2, employee_id)
    
    return 
    
def save_exit():

    ## prompt user for save location
    print(f'Saved File to: {os.getcwd()}')
    sys.exit(0)

    return


todays_file = f'{short_date}_gift_card_numbers.csv'
# todays_file = f'gift_card_numbers.csv'

if Path(todays_file).is_file():
    print ("File exist")
else:
    print ("File not exist")


if __name__ == "__main__":

    employee_id = 123456

    while True:
        try:
            # GC = getpass.getpass(prompt='Please swipe a Gift Card: ')
            
            GC = input("Please swipe a Gift Card: ")
        except Exception as error:
            print('Nuts something went wrong' , error)
        else:
            if (GC == "exit"):
                save_exit()
            elif (len(GC) == 6):
                employee_id = GC
                print(f'Updating Instructor Employee ID to: {employee_id}')
            else:
                parse_gc(GC)

                
                    

