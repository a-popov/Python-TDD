import logging
import datetime

from mixin import StringValidatorMixin


class Instances(StringValidatorMixin):
    """
    Instances of date and time
    """
    def __init__(self):
        super(Instances, self).__init__()

    def get_today_date(self, format="%Y-%m-%d"):
        """
        Returns the current date in the format of Year-Month-Day
        """
        try:
            now = datetime.datetime.now().strftime(format)
        except:
            raise ValueError("Expected a date with format YYYY-MM-DD got '{}'".format(format))
        logging.info("Time now is: %s" % now)
        return now
