#!/usr/bin/env python
import unittest
from BabySitterFeeCalculator import BabySitterFeeCalculator

class TestBabySitterFeeCalulator(unittest.TestCase):
    """Tests for the BabySitterFeeCalculator."""

    def testWhenANumberBeforeTheMinStartTimeIsPassedReturnError(self):
        """When the start time is before 5:00pm, an error should be returned."""
        feeCalculator = BabySitterFeeCalculator()
        with self.assertRaises(Exception) as context:
            feeCalculator.calculateFeeFromStartToBedtime(startTime=16, bedTime=22)
        self.assertTrue('The start time can not be before 5pm!' in context.exception)

    def testCalculateFeeFromStartToBedtimeWhenBedtimeIsBeforeMidnight(self):
        """When the start time is 5:00pm and bedtime is 10:00pm, calculate the correct fee."""
        feeCalculator = BabySitterFeeCalculator()
        calculatedFee = feeCalculator.calculateFeeFromStartToBedtime(startTime=17, bedTime=22)
        self.assertEquals(calculatedFee, 60.0)

    def testCalculateFeeFromBedtimeToMidnightWhenBedtimeIsBeforeMidnight(self):
        """When the bed time is 10:00pm calculate the correct fee until midnight."""
        feeCalculator = BabySitterFeeCalculator()
        calculatedFee = feeCalculator.calculateFeeFromBedtimeToMidnight(bedTime=22)
        self.assertEquals(calculatedFee, 16.0)

    def testWhenANumberAfterTheLatestEndTimeIsPassedReturnError(self):
        """When the end time is after 4:00am, an error should be returned."""
        feeCalculator = BabySitterFeeCalculator()
        with self.assertRaises(Exception) as context:
            feeCalculator.calculateFeeFromMidnightToEnd(endTime=5)
        self.assertTrue('The end time can not be after 4am!' in context.exception)


if __name__ == '__main__':
    unittest.main()