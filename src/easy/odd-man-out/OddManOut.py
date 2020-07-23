import sys

'''
Problem of finding the odd man out at a dinner party with pairs given N guests and all given
a number as identification. Find the person who came alone to the party.
'''
def mergeSort(oldList):
    if len(oldList) > 1:
        middle_point = len(oldList)//2

        # Split the lists
        left = oldList[:middle_point]
        right = oldList[middle_point:]

        # Recursively sort the arrays!
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                oldList[k] = left[i]
                i+=1
            else:
                oldList[k] = right[j]
                j+=1
            k+=1

        # Check if there are any elements left
        while i < len(left):
            oldList[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            oldList[k] = right[j]
            j+=1
            k+=1

def solve(g,ids):
    mergeSort(ids)

    for id in range(0,len(ids),2):
        if id+1 >= len(ids):
            print(f'Case #{count}: {ids[id]}')
            break
        else:
            if ids[id] != ids[id+1]:
                print(f'Case #{count}: {ids[id]}')
                break

line = sys.stdin.readline().rstrip()
count = 0
while line:
    if not count:
        count+=1
        line = sys.stdin.readline().rstrip()

    guests = int(line)
    ids = [int(x) for x in sys.stdin.readline().rstrip().split(' ')]
    solve(guests,ids)

    count+=1
    line = sys.stdin.readline().rstrip()




#END
