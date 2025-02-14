import sys
import time as t
import timetracker as tt
import unittest

class TestTimeTracker(unittest.TestCase):
    VERBOSE = False
    def identify(func):
        def wrapper(*args, **kwargs):
            if TestTimeTracker.VERBOSE: print(f"\nTEST: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

    def setUp(self):
        self.timer = tt.TimeTracker()
        t.sleep(3)

    def test_3_seconds(self):
        self.timer.stop()
        seconds = self.timer.seconds
        with self.subTest(seconds=seconds):
            self.assertEqual(int(seconds), 3)

    def test_3_seconds_formatted(self):
        timevalue = self.timer.split()
        with self.subTest(timevalue=timevalue):
            self.assertEqual(timevalue, "00:00:03.000")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-v':   
        TestTimeTracker.VERBOSE = True
    else:
        TestTimeTracker.VERBOSE = False
        
    unittest.main()
# # Example Usage
# timer = ProcessTimer()
# timer.start()
#
# # Print split time
# print(timer.split())
#
# # Perform some process here...
# timer.stop()
