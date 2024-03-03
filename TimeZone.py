import time

timestamp = int(time.strftime('%H'))

if timestamp < 12:
    print("Good Morning")
elif 12 <= timestamp < 15:
    print("Good Afternoon")
elif 15 <= timestamp < 20:
    print("Good Evening")
else:
    print("Good Night")
