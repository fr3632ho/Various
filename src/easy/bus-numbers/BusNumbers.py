import sys
from heapq import heappop,heappush,heapify
from collections import deque

N = sys.stdin.readline().rstrip()
buses = []
[heappush(buses,int(x)) for x in sys.stdin.readline().rstrip().split(' ')]

if len(buses) == 1:
    print(heappop(buses))
else:
    prev = heappop(buses)
    output_string = ""
    added_last = False
    while buses:
        top = heappop(buses)
        #print(f'OutStr: {output_string} Top: {top} Prev: {prev}')
        if top-prev == 1:
            streak = deque([prev])
            prev = top

            if not buses:
                streak.append(prev)
                added_last = True

            while buses:
                top = heappop(buses)
                #print(f'Prev: {prev} Top: {top} Streak: {streak} ')
                if top-prev ==1:
                    streak.append(prev)
                    prev = top
                    if not buses:
                        streak.append(prev)
                        added_last = True
                else:
                    streak.append(prev)
                    prev = top
                    break
            #print(f'\nFinal Streak: {streak}\n')
            if len(streak) > 2:
                output_string += f'{streak.popleft()}-{streak.pop()} '
            else:
                output_string += f'{streak.popleft()} {streak.popleft()} '
        else:
            output_string += f'{prev} '
            prev = top

        if not buses and not added_last:
            output_string += f'{prev}'


    if output_string[0] == " ":
        print(output_string[1:])
    else:
        print(output_string)
