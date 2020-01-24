#!/bin/python

import datetime
import calendar


def main():
    print("\n\nWelcome. \n")
    month_chosen = None
    while month_chosen == None:
        month_chosen = input(
            "What month would you like to plan recurring, random events for? [01-12] \n"
        )
        try:
            month_chosen = int(month_chosen)
            if month_chosen > 12 or month_chosen < 1:
                raise Exception
        except:
            print("Invalid option. Please choose a number between 1 and 12\n\n")
            month_chosen = None
    print("\nMonth chosen: %s" % calendar.month_abbr[month_chosen])

    while True:
        numeventsplanned = 1
        
        name = input("\nName of recurring event #%s? \n" % numeventsplanned)
        eventnumpermonth = None
        
        while eventnumpermonth == None:
            eventnumpermonth = input(
                "How many of these events per month on average? \n"
            )
            try:
                eventnumpermonth = int(eventnumpermonth)
                if eventnumpermonth < 1:
                    raise Exception
            except:
                print("Invalid option. Choose a valid natural number > 1\n\n")
                eventnumpermonth = None
        
        

if __name__ == "__main__":
    main()
