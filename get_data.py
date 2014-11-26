import re


def needle(pattern, line):
    r = re.compile(pattern)
    s = r.search(line)
    if s:
        d = s.groupdict()
        for i in d:
            if not d[i]:
                d[i] = ''

        return sorted(list(d.values()), key=lambda x: len(x))[-1]
    return ''


if __name__ == "__main__":
    hay = '''
    שלום, נוסע מאילת לירושלים היום ב18:30
    '''

    needle(r'\bל(?P<t>\w+)', hay)
    needle(r'\bמ(?P<t>\w+)', hay)