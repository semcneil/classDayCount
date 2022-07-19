# countDays.py
#
# Counts how many of each day occurs between the startDate and endDate
# subtracting out nonSchoolDays.
#
# Seth McNeill
# 2022 July 19

from datetime import datetime, timedelta
import numpy as np

startDate = datetime.strptime('8/29/2022','%m/%d/%Y')  # can also use the datetime(YYYY,mm,dd) method
endDate = datetime.strptime('12/9/2022','%m/%d/%Y')  # np.arange does not include last date
dt = timedelta(days=1)
nonSchoolDays = (
  datetime(2022,9,5),    # MLK
  datetime(2022,10,6),   # Fall Expo
  datetime(2022,10,13),  # Fall Break
  datetime(2022,10,14),  # Fall Break
  datetime(2022,11,11),  # Veterans day
  datetime(2022,11,23),  # Thanksgiving
  datetime(2022,11,24),  # Thanksgiving
  datetime(2022,11,25),  # Thanksgiving
  datetime(2022,11,26),  # Thanksgiving
  )

daySum = np.zeros(7)

# Looping through dates method from:
# https://stackoverflow.com/a/37508911
for day in np.arange(startDate,endDate,dt).astype(datetime):
  daySum[day.weekday()] += 1

for day in nonSchoolDays:
  daySum[day.weekday()] -= 1

# print(daySum)

mwfDays = daySum[0]+daySum[2]+daySum[4]
trDays = daySum[1]+daySum[3]

print(f'MWF meetings: {mwfDays}')
print(f'TTH meetings: {trDays}')
print(f'T only: {daySum[1]}')
print(f'TH only: {daySum[3]}')
