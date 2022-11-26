s = 'SOESSSROROOO'



def marsExploration(s: str) -> int:
    counter = 0
    sos_number = int(len(s)/3)
    sos_pattern = ('SOS' * sos_number)
    for letter in range(0, len(s)):
        if s[letter] != sos_pattern[letter]:
            counter += 1
    return counter

print(marsExploration(s))

