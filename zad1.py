from datetime import datetime

start = datetime(2018, 12, 31)
day = datetime.utcnow() - start
print(day.total_seconds()/(3600*24))
