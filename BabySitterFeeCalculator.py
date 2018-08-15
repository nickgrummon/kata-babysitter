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
    def __init__(self):
        self.today = datetime.datetime.today()

    # [ Internals ]
    def _calculate_difference_between_datetimes(self, latestDateTime, initialDateTime):
        """Return the difference in hours between two datetimes."""
        endTime = datetime.datetime.combine(latestDateTime.date(), latestDateTime.time())
        earlierTime = datetime.datetime.combine(initialDateTime.date(), initialDateTime.time())
        difference = endTime - earlierTime
        return difference.total_seconds() / 3600


    # [ Main ]
    def calculateFeeFromStartToBedtime(self, startTime, bedTime=0):
        """
        Given valid start time and bed time calculate the amount of the fee.
        The default value for bedtime is midnight.
        The rate for this time period is $12/hr.
        """
        if startTime < 17:
            raise Exception('The start time can not be before 5pm!')
        startDateTime = datetime.datetime(self.today.date().year, self.today.date().month, self.today.date().day, hour=startTime)
        endDateTime = datetime.datetime(self.today.date().year, self.today.date().month, self.today.date().day, hour=bedTime)
        return self._calculate_difference_between_datetimes(endDateTime, startDateTime) * 12


    def calculateFeeFromBedtimeToMidnight(self, bedTime):
        """
        Given bed time, calculate the amount of the fee between bed time and midnight.
        The rate for this time period is $8/hr.
        """
        bedDateTime = datetime.datetime(self.today.date().year, self.today.date().month, self.today.date().day, hour=bedTime)
        midnightDateTime = datetime.datetime.combine(self.today.date(), self.today.min.time()) + datetime.timedelta(days=1)
        return self._calculate_difference_between_datetimes(midnightDateTime, bedDateTime) * 8


    def calculateFeeFromMidnightToEnd(self, endTime):
        """
        Given end time, calculate the amount of the fee between midnight and the end of the job.
        The rate for this time period is $16/hr.
        """
        if 17 > endTime > 4:
            raise Exception('The end time can not be after 4am!')
        endDateTime = datetime.datetime(self.today.date().year, self.today.date().month, self.today.date().day, hour=endTime)
        midnightDateTime = datetime.datetime.combine(self.today.date(), self.today.min.time()) + datetime.timedelta(days=1)
        if endTime < 17:
            endDateTimeDelta = datetime.datetime.combine(endDateTime.date(), endDateTime.time()) + datetime.timedelta(days=1)
            return self._calculate_difference_between_datetimes(endDateTimeDelta, midnightDateTime) * 16
        return self._calculate_difference_between_datetimes(midnightDateTime, endDateTime) * 16


FeeCalculator = BabySitterFeeCalculator()
