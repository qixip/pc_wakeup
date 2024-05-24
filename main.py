import schedule
import time
import os
from datetime import datetime


def wake_pc():
    os.system("wake_from_sleep.bat")


def set_alarm(time_str):
    alarm_time = datetime.strptime(time_str, "%I:%M %p")
    schedule.every().day.at(alarm_time.strftime("%H:%M")).do(wake_pc)


if __name__ == "__main__":
    alarm_time_str = input("Enter the alarm time AM or PM ")
    set_alarm(alarm_time_str)

    while True:
        schedule.run_pending()
        time.sleep(1)
