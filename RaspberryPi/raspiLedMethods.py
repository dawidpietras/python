import requests
import datetime

class LedControl:

    def __init__(self):
        self.sunset_time = []
        self.today = ''
        self.getSunset()
        self.whatDayIsToday()
        self.isWeekend()



    def on_or_off(self):
        today_old = self.today
        self.whatDayIsToday()
        if self.today != today_old:
            self.getSunset()
        on_or_off = self.isNightNow()
        return on_or_off

    def getSunset(self):
        response = requests.get("https://api.sunrise-sunset.org/json?lat=51.7687323&lng=19.4569911")
        response = response.json()['results']['sunset'].split(":")
        response.pop(2)
        response[0] = int(response[0]) + 14
        response[1] = int(response[1])
        self.sunset_time = response

    def whatTimeIsIt(self):
        actual_time = [0, 0]
        time = datetime.datetime.now().strftime("%X")
        time = time.split(":")
        time.pop(2)
        actual_time[0] = int(time[0])
        actual_time[1] = int(time[1])
        return actual_time

    def isNightNow(self):
        actual_time = self.whatTimeIsIt()
        if actual_time[0] > self.sunset_time[0]:
            return True
        elif actual_time[0] == self.sunset_time[0]:
            if actual_time[1] >= self.sunset_time[1]:
                return True
            else:
                return False
        else:
            return False

    def isWeekend(self):
        weekday = datetime.datetime.now().strftime("%A")
        if weekday == 'Friday' or weekday == 'Saturday' or weekday == 'Sunday':
            return True
        else:
            return False

    def whatDayIsToday(self):
        self.today = datetime.datetime.now().strftime("%A")




if __name__ == "__main__":
    led = LedControl()
    print(led.on_or_off())