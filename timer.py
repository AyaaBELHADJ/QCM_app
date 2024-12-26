import time

class Timer:
    def __init__(self):
        self.start_time=None
        self.end_time=None
        self.duration=None
        self.is_running= False
    
    def enabled(self):
        return self.is_running
    
    def start(self):
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
