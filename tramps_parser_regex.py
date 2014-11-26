import re
from styling import style_time, style_phone_number
import get_data


with open('cities.txt') as f:
    cities_set = set(f.readlines())
    from_cities_set = set([r'(\bמ(?P<f{}>{}))'.format(i, city.strip()) for i, city in enumerate(cities_set)])
    to_cities_set = set([r'(\bל(?P<t{}>{}))'.format(i, city.strip()) for i, city in enumerate(cities_set)])

    from_regex = r'{}'.format('|'.join(from_cities_set))
    to_regex = r'{}'.format('|'.join(to_cities_set))

with open('days.txt') as f:
    days_set = set([r'(\b(?P<d{}>{}))'.format(i, day.strip()) for i, day in enumerate(f.readlines())])
    days_regex = r'{}'.format('|'.join(days_set))

time_patterns_list = [r"(ב(?P<time1>\d{1,2}:\d{2}))",
                      r"(ב(?P<time2>\d{4}))",
                      r"(ב (?P<time3>\d+:\d+))",
                      r"(ב (?P<time4>\d{4}))",
                      r"((?P<time5>\d{1,2}:\d{2}-\d{1,2}:\d{2}))"]
time_pattern = '|'.join(time_patterns_list)
phone_patterns_list = [r"(\b(?P<phone1>\d{2,3}-\d{7,8})\b)",
                       r"(\b(?P<phone2>\d{10})\b)"]
phone_pattern = '|'.join(phone_patterns_list)

with open('tramps.txt') as f, open('tramps_table_regex.csv', 'w') as output:
    output.write('from,to,day,time\n')
    for line in f:
        info = {}

        info['time'] = style_time(get_data.needle(time_pattern, line))
        info['phone'] = style_phone_number(get_data.needle(phone_pattern, line))
        info['from'] = get_data.needle(from_regex, line)
        info['to'] = get_data.needle(to_regex, line)
        info['day'] = get_data.needle(days_regex, line)

        print(info)
        output.write('{from},{to},{day},{time}\n'.format(**info))
