from datetime import datetime

now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

with open("last_run.txt", "w", encoding="utf-8") as f:
    f.write(f"Dernière exécution : {now}\n")

print("Heure :", now)
