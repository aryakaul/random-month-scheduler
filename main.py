#!/bin/python

import datetime
import calendar

def get_num_weekends(year, month, monthrange):
    num = 0
    for days in range(1,monthrange[1]+1):
        x = calendar.weekday(year, month, days)
        if x > 4:
            num += 1
    return num

def select_days(month, weekend_scaling, avg_events):
    curr_year = datetime.datetime.now().year
    range_in_given_month = calendar.monthrange(curr_year,month)
    num_weekends = get_num_weekends(curr_year,month,range_in_given_month)
    print(num_weekends)
    for days in range(1,range_in_given_month[1]+1):
        x = calendar.weekday(curr_year, month, days)

def main():
    select_days(2,2,3)
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
    print("Month chosen: %s" % calendar.month_abbr[month_chosen])

    while True:
        numeventsplanned = 1

        name = input("\nName of recurring event #%s? \n" % numeventsplanned)

        eventnumpermonth = None
        while eventnumpermonth == None:
            eventnumpermonth = input(
                "\nHow many of event #%s per month on average? \n" % numeventsplanned
            )
            try:
                eventnumpermonth = int(eventnumpermonth)
                if eventnumpermonth < 1:
                    raise Exception
            except:
                print("Invalid option. Choose a valid natural number > 1\n\n")
                eventnumpermonth = None

        """
        other_events_possible_bool = None
        while other_events_possible_bool == None:
            other_events_possible_bool = input(
                "\nAllow other events on the same day? [y/n]\n"
            )
            try:
                if other_events_possible_bool not in ["y", "n"]:
                    raise Exception
                else:
                    if other_events_possible_bool == "y":
                        other_events_possible_bool = True
                    else:
                        other_events_possible_bool = False
            except:
                print("Invalid option. Please choose 'y' or 'n'\n\n")
                other_events_possible_bool = None
        """

        weekend_scaling = None
        while weekend_scaling == None:
            weekend_scaling = input(
                "\nHow much more likely do you want to do this event on a weekend as opposed to a weekday? \n" % eventprob_weekend
            )
            try:
                weekend_scaling = float(weekend_scaling)
                if weekend_scaling < 0:
                    raise Exception
            except:
                print("Invalid option. Choose a rational number > 0\n\n")
                weekend_scaling = None


if __name__ == "__main__":
    main()
