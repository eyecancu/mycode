#!/usr/bin/env python3

def main():

    #ask question 
    print("Which character do you want to know about?\n" "(Starlord, Mystique, Hulk)\n ")
    char_name = input()
    print("What statistic do you want to know about?\n" "(real name, powers, archenemy)\n ")
    char_stat = input()

    marvelchars = {
    "Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

    "Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

    "Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }
    result = marvelchars.get(char_name).get(char_stat)

    print(f"{char_name}'s {char_stat} is: {result}")

main()    