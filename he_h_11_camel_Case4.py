import re

inputSample0 = 'S;M;thisIsAMethod()'
inputSample1 = 'S;V;thisIsAVariable'
inputSample2 = 'S;C;ThisIsAClass'
inputSample3 = 'S;V;iPad'
inputSample4 = 'S;C;OrangeHighlighter'
inputSample5 = 'C;M;this is a method'
inputSample6 = 'C;V;this is a variable'
inputSample7 = 'C;M;mouse pad'
inputSample8 = 'C;C;code swarm'
inputSample9 = 'C;C;this is a class'

list = ['S;M;thisIsAMethod()',
        'S;V;thisIsAVariable',
        'S;C;ThisIsAClass',
        'S;V;iPad',
        'S;C;OrangeHighlighter',
        'C;M;this is a method',
        'C;V;this is ',
        'a variable',
        'C;M;mouse pad', 'C;C;code swarm', 'C;C;this is a class']


def camelcase(input_string: str):
    output = input_string[4:]
    if input_string[0] == 'S':
        # all need to be lowercase, and separate on capital letters
        # method extra remove '()'
        if input_string[-2:] == '()':
            output = output[:-2]

        output = (' '.join(re.split('(?=[A-Z])', output)).lower())
        if input_string[2] == 'C':
            output = output.strip()

    if input_string[0] == 'C':
        output = output.title()
        if input_string[2] == 'V':
            output = output[0].lower() + output[1:]
        if input_string[2] == 'M':
            output = output[0].lower() + output[1:] + '()'
        output = output.replace(" ", "")
    print(output)


a = Console.Readline()

for i in a:
    camelcase(i)
