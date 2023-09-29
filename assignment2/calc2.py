# Kanyi Mwenda sct211-0012/2022

import datetime

# prompting input
print("Enter birth date(yyyy-mm-dd): ")
birth = input()

#splitting string input to separate numbers in order to create date object
birth = birth.split("-")
birth = datetime.date(int(birth[0]), int(birth[1]), int(birth[2]))

#getting the age in days 
today  = datetime.date.today() 
diff = today-birth
# print(diff)

# converting the datetime object to a suitable format
diff = str(diff)
diff = diff.split(" ")
days = int(diff[0])
print(days)

#computing ages
years = days // 365

months = (days - years*365) // 30

num_days = (days-years*365-months*30)

print(f" You are: {years} years, {months} months, {num_days} days old")



