# encoding:utf-8
# logic for dayCalc kivy framework application

# not implemented, to be refactored or deleted

class DayCalcDateValidation():

    def validate(self, date):
        # date is represented as list [year, month, day]
        if all(d > 0 for d in date):
            if self.cal.is_leap(date[0]):
                daysOfMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            else:
                daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if date[1] <= 12 and date[2] <= daysOfMonths[date[1]-1]:
                return True
        return False

    def validate_date_sequence(self, dates):
        print('Rcvd for validation: {}'.format(dates))
        year1, month1, day1, year2, month2, day2 = dates
        print('y1: {}, m1: {}, d1: {}, y2: {}, m2: {}, d2: {}'.format(year1, month1, day1, year2, month2, day2))
        if (year1 < year2) or (year1 == year2 and month1 < month2) or (year1 == year2 and month1 == month2 and day1 <= day2):
            return True
        return False
