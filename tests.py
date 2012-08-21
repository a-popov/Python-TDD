import unittest

from instances import Instances
from modifications import Modifications


class InstancesTest(unittest.TestCase):

    def setUp(self):
        self.fixture = Instances()

    def test_get_today_date_works(self):
        today_date = self.fixture.get_today_date()

        year = today_date[0:today_date.find('-')]
        self.assertEqual(len(year), 4)
        self.assertEqual(year[0:3], '201')
        self.assertTrue(0 <= int(year[3]) and int(year[3]) <= 9)

        month = today_date[today_date.find('-') + 1: today_date.find('-') + 3]
        self.assertTrue(0 < int(month) and int(month) <= 12)

        day = today_date[today_date.find('-') + 4: today_date.find('-') + 6]
        self.assertTrue(0 < int(day) and int(day) <= 31)


class ModificationsTest(unittest.TestCase):

    def setUp(self):
        self.fixture = Modifications()

    def test_calculate_date_with_default_arguments_works(self):
        self.assertEqual(self.fixture.calculate_date('2001-02-03'), '2001-02-03')

    def test_calculate_date_with_days_argument_only_works(self):
        self.assertEqual(self.fixture.calculate_date('2001-02-03', days=13), '2001-02-16')

    def test_calculate_date_with_days_string_argument_only_works(self):
        self.assertEqual(self.fixture.calculate_date('2001-02-03', days='13'), '2001-02-16')

    def test_calculate_date_with_large_days_argument_only_works(self):
        self.assertEqual(self.fixture.calculate_date('2001-02-03', days=100), '2001-05-14')

    def test_calculate_date_with_large_days_string_argument_only_works(self):
        self.assertEqual(self.fixture.calculate_date('2001-02-03', days='100'), '2001-05-14')

    def test_calculate_date_with_months_argument_only_works(self):
        self.assertEqual(self.fixture.calculate_date('2001-02-03', months=3), '2001-05-03')

    def test_calculate_date_with_months_string_argument_only_works(self):
        self.assertEqual(self.fixture.calculate_date('2001-02-03', months='3'), '2001-05-03')

    def test_calculate_date_with_large_months_argument_only_works(self):
        self.assertEqual(self.fixture.calculate_date('2001-02-03', months=14), '2002-04-03')

    def test_calculate_date_with_large_months_string_argument_only_works(self):
        self.assertEqual(self.fixture.calculate_date('2001-02-03', months='14'), '2002-04-03')

    def test_calculate_date_with_years_argument_only_works(self):
        self.assertEqual(self.fixture.calculate_date('2001-02-03', years=3), '2004-02-03')

    def test_calculate_date_with_years_string_argument_only_works(self):
        self.assertEqual(self.fixture.calculate_date('2001-02-03', years='3'), '2004-02-03')

    def test_calculate_date_with_day_and_month_arguments_only_works(self):
        self.assertEqual(self.fixture.calculate_date('2001-02-03', days=100, months=14), '2002-07-14')

    def test_calculate_date_with_day_and_year_arguments_only_works(self):
        self.assertEqual(self.fixture.calculate_date('2001-02-03', days=100, years=3), '2004-05-14')

    def test_calculate_date_with_month_and_year_arguments_only_works(self):
        self.assertEqual(self.fixture.calculate_date('2001-02-03', months=14, years=5), '2007-04-03')

    def test_calculate_date_with_all_given_arguments_works(self):
        self.assertEqual(self.fixture.calculate_date('2001-02-03', days=100, months=14, years=5), '2007-07-14')

    def test_calculate_date_with_invalid_date_argument_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.calculate_date('bla')
        self.assertEqual(context.exception.message, "Expected a date with format YYYY-MM-DD got 'bla'")

    def test_calculate_date_with_integer_date_argument_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.calculate_date(2001 - 02 - 03)
        self.assertEqual(context.exception.message, "Expected a date with format YYYY-MM-DD got '1996'")

    def test_calculate_date_with_invalid_days_in_date_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.calculate_date('2012-01-70')
        self.assertEqual(context.exception.message, "Expected a date with format YYYY-MM-DD got '2012-01-70'")

    def test_calculate_date_with_invalid_days_argument_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.calculate_date('2001-02-03', days='Bla')
        self.assertEqual(context.exception.message, "String passed in is not a number")

    def test_calculate_date_with_boolean_days_argument_throws_error(self):
        with self.assertRaises(TypeError) as context:
            self.fixture.calculate_date('2001-02-03', days=True)
        self.assertEqual(context.exception.message, "String is None or is a Boolean")

    def test_calculate_date_with_invalid_months_argument_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.calculate_date('2001-02-03', months='Bla')
        self.assertEqual(context.exception.message, "String passed in is not a number")

    def test_calculate_date_with_boolean_months_argument_throws_error(self):
        with self.assertRaises(TypeError) as context:
            self.fixture.calculate_date('2001-02-03', months=False)
        self.assertEqual(context.exception.message, "String is None or is a Boolean")

    def test_calculate_date_with_invalid_years_argument_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.calculate_date('2001-02-03', years='Bla')
        self.assertEqual(context.exception.message, "String passed in is not a number")

    def test_calculate_date_with_boolean_years_argument_throws_error(self):
        with self.assertRaises(TypeError) as context:
            self.fixture.calculate_date('2001-02-03', years=True)
        self.assertEqual(context.exception.message, "String is None or is a Boolean")

    def test_calculate_date_with_none_as_date_argument_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.calculate_date(None)
        self.assertEqual(context.exception.message, "Expected a date with format YYYY-MM-DD got 'None'")

    def test_calculate_date_with_none_as_any_of_arguments_throws_error(self):
        with self.assertRaises(TypeError) as context:
            self.fixture.calculate_date('2001-02-03', days=None, months=None, years=None)
        self.assertEqual(context.exception.message, "String is None or is a Boolean")

    def test_timestamp_to_date_realstic_argument_works(self):
        self.assertEqual(self.fixture.timestamp_to_date(1350000000000), '2012-10-11')

    def test_timestamp_to_date_low_argument_works(self):
        self.assertEqual(self.fixture.timestamp_to_date(999), '1969-12-31')

    def test_timestamp_to_date_high_argument_works(self):
        self.assertEqual(self.fixture.timestamp_to_date(23500000000000), '2714-09-08')

    def test_timestamp_to_date_string_number_argument_works(self):
        self.assertEqual(self.fixture.timestamp_to_date('1350000000000'), '2012-10-11')

    def test_timestamp_to_date_negative_argument_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.timestamp_to_date(-12345678)
        self.assertEqual(context.exception.message, "Timestamp cannot be negative")

    def test_timestamp_to_date_empty_string_argument_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.timestamp_to_date('')
        self.assertEqual(context.exception.message, "String passed in is not a number")

    def test_timestamp_to_date_string_argument_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.timestamp_to_date('Time')
        self.assertEqual(context.exception.message, "String passed in is not a number")

    def test_timestamp_to_date_boolean_argument_throws_error(self):
        with self.assertRaises(TypeError) as context:
            self.fixture.timestamp_to_date(True)
        self.assertEqual(context.exception.message, "String is None or is a Boolean")

    def test_timestamp_to_date_none_argument_throws_error(self):
        with self.assertRaises(TypeError) as context:
            self.fixture.timestamp_to_date(None)
        self.assertEqual(context.exception.message, "String is None or is a Boolean")

    def test_date_to_timestamp_realistic_argument_works(self):
        self.assertEqual(self.fixture.date_to_timestamp('2012-10-11'), 1349928000000)

    def test_date_to_timestamp_low_argument_works(self):
        self.assertEqual(self.fixture.date_to_timestamp('1970-01-01'), 18000000)

    def test_date_to_timestamp_high_argument_works(self):
        self.assertEqual(self.fixture.date_to_timestamp('2700-01-01'), 23036590800000)

    def test_date_to_timestamp_invalid_year_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.date_to_timestamp('1969-12-31')
        self.assertEqual(context.exception.message, "Year cannot be under 1970")

    def test_date_to_timestamp_invalid_day_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.date_to_timestamp('2012-01-70')
        self.assertEqual(context.exception.message, "Expected a date with format YYYY-MM-DD got '2012-01-70'")

    def test_date_to_timestamp_invalid_argument_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.date_to_timestamp('bla')
        self.assertEqual(context.exception.message, "Expected a date with format YYYY-MM-DD got 'bla'")

    def test_date_to_timestamp_integer_argument_throws_error(self):
        with self.assertRaises(TypeError) as context:
            self.fixture.date_to_timestamp(123)
        self.assertEqual(context.exception.message, "Date is not a string")

    def test_date_to_timestamp_boolean_argument_throws_error(self):
        with self.assertRaises(TypeError) as context:
            self.fixture.date_to_timestamp(False)
        self.assertEqual(context.exception.message, "Date is not a string")

    def test_date_to_timestamp_empty_argument_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.date_to_timestamp('')
        self.assertEqual(context.exception.message, "Expected a date with format YYYY-MM-DD got ''")

    def test_date_to_timestamp_none_argument_throws_error(self):
        with self.assertRaises(TypeError) as context:
            self.fixture.date_to_timestamp(None)
        self.assertEqual(context.exception.message, "Date is not a string")

    def test_increment_one_day_works(self):
        self.assertEqual(self.fixture.increment_one_day('2012-10-11'), '2012-10-12')

    def test_increment_one_day_at_month_end_works(self):
        self.assertEqual(self.fixture.increment_one_day('2012-10-31'), '2012-11-01')

    def test_increment_one_day_at_year_end_works(self):
        self.assertEqual(self.fixture.increment_one_day('2012-12-31'), '2013-01-01')

    def test_increment_one_day_with_invalid_days_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.increment_one_day('2012-01-70')
        self.assertEqual(context.exception.message, "Expected a date with format YYYY-MM-DD got '2012-01-70'")

    def test_increment_one_day_with_invalid_string_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.increment_one_day('bla')
        self.assertEqual(context.exception.message, "Expected a date with format YYYY-MM-DD got 'bla'")

    def test_increment_one_day_integer_argument_throws_error(self):
        with self.assertRaises(TypeError) as context:
            self.fixture.increment_one_day(123)
        self.assertEqual(context.exception.message, "Date is not a string")

    def test_increment_one_day_boolean_argument_throws_error(self):
        with self.assertRaises(TypeError) as context:
            self.fixture.increment_one_day(False)
        self.assertEqual(context.exception.message, "Date is not a string")

    def test_increment_one_day_empty_argument_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.increment_one_day('')
        self.assertEqual(context.exception.message, "Expected a date with format YYYY-MM-DD got ''")

    def test_increment_one_day_none_argument_throws_error(self):
        with self.assertRaises(TypeError) as context:
            self.fixture.increment_one_day(None)
        self.assertEqual(context.exception.message, "Date is not a string")

    def test_decrement_one_day_works(self):
        self.assertEqual(self.fixture.decrement_one_day('2012-10-11'), '2012-10-10')

    def test_decrement_one_day_at_month_beginning_works(self):
        self.assertEqual(self.fixture.decrement_one_day('2012-03-01'), '2012-02-29')

    def test_decrement_one_day_at_year_end_works(self):
        self.assertEqual(self.fixture.decrement_one_day('2012-01-01'), '2011-12-31')

    def test_decrement_one_day_with_invalid_days_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.decrement_one_day('2012-01-70')
        self.assertEqual(context.exception.message, "Expected a date with format YYYY-MM-DD got '2012-01-70'")

    def test_decrement_one_day_with_invalid_string_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.decrement_one_day('bla')
        self.assertEqual(context.exception.message, "Expected a date with format YYYY-MM-DD got 'bla'")

    def test_decrement_one_day_integer_argument_throws_error(self):
        with self.assertRaises(TypeError) as context:
            self.fixture.decrement_one_day(123)
        self.assertEqual(context.exception.message, "Date is not a string")

    def test_decrement_one_day_boolean_argument_throws_error(self):
        with self.assertRaises(TypeError) as context:
            self.fixture.decrement_one_day(False)
        self.assertEqual(context.exception.message, "Date is not a string")

    def test_decrement_one_day_empty_argument_throws_error(self):
        with self.assertRaises(ValueError) as context:
            self.fixture.decrement_one_day('')
        self.assertEqual(context.exception.message, "Expected a date with format YYYY-MM-DD got ''")

    def test_decrement_one_day_none_argument_throws_error(self):
        with self.assertRaises(TypeError) as context:
            self.fixture.decrement_one_day(None)
        self.assertEqual(context.exception.message, "Date is not a string")
