import logging
import time
import datetime

from mixin import StringValidatorMixin


class Modifications(StringValidatorMixin):
    """
    Modifications of date and time
    """
    def __init__(self):
        super(Modifications, self).__init__()

    def calculate_date(self, date, days=0, months=0, years=0):
        """
        Adds `days`, `months`, and `years` to `date`.
        """

        days = self._as_integer(days)
        months = self._as_integer(months)
        years = self._as_integer(years)

        change = datetime.timedelta(days=days)
        logging.info("Change: {}".format(change))
        if isinstance(date, datetime.date):
            date = date + change
        else:
            try:
                date = datetime.date(year=int(date[:4]), month=int(date[5:7]), day=int(date[8:10]))
                date = date + change
            except:
                raise ValueError("Expected a date with format YYYY-MM-DD got '{}'".format(date))
        logging.info("Date: {}".format(date))
        if months or years:
            months = months + date.month
            years = years + date.year
            if months > 12:
                years += months / 12
                months = months % 12
            elif months < 1:
                years += months / 12 if months else -1
                months = months % 12 if months else 12
            date = date.replace(year=years, month=months)
        logging.info("Date in iso format: {}".format(date.isoformat()))
        return date.isoformat()

    def timestamp_to_date(self, timestamp, format='%Y-%m-%d'):
        """
        Converts a timestamp in MS resolution to a string date in the form YYYY-MM-DD
        """
        timestamp = self._as_integer(timestamp)
        if timestamp < 0:
            raise ValueError('Timestamp cannot be negative')
        return datetime.datetime.fromtimestamp(timestamp / 1000).strftime(format)

    def date_to_timestamp(self, date, format='%Y-%m-%d'):
        """
        Converts a date string in the given format to a MS resolution timestamp
        """
        if isinstance(date, bool) or isinstance(date, int) or date is None:
            raise TypeError('Date is not a string')
        try:
            datetime.date(year=int(date[:4]), month=int(date[5:7]), day=int(date[8:10]))
        except:
            raise ValueError("Expected a date with format YYYY-MM-DD got '{}'".format(date))
        try:
            return int(time.mktime(datetime.datetime.strptime(date, format).timetuple())) * 1000
        except:
            raise ValueError('Year cannot be under 1970')

    def increment_one_day(self, date):
        """
        Increments a YYYY-MM-DD formatted date one day
        """
        return self.timestamp_to_date(self.date_to_timestamp(date) + 86400000)

    def decrement_one_day(self, date):
        """
        Decrements a YYYY-MM-DD formatted date one day
        """
        return self.timestamp_to_date(self.date_to_timestamp(date) - 86400000)
