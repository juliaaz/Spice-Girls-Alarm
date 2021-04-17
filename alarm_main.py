"""
Alarm module
"""
from datetime import datetime
import winsound
import time
import data_generating


class Alarm_Clock:
    """
    Alarm clock class
    """
    def __init__(self):
        self.alarm_time = None

    def validate_time(self):
        """
        Returns 'ok' if time is validate or message about an error otherwise
        """
        if len(self.alarm_time) != 8:
            return "Invalid time format! Please enter valid time."
        else:
            if int(self.alarm_time[0:2]) > 23:
                return "Invalid hour format! Please enter valid time."
            elif int(self.alarm_time[3:5]) > 59:
                return "Invalid minute format! Please enter valid time."
            elif int(self.alarm_time[6:8]) > 59:
                return "Invalid second format! Please enter valid time."
            else:
                return "ok"

    def set_alarm(self):
        """
        Sets alarm and returns alarm time
        """
        while True:
            self.alarm_time = input("Enter time in 'HH:MM:SS' format (24 hours format): ")
            
            valid = self.validate_time()
            if valid != "ok":
                print(valid)
            else:
                now = datetime.now()
                print('Current time: ',now.strftime("%H:%M:%S"))
                print(f"Setting alarm for {self.alarm_time}...")
                return self.alarm_time


    def run_alarm(self):
        """
        Runs alarm clock
        """
        self.alarm_hour = self.alarm_time[0:2]
        self.alarm_min = self.alarm_time[3:5]
        self.alarm_sec = self.alarm_time[6:8]

        while True:
            now = datetime.now()

            current_hour = now.strftime("%H")
            current_min = now.strftime("%M")
            current_sec = now.strftime("%S")

            if self.alarm_hour == current_hour:
                if self.alarm_min == current_min:
                    if self.alarm_sec == current_sec:
                        print("Wake Up!")
                        break

    def alarm_sound(self):
        """Make an alarm sound."""
        winsound.PlaySound("Wannabe.wav", winsound.SND_ASYNC)
        command = input("To stop alarm enter 'stop': ")
        while command != 'stop':
            command = input("To stop alarm enter 'stop': ")
        self.start_quiz(command)

    def start_quiz(self,command):
        """
        Stops alarm sound id command is 'stop'
        """
        if command == 'stop':
            winsound.PlaySound(None, winsound.SND_PURGE)

def main():
    """Main algorithms of the program."""
    alarm_clock = Alarm_Clock()
    alarm_clock.set_alarm()
    alarm_clock.run_alarm()
    res_of_quize = False
    while res_of_quize == False:
        alarm_clock.alarm_sound()
        res_of_quize = data_generating.generating_quiz()

        
if __name__ == '__main__':
    main()




