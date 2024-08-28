# Create a class called TimeUtils that has a static method called time_to_seconds
#  that takes a time string in the format hh:mm:ss and returns the total number of seconds represented by that time.


class TimeUtils:
    @staticmethod
    def time_to_seconds(time_str):
        h, m, s = map(int, time_str.split(':'))
        return h * 3600 + m * 60 + s

print(TimeUtils.time_to_seconds('12:30:15')) # 45015
print(TimeUtils.time_to_seconds('00:00:00')) # 0
print(TimeUtils.time_to_seconds('01:00:00')) # 3600
print(TimeUtils.time_to_seconds('00:01:00')) # 60