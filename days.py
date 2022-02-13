import datetime

examDay = datetime.datetime(2022, 5, 9)
currentDay = datetime.datetime.now()
answer = str(examDay - currentDay)
x = (answer.split(","))
print(x[0])
