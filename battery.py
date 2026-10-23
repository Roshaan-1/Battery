import psutil # For Monitoring Battery
from plyer import notification # To Display Notification
import time #
# To Start Batter Monitoring
battery = psutil.sensors_battery()

while True:
    try:
        #Incase If there is a Problem
        if battery is None:
            print("Battery information unavailable")
        # 
        percentage = battery.percent
        plugged = battery.power_plugged
        #
        if percentage <= 30 and not plugged:
            notification.notify(
                title="BATTERY LOW",
                message=f"{percentage}% battery remaining! Please plug  the charger.",
                timeout=5)
    
        elif percentage == 100 and plugged == True:
            notification.notify(
                title="BATTERY FULLY CHARGED",
                message=f"{percentage}% battery is fully charged! Please unplug in the charger.",
                timeout=5 )
        # Will Wait 60 sec b4 checking it again        
        time.sleep(60)
    except :
        print("System is Keep Monitoring Your Battery")
        # Will Wait 60 sec b4 entering while loop
        time.sleep(60)
    

