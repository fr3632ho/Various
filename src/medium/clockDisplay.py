import sys
import numbers

zero  = f'+---+\n|   |\n|   |\n+   +\n|   |\n|   |\n+---+'
one   = f'    +\n    |\n    |\n    +\n    |\n    |\n    +'
two   = f'+---+\n    |\n    |\n+---+\n|    \n|    \n+---+'
three = f'+---+\n    |\n    |\n+---+\n    |\n    |\n+---+'
four  = f'+   +\n|   |\n|   |\n+---+\n    |\n    |\n    +'
five  = f'+---+\n|    \n|    \n+---+\n    |\n    |\n+---+'
six   = f'+---+\n|    \n|    \n+---+\n|   |\n|   |\n+---+'
seven = f'+---+\n    |\n    |\n    +\n    |\n    |\n    +'
eight = f'+---+\n|   |\n|   |\n+---+\n|   |\n|   |\n+---+'
nine  = f'+---+\n|   |\n|   |\n+---+\n    |\n    |\n    +'
s     = f' \n \no\n \no\n \n '

nbrs = { '1' : one,
                   '2' : two,
                   '3' : three,
                   '4' : four,
                   '5' : five,
                   '6' : six,
                   '7' : seven,
                   '8' : eight,
                   '9' : nine,
                   '0' : zero,
                   'semi' : s}

semi = nbrs['semi'].split('\n')

def print_dict(d):
    print()
    for key,value in d.items():
        print(f'{key} -> {len(value)}')

def print_time(line):
    s = '  '
    words = line.split(':')
    t1,t2,t3,t4 = nbrs[words[0][0]],nbrs[words[0][1]],nbrs[words[1][0]],nbrs[words[1][1]]
    t1,t2,t3,t4 = t1.split('\n'),t2.split('\n'),t3.split('\n'),t4.split('\n')
    str = ''
    for i in range(0,len(t1)):
        str += t1[i] + s + t2[i] + s + semi[i] + s + t3[i] + s + t4[i] + '\n'
    print(str + '\n')

def print_times(data):
    for line in data:
        if line == 'end':
            print(line)
            break
        print_time(line)

input = sys.stdin.read().rstrip('\n').split('\n')
print_times(input)
print_dict(nbrs)



#END
