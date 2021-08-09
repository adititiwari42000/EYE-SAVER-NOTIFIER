
import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        app_name = "BLINK YOUR EYES",
        #app_icon = " C:\Users\hp\Downloads\eye.ico ",
        title = "INTERMISSION NOTIFIER",
        message = " It's the time to take a break ! Blink your Eyes , Save your Eyes !  ",
        timeout = 12


    )
    time.sleep(20*60) # it will notify in every hour
