from datetime import datetime

date_1jun = datetime(2024, 1, 1)
difference = date_1jun - datetime.now()
hours = divmod(difference.seconds, 3600)
minutes = divmod(hours[1], 60)
seconds = divmod(minutes[1], 1)
print(f"the 1st of January is in {difference.days} days and {hours[0]}:{minutes[0]}:{seconds[0]}")

