"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

args = sys.argv
if len(sys.argv) == 3:
  month =sys.argv[1]
  year =sys.argv[2]
elif len(sys.argv) == 2:
  month = sys.argv[1]
  year = str(datetime.today())[0:4]
elif len(sys.argv) == 1:
  month = str(datetime.today())[5:7]
  year = str(datetime.today())[0:4]
else:
  print('Please run command with this format 14_cal.py month [year]')



print(calendar.month(int(year), int(month)))