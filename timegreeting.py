import time

#Making time to int so that we use to compair time
timestamp = time.strftime(' %H:%M:%S ')

print(timestamp)

a = int(time.strftime('%H'))

# checking for good morning
if (a < 12):
    print("Good Morning")

# checking for good afternoon
elif (a >= 12 and a <= 18):
    print("Good Afternoon")

elif ( a > 18 and a <= 20):
    print("goodevening")
else :
    print("Goodnight")
