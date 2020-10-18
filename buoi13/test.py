from datetime import datetime

date_str='2020-12-09'
date_object=datetime.strptime(date_str,'%Y-%m-%d').date()
now_date=datetime.now().date()
a=(now_date-date_object)
print(date_object)
print(now_date)
print(a.days)
