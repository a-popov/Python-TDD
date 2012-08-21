

class StringValidatorMixin(object):

    def _as_integer(self, string):
        """
        Determines whether a string is a number.
        """
        if string is None or isinstance(string, bool):
            raise TypeError("String is None or is a Boolean")
        try:
            return int(string)
        except ValueError:
            raise ValueError("String passed in is not a number")
