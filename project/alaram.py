import datetime
import time 
import winsound

print("----simple Alaram clock-----")

alaram_time = input("enter alaram time (HH:MM, 24-hour format): ")
print (f"Alaram set for {alaram_time}.waiting...")\

while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now == alaram_time:
        print("⏰ Alarm Time! Wake up!")

        for i in range(5):
            winsound.Beep(1000 , 1000)
            print("Weak  up!!!!")

        break

    time.sleep(1)