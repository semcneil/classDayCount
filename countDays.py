# countDays.py
#
# Counts how many of each day occurs between the startDate and endDate
# subtracting out nonSchoolDays.
#
# Seth McNeill
# 2022 July 19

from datetime import datetime, timedelta
import numpy as np

startDate = datetime.strptime('01/10/2024','%m/%d/%Y')  # can also use the datetime(YYYY,mm,dd) method
endDate = datetime.strptime('04/26/2024','%m/%d/%Y')  # np.arange does not include last date
dt = timedelta(days=1)
nonSchoolDays = (
  datetime(2024,1,15),    # MLK Jr day
  datetime(2024,2,19),    # Presidents day
  datetime(2024,3,11),  # Thanksgiving
  datetime(2024,3,12),  # Thanksgiving
  datetime(2024,3,13),  # Thanksgiving
  datetime(2024,3,14),  # Thanksgiving
  datetime(2024,3,15),  # Thanksgiving
  )

print(f'School starts: {startDate:%m/%d/%Y}')
daySum = np.zeros(7)

# Looping through dates method from:
# https://stackoverflow.com/a/37508911
for day in np.arange(startDate,endDate,dt).astype(datetime):
  daySum[day.weekday()] += 1

for day in nonSchoolDays:
  daySum[day.weekday()] -= 1
  print(f'No school on {day:%m/%d/%Y}')

print(f'Reading day is: {endDate:%m/%d/%Y}')

# print(daySum)

mwfDays = daySum[0]+daySum[2]+daySum[4]
trDays = daySum[1]+daySum[3]

print(f'MWF meetings: {mwfDays}')
print(f'TTH meetings: {trDays}')
print(f'T only: {daySum[1]}')
print(f'TH only: {daySum[3]}')
print(daySum)
