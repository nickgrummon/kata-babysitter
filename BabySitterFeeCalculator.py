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


    # [ Main ]
    def calculateFeeFromStartToBedtime(self, startTime, bedTime):
        """Given valid start time and bed time calculate the amount of the fee."""
        start = datetime.time(hour=startTime)
        if start < datetime.time(hour=17):
            raise Exception('The start time can not be before 5pm!')


FeeCalculator = BabySitterFeeCalculator()
