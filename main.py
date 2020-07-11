
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

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

todays_file = f'{short_date}_gift_card_numbers.csv'
# todays_file = f'gift_card_numbers.csv'

if Path(todays_file).is_file():
    print ("File exist")
else:
    print ("File not exist")


if __name__ == "__main__":


    while True:
        try:
            # GC = getpass.getpass(prompt='Please swipe a Gift Card: ')
            GC = input("Please swipe a Gift Card: ")
        except Exception as error:
            print('Nuts something went wrong' , error)
        else:
            if (GC == "exit"):
                sys.exit(0)
            else:
                print(GC)
                card_split = GC.split('~')
                card_1_r= card_split[1].split('^')
                card_1 = card_1_r[0][1:]
                card_2 = card_split[2].split('=')[0]
                card_list = []
                card_list.append(card_1)

                if (card_1 != card_2):
                    print('sorry please swipe again -> I didn\'t quite get that.....')
                else:
                    print(f"successfully extracted card number: {card_1}")
                    append_list_as_row(todays_file,card_list)
                    

