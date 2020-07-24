import sys

COKE = 8
coins = [1, 5, 10]

def buy_cokes(amount, cokes):
    index = 2
    for i in range(3):
        if not amount[i]:
            break
        index = i

    count = 0
    current_value = coins[index]
    coins_used = 1
    while count != cokes:

        i = amount[index]
        for _ in range(i+1):
            if count == cokes:
                break

            if current_value >= COKE:
                amount[0] += current_value - COKE
                count += 1
                current_value = 0
                continue

            if amount[index]:
                current_value += coins[index]
                coins_used += 1
            else:
                break
        index -= 1

    print(coins_used)



def main():
    T = int(input())
    for i in range(T):
        C, n1, n5, n10 = map(int , input().split())
        currencies = [n1, n5, n10]
        buy_cokes(currencies, C)


if __name__ == "__main__":
    main()
