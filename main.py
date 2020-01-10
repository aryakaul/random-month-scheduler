#!/bin/python

import datetime
import calendar


def main():
    print("\n\nWelcome. \n")
    month_chosen = None
    while month_chosen == None:
        month_chosen = input(
            "What month would you like to plan recurring, random events for? Choose between 01-12. \n"
        )
        try:
            month_chosen = int(month_chosen)
            if month_chosen > 12 or month_chosen < 1:
                raise Exception
        except:
            print("Invalid option. Please choose a number between 1 and 12\n\n")
            month_chosen = None


if __name__ == "__main__":
    main()
