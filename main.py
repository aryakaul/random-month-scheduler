#!/bin/python

import datetime
import calendar
import numpy as np
import re
import random
import argparse
import sys
import os
# from loguru import logger


def parse_args(args):
    parser = argparse.ArgumentParser(description="check help!")
    parser.add_argument(
        "-i",
        "--input",
        dest="input",
        required=True,
        help="What task are you scheduling recurring monthly meetings for?",
        type=str,
    )
    parser.add_argument(
        "-y",
        "--year",
        dest="year",
        required=False,
        help="Year we are scheduling recurring events for",
        type=int,
    )
    parser.add_argument(
        "-m",
        "--month",
        dest="month",
        required=False,
        help="Month we are scheduling recurring events for",
        type=int,
    )
    parser.add_argument(
        "-n",
        "--number",
        dest="number",
        required=True,
        help="Mean number of times you would like to do this event/month",
        type=int,
    )
    parser.add_argument(
        "-s",
        "--std",
        dest="std",
        required=False,
        help="Standard deviation from the mean of the number of times to do \
        event/month",
        type=float,
    )
    parser.add_argument(
        "-w",
        "--weekdays",
        dest="weekdays",
        required=False,
        nargs='+',
        help="Which weekdays to include in set dates. Useful if you only want \
        to schedule an event for the weekend. Monday - 0 and Sunday - 6. For \
        example, if I only want to schedule events for the middle of the week,\
        then I could type -w 0 1 2 3 4",
        type=int,
    )
    return parser.parse_args()


def shuffle_dates(year, month, pass_weekdays=None):
    cal = calendar.Calendar(calendar.monthrange(year, month)[1])
    days = list(cal.itermonthdays2(year, month))
    days = list(filter(lambda day: day[0] != 0, days))
    if pass_weekdays is not None:
        pass_days = []
        for i in days:
            if i[1] in pass_weekdays:
                pass_days.append(i)
        days = pass_days
    random.shuffle(days)
    return days

def pick_dates(days, number, std=None):
    if std is not None:
        num_picks = int(np.random.normal(number, std, 1)[0])
        # logger.info("Number of events this month: %s" % num_picks)
    else: num_picks = number
    if num_picks > len(days):
        logger.warning("The number of picked days (%s) is larger than the \
                       # number of passing days (%s). Choosing all passing days"\
                       # % (num_picks, len(days)))
        return days
    return days[:num_picks]

def print_calendar(days, month, year):
    month_cal = calendar.month(year, month)
    # date = datetime.date.today().day.__str__().rjust(2)
    for i in days:
        rday  = ('\\b' + str(i[0]) + '\\b').replace('\\b ', '\\s')
        rdayc = "\033[7m" + str(i[0]) + "\033[0m"
        month_cal = re.sub(rday,rdayc,month_cal)
    print(month_cal)

def main():
    args = parse_args(sys.argv[1:])

    # first pick the month and date that we're working with
    if args.year == None:
        year_chosen = datetime.datetime.now().year
    else:
        year_chosen = args.year

    if args.month == None:
        month_chosen = datetime.datetime.now().month
    else:
        month_chosen = args.month
        if month_chosen > 12 or month_chosen < 1:
            print("Invalid month chosen: %s" % month_chosen)
            raise Exception
    # logger.info(
        # "Picking dates for: %s in %s" % (calendar.month_name[month_chosen], \
                                         # year_chosen)
    # )

    # shuffle dates in the month
    shuffled_dates = shuffle_dates(year_chosen, month_chosen, args.weekdays)

    # pick dates
    picked_dates = pick_dates(shuffled_dates, args.number, args.std)

    # output chosen dates
    print("%s is scheduled for:" % args.input)
    print_calendar(picked_dates, month_chosen, year_chosen)


if __name__ == "__main__":
    main()
