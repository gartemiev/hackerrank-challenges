#Standart solution without massive Python3 features
def timeConversion(s):
    if 'PM' in s and s[0:2] != '12' and 'AM' not in s:
        s = s.replace(s[0:2], str(int(s[0:2]) + 12)).replace('PM','')
    elif 'AM' in s and s[0:2] == '12':
        s = s.replace(s[0:2], '0' + str(int(s[0:2]) - 12)).replace('AM', '')
    elif 'PM' in s and s[0:2] == '12':
        s = s.replace('PM', '')
    else:
        s = s.replace('AM', '')

    return s


#With strptime
from datetime import datetime


s = '07:05:45AM'
def timeConversion2(s):
    s = datetime.strptime(s, '%I:%M:%S%p')
    print(s.strftime('%H:%M:%S'))

print(timeConversion2(s))