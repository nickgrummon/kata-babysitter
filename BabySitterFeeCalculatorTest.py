#!/usr/bin/env python
import unittest
from BabySitterFeeCalculator import BabySitterFeeCalculator

class TestBabySitterFeeCalulator(unittest.TestCase):
    """Tests for the BabySitterFeeCalculator."""

    def testWhenANumberBeforeTheStartTimeIsPassedReturnError(self):
        """When the start time is before 5:00pm, an error should be returned."""
        feeCalculator = BabySitterFeeCalculator()
        with self.assertRaises(Exception) as context:
            feeCalculator.calculateFeeFromStartToBedtime(startTime=16, bedTime=22)
        self.assertTrue('The start time can not be before 5pm!' in context.exception)


if __name__ == '__main__':
    unittest.main()