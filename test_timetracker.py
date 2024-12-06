import time as t
import timetracker as tt
import unittest

class TestMain(unittest.TestCase):
    def setUp(self):
        self.timer = tt.TimeTracker()
        t.sleep(3)

    def test_3_seconds(self):
        self.timer.stop()
        seconds = self.timer.seconds
        with self.subTest(seconds=seconds):
            self.assertEqual(int(seconds), 3)

    def test_3_seconds_formatted(self):
        self.timer.split()
        timevalue = self.timer.elapsed_time_formatted
        with self.subTest(timevalue=timevalue):
            self.assertEqual(timevalue, "00:00:03.000")

# # Example Usage
# timer = ProcessTimer()
# timer.start()
# # Perform some process here...
# timer.stop()