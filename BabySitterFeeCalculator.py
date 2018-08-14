#!/usr/bin/env python
import datetime

class BabySitterFeeCalculator:
    """
    This class will calculate the nightly charge of a babysitter who:

    starts no earlier than 5:00PM
    leaves no later than 4:00AM
    gets paid $12/hour from start-time to bedtime
    gets paid $8/hour from bedtime to midnight
    gets paid $16/hour from midnight to end of job
    gets paid for full hours (no fractional hours)
    """
    # [ Internals ]
    def _calculate_difference_between_hours(self, endTime, initialTime):
        """Return the difference in hours between two datetimes."""
        latestTime = datetime.datetime.combine(datetime.date.today(), endTime)
        earlierTime = datetime.datetime.combine(datetime.date.today(), initialTime)
        difference = latestTime - earlierTime
        return difference.total_seconds() / 3600


    # [ Main ]
    def calculateFeeFromStartToBedtime(self, startTime, bedTime=0):
        """
        Given valid start time and bed time calculate the amount of the fee.
        The default value for bedtime is midnight.
        The rate for this time period is $12/hr.
        """

        start = datetime.time(hour=startTime)
        if start < datetime.time(hour=17):
            raise Exception('The start time can not be before 5pm!')
        end = datetime.time(hour=bedTime)
        return self._calculate_difference_between_hours(end, start) * 12



FeeCalculator = BabySitterFeeCalculator()
