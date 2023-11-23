from datetime import *
class DateRangeIterable:
    """An iterable that contains its own iterator object."""
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date
    def __iter__(self):
        print("__iter__")
        return self
    def __next__(self):
        print("__next__")
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today
    
if __name__ =="__main__":
    for day in DateRangeIterable(date(2018,1,1), date(2018, 1, 5)):
        print(day)