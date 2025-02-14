#timetracker.py

import time

class TimeTracker:
    """
        A class that tracks start, stop and elapsed times with formatting
        
        :Example:
        >>> timer = TimeTracker()
    """
    def __init__(self) -> None:
        self.restart()

    def restart(self) -> None:
        """
            A method that explicitly starts/restarts the timer
            
            :Example:
            >>> timer.restart()
        """
        self.start_time: float = time.perf_counter()
        self.stop_time = None
        self.elapsed_time = None

    def stop(self) -> None:
        """
            A method that stops the timer and calculates elapsed time
            
            :Example:
            >>> timer.stop()
        """
        assert self.start_time is not None, "Timer has not been started."
        self.stop_time: float = time.perf_counter()
        self.elapsed_time: float = self.stop_time - self.start_time
        total_seconds: float = self.elapsed_time
        self.hours, remainder = divmod(total_seconds, 3600)
        self.minutes, self.seconds = divmod(remainder, 60)
        self.milliseconds: float = (self.seconds - int(self.seconds)) * 1000

    def split(self) -> str:
        """
            A method that returns a formatted split time
            
            :Example:
            >>> timer.split()
            00:00:03.00
            
            :returns: The formatted elapsed time.
            :rtype: str
        """
        self.stop()
        self.elapsed_time_formatted: str = f"{int(self.hours):02}:{int(self.minutes):02}:{int(self.seconds):02}.{int(self.milliseconds):03}"
        return self.elapsed_time_formatted

if __name__ == "__main__":
    duration: int = 3
    print(f'Starting timetracker.py with a {duration} second duration')
    timer = TimeTracker()
    time.sleep(duration)
    print(f"- split time: {timer.split()}")
    print('Stopping timetracker.py')
