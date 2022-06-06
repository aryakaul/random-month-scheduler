# random-month-scheduler

<h3 align="center"><img src="https://i.stack.imgur.com/ww8c0.png" width="700px"></h3>
<p align="center"> 🗓️ - live RaNDomLy </p>

this is a silly application to randomly schedule recurring events for a given month.

### how do i use?

```
git clone https://github.com/aryakaul/random-month-scheduler.git
python main.py -h
usage: main.py [-h] -i INPUT [-y YEAR] [-m MONTH] -n NUMBER [-s STD] [-w WEEKDAYS [WEEKDAYS ...]]

Schedule random recurring events in a given month!

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        What task are you scheduling recurring monthly meetings for?
  -y YEAR, --year YEAR  Year we are scheduling recurring events for
  -m MONTH, --month MONTH
                        Month we are scheduling recurring events for
  -n NUMBER, --number NUMBER
                        Mean number of times you would like to do this event/month
  -s STD, --std STD     Standard deviation from the mean of the number of times to do event/month
  -w WEEKDAYS [WEEKDAYS ...], --weekdays WEEKDAYS [WEEKDAYS ...]
                        Which weekdays to include in set dates. Useful if you only want to schedule an event
                        for the weekend. Monday - 0 and Sunday - 6. For example, if I only want to schedule
                        events for the middle of the week, then I could type -w 0 1 2 3 4
```

### how does it work?
Let's say I wanted to randomly exercise ~8 days sometime during January 2050. But I also didn't want to exercise on Sundays. I would run the command:
`python main.py -i Exercise -y 2050 -m 01 -n 8 -w 0 1 2 3 4 5` This command shuffles all the non-Sunday days in January 2050 and returns the top 8 days back to me. Let's now say that I didn't want to always have exactly 8 days of exercise, but instead I wanted to have on average 8 days but with a standard deviation of 3 days. I would then add the flag `-s 3`. This would sample from a normal distribution with a mean of 8 and a std. deviation of 3 (denoted X) and then return the top X days from that week. 
