# random-month-scheduler

<h3 align="center"><img src="https://i.stack.imgur.com/ww8c0.png" width="700px"></h3>
<p align="center"> 🗓️ - live RaNDomLy </p>

this is a silly application to randomly schedule recurring events for a given month.

### how do i use?

```
git clone https://github.com/aryakaul/random-month-scheduler.git
python main.py
```
then follow the prompts.

### how does it work?

let's say that I wanted to schedule recurring 'random acts of kindness' for January 2050. this is the calendar for that month:

```
    January 2050
Su Mo Tu We Th Fr Sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
```

let's say that I wanted to commit an average of 5 random acts of kindness for this month, let's also say that I wanted to be twice as likely to do one of these acts on a weekend as opposed to a weekday. within this month, there are 10 days that fall on weekends, and 21 days that fall on weekdays. I solve the following system of linear equations for p and q.

```
21p + 10q = 5
2p - q = 0
```

p represents the probability of scheduling a random act of kindness on a weekday, and q represents the probability of scheduling a random act of kindess on a weekend. I then run bernoulli trials for each day of the given month with the calculated probability of success, and report the outcome. 

