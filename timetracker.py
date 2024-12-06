#timetracker.py

import time

class TimeTracker:
    def __init__(self):
        self.start()

    def start(self):
        self.start_time = time.perf_counter()
        self.stop_time = None
        self.elapsed_time = None

    def stop(self):
        assert self.start is not None, "Timer has not been started."
        
        self.stop_time = time.perf_counter()
        self.calculate_elapsed_time()

    def split(self):
        self.stop()
        self.elapsed_time_formatted = f"{int(self.hours):02}:{int(self.minutes):02}:{int(self.seconds):02}.{int(self.milliseconds):03}"
        return self.elapsed_time_formatted

    def calculate_elapsed_time(self):
        if self.start_time is None:
            raise ValueError("Timer has not been started.")

        if self.stop_time is None:
            raise ValueError("Timer has not been stopped.")

        self.elapsed_time = self.stop_time - self.start_time
        total_seconds = self.elapsed_time
        self.hours, remainder = divmod(total_seconds, 3600)
        self.minutes, self.seconds = divmod(remainder, 60)
        self.milliseconds = (self.seconds - int(self.seconds)) * 1000

if __name__ == "__main__":
    import time
    timer = TimeTracker()
    timer.start()
    time.sleep(3)
    print(timer.split())