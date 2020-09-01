import datetime
currentDate = datetime.datetime.now()

deadline= input ('Plz enter your date of birth (mm/dd/yyyy) ')
deadlineDate= datetime.datetime.strptime(deadline,'%m/%d/%Y')
print (deadlineDate)
