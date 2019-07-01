import datetime
musleh_birth_date = datetime.date(1999,3,10)
print(musleh_birth_date)
print(musleh_birth_date.year,musleh_birth_date.month,musleh_birth_date.day)
print(musleh_birth_date.strftime("%A, %B %d, %Y"))

message = "Musleh was born on {:A, %B %d, %Y}."
print(message.format(musleh_birth_date))
launch_time = datetime.time(22,22,0)
print(launch_time)
launch_datetime = datetime.datetime(1998,10,12,22,22,0)
print(launch_datetime)

#current date time
now = datetime.datetime.today()
print(now)
moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing,"%m/%d/%Y")
print(moon_landing_datetime)

dt = datetime.timedelta(100) #positive will add time and negative will subtract time
