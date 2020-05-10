import sys


def parse_data():
    data = sys.stdin.read().split('\n')
    data = data[:len(data)-2]
    return data

def count_votes(v):
    candidates = dict()

    for vote in v:
        if vote not in candidates:
            candidates[vote] = 1
        else:
            candidates[vote] += 1

    max_candidate = max(candidates,key=candidates.get)
    values = candidates.values()

    count = 0
    for i in values:
        if i == candidates[max_candidate]:
            count+=1
    if count > 1:
        print("Runoff!")
    else:
        print(max_candidate)


data = parse_data()
count_votes(data)
