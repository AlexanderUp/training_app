# encoding:utf-8
# module wrapped into class to be used in dayCalc kivy application
# task from Udacity, Computer Science course, lesson 8-2
# ==============================================================================

# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

# ==============================================================================

# Some doubt exists in question of including first or last days in mentioned period.

# ==============================================================================

# daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# ==============================================================================

class LeapCalendar():

    def is_leap(self, year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def days_till_date(self, year, month, day):
        # count quantity of days passed since beginning of year
        total = 0
        if self.is_leap(year):
            daysOfMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for month in range(month-1):
            total += daysOfMonths[month]
        return total + day

    def same_year(self, year, month1, day1, month2, day2):
        return self.days_till_date(year, month2, day2) - self.days_till_date(year, month1, day1)

    def diff_year(self, year1, month1, day1, year2, month2, day2):
        total = 0 # days in entire years
        days_in_first_year = 0
        if self.is_leap(year1):
            days_in_first_year = 366 - self.days_till_date(year1, month1, day1)
        else:
            days_in_first_year = 365 - self.days_till_date(year1, month1, day1)
        for year in range(year1 + 1, year2):
            if self.is_leap(year):
                total += 366
            else:
                total += 365
        return total + days_in_first_year + self.days_till_date(year2, month2, day2)

    def daysBetweenDates(self, year1, month1, day1, year2, month2, day2):
        if year1 == year2:
            return self.same_year(year1, month1, day1, month2, day2)
        else:
            return self.diff_year(year1, month1, day1, year2, month2, day2)

    def validate(self, date):
        # date is represented as list [year, month, day]
        if all(d > 0 for d in date):
            if self.is_leap(date[0]):
                daysOfMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            else:
                daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if date[1] <= 12 and date[2] <= daysOfMonths[date[1]-1]:
                return True
        return False

    def validate_date_sequence(self, dates):
        year1, month1, day1, year2, month2, day2 = dates
        if (year1 < year2) or (year1 == year2 and month1 < month2) or (year1 == year2 and month1 == month2 and day1 <= day2):
            return True
        return False

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    a = LeapCalendar()
    for (args, answer) in test_cases:
        result = a.daysBetweenDates(*args)
        print('Test: {}'.format(args))
        print('Result: {}'.format(result))
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")

if __name__ == '__main__':
    print("*" * 20)
    test()
