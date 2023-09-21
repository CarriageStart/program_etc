from enum import Enum
from functools import total_ordering

@total_ordering
class Grade(Enum):
    A = 5
    B = 4
    C = 3
    D = 2
    E = 1
    F = 0

    def __it__(self, other):
        if self.__class is other.__class__:
            return self.value < other.value
        return NotImplemented


Grade.A >= Grade.B # True
Grade.A >= 3 # NotImplemented
# Acces the numerical value via ".value"



from enum import Flag
class Weekday(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 4
    FRIDAY = 4
    SATURDAY = 4
    SUNDAY = 4


first_week_day = Weekday.MONDAY
first_week_day

weekend = Weekday.SATURDAY | Weekday.SUNDAY
weekend
for day in weekend:
    print(day)








