from datetime import datetime, timedelta

import pytz
from tabulate import tabulate

IST = pytz.timezone('Asia/Kolkata')

now = datetime.now(IST)

current_day = now.strftime("%A")
current_time = now.strftime("%I:%M %p")
current_date = now.strftime("%d %m %Y")

sub_dict = {
    'cl': 'Calculus Lab',
    'ss': 'Soft Skill',
    'eng': 'English',
    'chem': 'Chemistry',
    'pl': 'Python Lab',
    'c': 'Calculus',
    'eee': 'EEE',
    'eeel': 'EEE Lab',
    'el': 'English Lab',
    'chl': 'Chemistry Lab',
    'pt': 'Python Theory'
}

name_dict = {
    'mcr': 'AB1-510',
    'calcl': 'AB1-707',
    'pyl': 'AB1-210',
    'eeel': 'AB1-306',
    'engl': 'AB2-701A',
    'cheml': 'AB1-120C',
}

time_dict = {
    9: '09:50 AM',
    2: '02:00 PM',
    5: '04:45 PM',
    3: '02:55 PM',
    8: '08:00 AM',
    4: '03:50 PM',
    6: '05:40 PM',
}

time_table = {
    "Monday": [
        [sub_dict['cl'], name_dict['calcl'], time_dict[9]],
        [sub_dict['ss'], name_dict['mcr'], time_dict[2]],
        [sub_dict['eng'], name_dict['mcr'], time_dict[3]],
        [sub_dict['chem'], name_dict['mcr'], time_dict[5]],
    ],
    "Tuesday": [
        [sub_dict['pl'], name_dict['pyl'], time_dict[8]],
        [sub_dict['chem'], name_dict['mcr'], time_dict[2]],
        [sub_dict['c'], name_dict['mcr'], time_dict[4]],
        [sub_dict['eee'], name_dict['mcr'], time_dict[5]],
        [sub_dict['eeel'], name_dict['eeel'], time_dict[6]],
    ],
    "Wednesday": [
        [sub_dict['el'], name_dict['engl'], time_dict[8]],
        [sub_dict['eee'], name_dict['mcr'], time_dict[2]],
        [sub_dict['ss'], name_dict['mcr'], time_dict[3]],
        [sub_dict['eng'], name_dict['mcr'], time_dict[4]],
    ],
    "Thursday": [
        [sub_dict['pl'], name_dict['pyl'], time_dict[8]],
        [sub_dict['chem'], name_dict['mcr'], time_dict[3]],
        [sub_dict['c'], name_dict['mcr'], time_dict[5]],
    ],
    "Friday": [
        [sub_dict['chl'], name_dict['cheml'], time_dict[9]],
        [sub_dict['c'], name_dict['mcr'], time_dict[2]],
        [sub_dict['eee'], name_dict['mcr'], time_dict[3]],
        [sub_dict['ss'], name_dict['mcr'], time_dict[4]],
        [sub_dict['pt'], name_dict['mcr'], time_dict[5]],
    ]
}


def dayfinder(n):
    zxs = datetime.strptime(n, '%d %m %Y').weekday()
    day = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    return day[zxs]


def main():

    print(f"{current_day}, {current_time}\n")

    uxlist = [['Query', 'Command'], ['Next class', 'Next'],
              ['Morning classes', 'AM'], ['Afternoon classes', 'PM'],
              ['All classes', 'All']]

    print(tabulate(uxlist, headers='firstrow', tablefmt='grid'), end='\n\n')

    print(
        "Commands show today's classes by default. To check classes for a specific date, use the command followed by the date, e.g., AM 06 09 2024"
    )

    enquiry = input("\nEnter your query: ").lower().strip()

    try:
        a, b = enquiry.split(' ', 1)
    except ValueError:
        a = enquiry
        b = current_date

    da, mo, ye = b.split(' ')

    if int(mo) > 11 or int(ye) > 2024:
        print('Stay tuned for upcoming semester timetable update ;)')
        exit()

    processing(a, b)


def processing(n, date):

    current_day = dayfinder(date)

    if current_day == 'Sunday' or current_day == 'Saturday':
        print(f'\n{current_day}')
        print(f"\nNo classes on {date}. Have a nice weekend!")
    else:
        a = time_table[current_day]

        if n == 'next':
            j = 0
            try:
                for i in a:
                    if compare(current_time, i[2]):
                        break
                    else:
                        j += 1
                output_table(a[j][0], a[j][1], a[j][2])
            except IndexError:
                print('You don\'t have any more classes today :)')

        elif n == 'pm':
            print(f'\n{current_day}')
            for i in a:
                if compare("12:00 PM", i[2]):
                    output_table(i[0], i[1], i[2])

        elif n == 'am':
            print(f'\n{current_day}')
            for i in a:
                if compare(i[2], "12:00 PM"):
                    output_table(i[0], i[1], i[2])

        elif n == 'all':
            print(f'\n{current_day}')
            for i in a:
                output_table(i[0], i[1], i[2])

        else:
            print('\nInvalid command.')
            


def compare(comt, clst):
    format_str = "%I:%M %p"
    t1 = datetime.strptime(comt, format_str)
    t2 = datetime.strptime(clst, format_str)
    if t2 > t1:
        return True


def end_time(n, delta):
    time_obj = datetime.strptime(n, "%I:%M %p")
    end_time_fr = time_obj + timedelta(minutes=delta)
    return end_time_fr.strftime("%I:%M %p")


def output_table(a, b, c):
    delta = 100 if 'Lab' in a else 50
    col1 = [a, b, c, end_time(c, delta)]
    col2 = ['Class', 'Room no', 'Start time', 'End time']
    table = zip(col2, col1)
    print(tabulate(table, tablefmt='grid'))


main()
