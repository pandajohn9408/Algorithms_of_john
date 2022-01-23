from datetime import datetime

someday = datetime(2016,9,16,22,33,32,7)
today = datetime.utcnow()
print(someday.min)
print(today)