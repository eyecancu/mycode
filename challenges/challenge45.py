#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

NE_animals= farms[0]["agriculture"]

for x in NE_animals:
     print(x)

user_choice = input("Choose a farm (NE Farm, W Farm, or SE Farm): ")

for farm in farms:
     if farm["name"] == user_choice:
        agriculture = farm["agriculture"]

        print(f"Plants/Animals raised on {user_choice}:")
        for item in agriculture:
            print(item)
        break
else:
    print("Invalid farm choice.")