#A simple stock tracker that calculates total investment based on manually defined stock prices.

stocks = { "ASL": 145.50, "KBM": 278.30, "TRX": 89.75,  "NVD": 512.40, "ZYN": 63.20, "QRT": 341.10, "LMP": 120.00, "VEX": 77.85, 
            "HGT": 256.60, "PRL": 98.45,  "DYN": 410.25, "XTO": 185.90, "BLU": 54.70, "KOR": 299.99, "MTR": 132.15 }

import csv

ch = 'Y'

while ch.upper()=='Y':
    investor_name = str(input("Enter your name : "))            #all 3 inputs from the user
    stock_name = str(input("Enter the stock's name: "))
    stock_quantity = float(input("Enter the quantity : "))

    if stock_name.upper() in stocks.keys():                     
        investment_value = stocks[stock_name.upper()] * stock_quantity      #calculation of the total investment value
        print("Your investment value is : " , investment_value )            #displaying the total investment value

        with open("Investment_values.csv" , 'a') as F:       #adding the info(investor's name , stock's name and it's quantity) to another csv file
            writer = csv.writer(F)
            writer.writerow([investor_name, stock_name.upper(), stock_quantity, investment_value])

    else:
        print("Not found!")
    
    ch = str(input("Would you like to enter again? Y/N : "))
    
