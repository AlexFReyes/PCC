import datetime as d 
import random
from sqlite3 import Date

import numpy

#Dataset split on periods and made lowercase
roster_raw = '''
Valentine O.	Bradley M.
Corey C.	Emiliano C.
Landon R.	Christian M.
Hawthorne K.	Isaac A.
Sam F.	Indinma S.
James I.	Nate Z.
Fernando E.	Nick I.
Nick I.	Pablo AC.
EG P.	Mitchell G.
Fletcher B.	Luke N.
Dunkey C.	Tyler R.
Thomas R.	Gabe K.
Payton S.	Kevin W.
Kai M.	Mateus F.
Alex R.	Chris R.
Japhet H.	Everett P.
Tyler W.	Robbie R.
William J.	Ben P.
Reggie K.	Phasha M.
Sebastian V.	Paul F.
Riley S.	Mar’Quidric C.
Wyatt S.	Hamza N.
Elliott M.	Alex R 
'''.lower().split('.')

#stripping each index of blank space on either side
for i in roster_raw:
    roster_raw[roster_raw.index(i)] = i.strip()

#creating a list of pairs of roomates / workers
roster_pair_list = []
for i in range(0,len(roster_raw),2):
    #grabbing the i+1 index at max wouldn't work hence safety feature
    if i == len(roster_raw):
        roomate = roster_raw[-1]
    else:
        roomate = roster_raw[i+1]
    roster_pair_list.append(roster_raw[i] + ' & ' + roomate)

#shuffling the list for fairness
random.shuffle(roster_pair_list)

#start date / end date
print('Please enter the start and end dates of work duties (mm/dd/yyy):')
start_date_input = input('Start date:').split('/')
end_date_input = input('End date:').split('/')

#convert input to date format
s_date = d.datetime(int(start_date_input[2]), int(start_date_input[0]), int(start_date_input[1]))
e_date = d.datetime(int(end_date_input[2]), int(end_date_input[0]), int(end_date_input[1]))

#number of days in list
num_days = e_date - s_date

#a list of dates starting at ^ and going for the length of roster dictionary inclusive
dates_list = [s_date + d.timedelta(days = day) for day in range((num_days.days)+1)]

multiply_list_factor = round((num_days.days / len(roster_pair_list)))


while (len(roster_pair_list) < num_days.days):
    for i in range(len(roster_pair_list)):
        roster_pair_list.append(roster_pair_list[i])

work_schedule = {}
for i in range(0,num_days.days): 
        ws_key = str(dates_list[i].month) + '/' + str(dates_list[i].day) + str(s_date.year)
        work_schedule[ws_key] = roster_pair_list[i]
            

