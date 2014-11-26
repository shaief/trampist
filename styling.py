def style_time(time):
    '''
    This function style time string to hh:mm format.
    :param time: string
    :return: string
    '''
    if time:
        if len(time) >= 5:
            return time
        if len(time) == 3:
            return '0{}:{}'.format(time[0], time[1:])
        return '{}:{}'.format(time[:2], time[2:])
    return time


def style_phone_number(number):
    '''
    This function style phone number string to match
    prefix{3}-number{7}
    :param number: string
    :return: string
    '''
    if number:
        if len(number) == 10:
            return '{}-{}'.format(number[:3], number[3:])
        elif not number[4].isdigit():
            return '{}-{}{}'.format(number[:3], number[3], number[5:])
    return number


if __name__ == "__main__":
    assert style_time('') == ''
    assert style_time('0800') == '08:00'
    assert style_time('800') == '08:00'
    assert style_time('08:00') == '08:00'

    assert style_phone_number('') == ''
    assert style_phone_number('0545678789') == '054-5678789'
    assert style_phone_number('054-5678789') == '054-5678789'
    assert style_phone_number('0545-678789') == '054-5678789'
