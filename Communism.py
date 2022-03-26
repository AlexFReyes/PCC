import datetime as d
from sqlite3 import Date
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
for i in roster_raw:
    roster_raw[roster_raw.index(i)] = i.strip()

roster_dict = {}
rd_key = 0
for i in range(0,len(roster_raw),2):
    if i == len(roster_raw):
        roomate = roster_raw[-1]
    else:
        roomate = roster_raw[i+1].title()

    roster_dict[rd_key] = roster_raw[i].title() + '. & ' + roomate + '.'

    rd_key += 1

base_date = d.datetime(2022, 3, 25)
dates_list = [base_date + d.timedelta(days = day) for day in range(len(roster_dict)+1)]

work_schedule = {}
for i in range(0,len(roster_dict)): 
    ws_key = str(dates_list[i].month) + '/' + str(dates_list[i].day)
    work_schedule[ws_key] = roster_dict[i]

ws_keys = list(work_schedule.keys())
ws_values = list(work_schedule.values())

print('Enter a date to find worker duties for that date (M/D)\nor press enter')
date = input()
if date == "":
    print('Please enter your first name and first letter of your last name(first name initial)')
    name = input()
    print(f'Comrades {ws_values.index(name.lower)}, your work day is {ws_keys[ws_values.index(name.lower)]}.')




print(f'Comrades {work_schedule[date]} have duties on {date}. ')