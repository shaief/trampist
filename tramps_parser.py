definitions = {
    'from': u'מ',
    'to': u'ל',
    'at': u'ב',
}

empty_dict = {
    'from': '',
    'to': '',
    'day': '',
    'time': '',
    'phone': '',
}

AT_TIME = u'בשעה'
AT_DAY = u'ביום'

with open('cities.txt') as f:
    cities_set = set([city.strip() for city in f.readlines()])

with open('days.txt') as f:
    days_set = set([day.strip() for day in f.readlines()])

with open('tramps.txt') as f, open('tramps_table.csv', 'w') as output:
    output.write('from,to,day,time\n')
    for line in f:
        info = empty_dict
        sentence = [''.join(c for c in word if c.isalnum()) for word in line.split()]
        for i, word in enumerate(sentence):
            if word:
                if word[1:] in cities_set:
                    if i < len(sentence) - 1:
                        maybe = '{} {}'.format(word[1:], sentence[i + 1])
                        if maybe in cities_set:
                            place = maybe
                        else:
                            place = word[1:]
                    if word[0] == definitions['to']:
                        info['to'] = place
                    elif word[0] == definitions['from']:
                        info['from'] = place
                elif word[0] == definitions['at']:
                    if word[1:5].isdigit():
                        info['time'] = '{}:{}'.format(word[1:3], word[3:5])
                    else:
                        if word[1:] in days_set:
                            info['day'] = '{}'.format(word[1:])
                elif word in days_set and word != maybe:
                    info['day'] = '{}'.format(word)
                if len(word) == 4 and word.isdigit():
                    info['time'] = '{}:{}'.format(word[:2], word[2:4])
        if info['from'] or info['to']:
            if not info['time']:
                info['time'] = "בזמן לא ברור"
            print("טרמפ יוצא מ{from} ל{to} {day} {time}".format(**info))
            output.write('{from},{to},{day},{time}\n'.format(**info))
