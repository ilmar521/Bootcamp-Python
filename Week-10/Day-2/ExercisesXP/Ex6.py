from datetime import datetime

date_pesah = datetime(2023, 4, 4, 18, 00)
difference = date_pesah - datetime.now()
hours = divmod(difference.seconds, 3600)
minutes = divmod(hours[1], 60)
seconds = divmod(minutes[1], 1)
print(f"the next Pesah is in {difference.days} days and {hours[0]}:{minutes[0]}:{seconds[0]}")

