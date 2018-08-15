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

    def testCalculateFeeFromMidnightToLatestEnd(self):
        """When the end time is 4:00am, calculate the correct fee since midnight."""
        feeCalculator = BabySitterFeeCalculator()
        calculatedFee = feeCalculator.calculateFeeFromMidnightToEnd(endTime=4)
        self.assertEquals(calculatedFee, 64.0)

    def testCalculateMaxFee(self):
        """Calculate the fee for a full night of babysitter work."""
        feeCalculator = BabySitterFeeCalculator()
        calculatedFee = feeCalculator.calculateTotalFee(startTime=17, bedTime=0, endTime=4)
        self.assertEquals(calculatedFee, 148.0)

    def testCalculateFeeWhenBedtimeIsBeforeMidnightAndEndIsBeforeMax(self):
        """Calculate the fee for when bedtime is before midnight and endtime is before max endtime."""
        feeCalculator = BabySitterFeeCalculator()
        calculatedFee = feeCalculator.calculateTotalFee(startTime=17, bedTime=22, endTime=2)
        self.assertEquals(calculatedFee, 108.0)

    def testCalculateFeeWhenBedtimeIsIsNotSpecified(self):
        """Calculate the fee for when bedtime is not specified."""
        feeCalculator = BabySitterFeeCalculator()
        calculatedFee = feeCalculator.calculateTotalFee(startTime=17, endTime=4)
        self.assertEquals(calculatedFee, 148.0)

if __name__ == '__main__':
    unittest.main()
