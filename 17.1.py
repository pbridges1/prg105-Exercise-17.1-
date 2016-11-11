class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_sec(self):
        hr = self.hour * 60 * 60
        mt = self.minute * 60
        sec = self.second + hr + mt
        print 'The time being converted is ' + '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
        print '\n'
        return 'The time converted into seconds is %d seconds ' % sec


time = Time()
time.hour = 11
time.minute = 30
time.second = 45

print time.time_to_sec()

# Answer to question:
# I would invoke int_to_time with the time_to_sec method.


# def adjust(t, inc):
#    t1 = t
#    t1 = (t1 + inc)
#    return t1

# user = raw_input("Enter how many seconds you would like to adjust: \n")
# new_time = adjust(time_to_sec(time.hour, time.minute), int(user))
# print ("\nYou entered " + str(user) + " seconds")

# answer = raw_input("Is this correct? \n")
# while answer != "yes":
#    user = raw_input("Please Re-enter how many seconds you would like to adjust: \n")
#    print ("\nYou entered " + str(user) + " seconds")
#    answer = raw_input("Is this correct? \n")


# def int_to_time(seconds):
#    t = Time()
#    minutes, time.second = divmod(seconds, 60)
#    time.hour, time.minute = divmod(minutes, 60)
#    return t
# times = int_to_time(new_time)
# if time.second > 60:
#    time.second -= 60
#    time.minute += 1
# if time.minute > 60:
#    time.minute -= 60
#    time.hour += 1
# if time.hour > 12:
#   time.hour -= 12

# print ('\nThe new incremented time is ' + '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
