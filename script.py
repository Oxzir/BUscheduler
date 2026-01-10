from datetime import datetime, time
from zoneinfo import ZoneInfo
import time as sleep_time

timezone = ZoneInfo("Europe/Paris")
target_time = time(10,0)
launchtime = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S %Z")

def wait_until_midnight():
    while True:
        now = datetime.now(timezone)
        if now.time() >= target_time:
            return now.strftime('%Y-%m-%d %H:%M:%S %Z')
        print(f"{now.strftime('%H:%M:%S')} : en attente de {target_time}")
        sleep_time.sleep(5)

wait_until_midnight()
with open("last_run.txt", "w", encoding="utf-8") as f:
    f.write(
        f"Lancement à {launchtime}\n"
        f"Exécution à {wait_until_midnight()}\n"
    )

print("Heure :", now)
