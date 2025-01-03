import time
class Timer:

    def __init__(self, time_limit):
        self.time_limit = time_limit  # Time limit in seconds
        self.time_left = time_limit
        self.timer_running = True

    def start(self):
        """Start the timer in the background."""
        while self.time_left > 0 and self.timer_running:
            time.sleep(1)  # Wait for one second
            self.time_left -= 1

        if self.time_left <= 0:
            print("\n[red]Time's up! The quiz is over.[/red]")  # Notify the user when time is up
            self.timer_running = False  # Stop the timer


    #def __init__(self):
        self.start_time=None
        self.end_time=None
        self.duration=None
        self.is_running= False
    
    def enabled(self):
        return self.is_running
    
   # def start(self):
        if not self.is_running:
            self.is_running= True   
            self.start=time.time 
            print("Timer started!") 
        else: print("Timer is already running.")
        
    def stop(self):
        if self.is_running:
            self.end_time= time.time
            self.duration = self.end_time - self.start_time  # Calculate the duration
            self.is_running = False
            print(f"Timer stopped! Duration: {self.duration:.2f} seconds.") 
        else:
            print("Timer is not running.")