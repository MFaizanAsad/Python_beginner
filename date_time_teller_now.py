# Program to get the current date and time
from datetime import datetime

now = datetime.now()

mm = str(now.month)

dd = str(now.day)

yyyy = str(now.year)

hour = str(now.hour)

mi = str(now.minute)

ss = str(now.second)

print (f'{dd}-{mm}-{yyyy}  {hour}hr:{mi}min:{ss}sec')