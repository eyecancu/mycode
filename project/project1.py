#!/usr/bin/env python 3
#BTC and ETH price tracker
#This script allows the user to check the price of Bitcoin or Ethereum for a specific year
#Charles De Sousa

import requests

def fetch_crypto_price(coin, year):             # fetches the price and year from the Coinbase API
    url = f"https://api.coinbase.com/v2/prices/{coin}-USD/spot?date={year}-01-01"   #  URL for the Coinbase API/ 
    response = requests.get(url)           # retrieve info from the JSON repsonse obtained from the API 
    data = response.json()                 
    price = data["data"]["amount"]
    return price

while True:
    # Prompting the user to choose a cryptocurrency
    crypto_choice = input("Choose a cryptocurrency: Bitcoin (BTC) or Ethereum (ETH): ")

    # Validating the user's choice
    if crypto_choice.upper() not in ["BTC", "ETH"]:                # Checks if the user chose btc or eth/converts to uppercase
        print("That's a shit coin!")                                # prints wrong answer if user doesn't use btc or eth
        continue

    while True:
        # Prompting the user to enter a year
        year = int(input("Enter a year between 2015 and 2023: "))

        # Validating the input year
        if year < 2015 or year > 2023:
            print("Follow instructions! Choose a year between 2015 and 2023!")
        else:
            # Fetching the price of the selected cryptocurrency for the chosen year
            crypto_price = fetch_crypto_price(crypto_choice.upper(), year)

            # Printing the price
            print(f"The price of {crypto_choice.upper()} in {year} is: ${crypto_price}")

            break  # Exit the inner loop and ask the question again

    # Asking the question again
    repeat = input("Do you want to check another cryptocurrency and year? (yes/no): ")
    if repeat.lower() != "yes":
        break
