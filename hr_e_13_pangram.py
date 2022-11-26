import string
a = 'abc'


def isPangram(text: string) -> str:
    set_a = set(text.casefold())
    set_alfabet = set(' '+string.ascii_lowercase)
    if set_alfabet <= set_a:
        pangram = 'pangram'
    else:
        pangram = 'not pangram'
    return pangram


print(isPangram(a))
