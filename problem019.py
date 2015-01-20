# calendar
# index the days in a list
# index month lengths, special-case Feb
# skip to the first of each month, determine day-of-week

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

curr_day = 1
collect = []

for year in xrange(1901, 2001):
    for add in months:
        # check whether current day is a Sunday
        if curr_day == 6:
            collect.append((add, year))
        # check for leap year
        if add == 28:
            if (not year % 400) or (not year % 4 and year % 100):
                add += 1
        # skip to next month
        curr_day = divmod(curr_day + add, 7)[1]

print len(collect)