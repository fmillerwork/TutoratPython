class Time:
    def __init__(self, NewtimeInSec):
        self.timeInSec = NewtimeInSec

    def convert_to_minutes(self):
        return str(self.timeInSec // 60) + ":" + str(self.timeInSec % 60)
    
    def convert_to_hours(self):
        
        return str(self.timeInSec // 3600) + ":" + str((self.timeInSec % 3600) // 60) + ":" + str(self.timeInSec % 60)

time1 = Time(100)
print(time1.convert_to_minutes())

time2 = Time(3763)
print(time2.convert_to_hours())
